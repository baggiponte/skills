---
name: build-python-dockerfiles
description: Build production-ready Dockerfiles for Python projects that use uv. Use when creating or refactoring Dockerfiles for reproducible installs, cache-efficient builds, bytecode compilation, small runtime images, and non-root execution. Follows the production patterns from Hynek Schlawack's article "Production-ready Python Docker Containers with uv" while staying flexible about base images and app type. Supports packaged and unpackaged applications, including web apps, workers, and CLI services. Triggers on requests like "write a Dockerfile for this Python project", "optimize this uv Dockerfile", "containerize this FastAPI/Django/Flask app", "containerize this worker", or "split this into build and runtime stages".
---

# Build Python Dockerfiles

Use this skill to author Dockerfiles for Python projects using `uv` and multi-stage builds.
The default pattern is based on Hynek Schlawack's article [Production-ready Python Docker Containers with uv](https://hynek.me/articles/docker-uv/).

## Workflow

1. Detect whether the project is packaged (installable) or unpackaged (run from copied source).
2. Choose a base image strategy:
   - Default to `python:<version>-slim` for generic Python services.
   - Use an OS image like `ubuntu:noble` when system packages or org-standard base images matter.
   - Keep build and runtime on the same distro family.
   - Avoid Alpine unless the user has a hard requirement.
3. Install dependencies before copying source so lockfile changes and app code changes stay in separate layers.
4. Keep dependency sync and app install in separate `uv sync` steps.
5. Pick the runtime command pattern that matches the app type.
6. Verify the final Dockerfile against the checklist in this file.

## Required build patterns

- Use two stages: `build` and `final`.
- Add layers in inverse order of likely change frequency.
- Install dependencies before copying source to maximize cache hits.
- Keep dependency sync and app install in separate `RUN uv sync` steps.
- Use BuildKit cache mounts for the `uv` cache.
- Use `UV_PROJECT_ENVIRONMENT=/app` and copy `/app` into runtime image.
- Byte-compile Python files for faster startup with `UV_COMPILE_BYTECODE=1`.
- Run as non-root in runtime.
- Prefer `uv sync --locked` for deployment builds.

## Default settings

- Copy `uv` from `ghcr.io/astral-sh/uv:<version>`.
- Set:
  - `UV_LINK_MODE=copy`
  - `UV_COMPILE_BYTECODE=1`
  - `UV_PYTHON_DOWNLOADS=never`
  - `UV_PROJECT_ENVIRONMENT=/app`
- Set `UV_PYTHON` when the base image has multiple Python interpreters or when `uv` cannot infer the intended one cleanly.
- Use BuildKit cache mounts for the `uv` cache, typically `/root/.cache/uv` or `/root/.cache`.
- Never bake secrets into the Dockerfile via `ENV`.

## Baseline template

Use this as the default starting point for packaged applications:

```dockerfile
# syntax=docker/dockerfile:1.9

FROM python:3.13-slim AS build

COPY --from=ghcr.io/astral-sh/uv:0.8.15 /uv /uvx /bin/

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/app

WORKDIR /src
COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-install-project

COPY . /src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-editable

FROM python:3.13-slim AS final

ENV PATH="/app/bin:$PATH"
STOPSIGNAL SIGINT

RUN groupadd --system app && useradd --system --gid app --home-dir /app app

COPY --from=build --chown=app:app /app /app

USER app
WORKDIR /app

CMD ["python", "-m", "your_package"]
```

Keep the following adaptation rules in mind:

- If the project is not packaged, skip the second `uv sync` step and copy the source into the runtime image after copying `/app`.
- If the project has heavy OS-level build dependencies, use a fuller build image and only install runtime libraries in the final image.
- If the project needs a shell entrypoint or signal handling wrapper, use an explicit `ENTRYPOINT` script and keep `STOPSIGNAL SIGINT`.
- When using an OS image instead of `python:<version>-slim`, install the exact runtime Python packages explicitly and set `UV_PYTHON` if needed.

## Entrypoint patterns

Pick the startup command that matches the project type.

### ASGI (FastAPI, Starlette, Quart)

```dockerfile
EXPOSE 8000
CMD ["uvicorn", "your_package.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Django (WSGI)

```dockerfile
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]
```

### Flask or generic WSGI

```dockerfile
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_package.wsgi:app"]
```

### Background worker

```dockerfile
CMD ["python", "-m", "your_package.worker"]
```

### CLI or batch task container

```dockerfile
ENTRYPOINT ["python", "-m", "your_package.cli"]
```

Use JSON-array syntax for `CMD` and `ENTRYPOINT`.

## Final checklist

Run this checklist before finalizing output:

1. Multi-stage build is used.
2. `uv` is copied from the official image.
3. Dependency installation happens before source copy.
4. Dependency sync and application install are separate when the app is packaged.
5. A BuildKit cache mount is used for `uv`.
6. `UV_PROJECT_ENVIRONMENT=/app` is set and `/app` is copied into the runtime image.
7. The runtime image runs as a non-root user.
8. `PATH` includes `/app/bin` when executables live in the project environment.
9. Startup command is explicit and matches app type.
10. No secrets are baked into the image.
11. Optional but recommended: `STOPSIGNAL SIGINT`.
12. Optional but recommended: `EXPOSE` for network services.
13. Optional but recommended: a `.dockerignore` that excludes VCS data, caches, build artifacts, and local virtualenvs.

## Output contract

When generating a Dockerfile for a user:

1. Return a complete Dockerfile.
2. State assumptions briefly (Python version, packaged vs unpackaged, startup command).
3. Add a short `.dockerignore` suggestion when missing.
