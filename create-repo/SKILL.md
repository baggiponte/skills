---
name: create-repo
description: Create a new GitHub repository with gh and protect its default branch with the "main branch" ruleset in this skill's ruleset.json. Use whenever a new repository is created.
---

# Create repo

GitHub cannot protect a repository at creation time: `gh repo create` has no ruleset flag, template repositories copy files but not rulesets, and personal accounts have no account-wide rulesets. Create the repository, then apply the ruleset through the API.

## Steps

1. Create the repository. Ask for the name and visibility when they are not given; never guess visibility.

   ```sh
   gh repo create OWNER/NAME --public|--private [--description "..."] [--clone | --source . --push]
   ```

   The ruleset targets `~DEFAULT_BRANCH`, so it applies before the first commit.

2. Apply [ruleset.json](ruleset.json), which sits next to this file:

   ```sh
   gh api repos/OWNER/NAME/rulesets --method POST --input ruleset.json
   ```

3. Check that `gh api repos/OWNER/NAME/rulesets` lists `main branch` with `enforcement: active`, and report `https://github.com/OWNER/NAME/rules/<id>`.

## What the ruleset enforces

No branch deletion, no force pushes, signed commits, linear history, and changes through pull requests merged by squash with no required approvals. The repository Admin role (`actor_id: 5`) can always bypass it.

## Added later, not at creation

- **Required status checks.** A new repository has no CI yet, so required checks would block every pull request. Once its workflows have run, offer to add them: GET the ruleset, append a `required_status_checks` rule whose contexts are the job names (`integration_id: 15368` is GitHub Actions), and PUT it back to `repos/OWNER/NAME/rulesets/<id>`.
- **Merge queue.** GitHub offers a `merge_queue` rule only on repositories owned by an organization. Add it only for those, the same way as status checks.

## Failures

Never fall back silently or weaken the ruleset to make a call pass. The repository already exists at this point, so say plainly that it is unprotected.

- 403 asking to upgrade, on a private repository: rulesets on private repositories need a paid plan. Stop and tell the user; do not switch the repository to public.
- 422: show GitHub's message as it is.
- A ruleset exported from the GitHub UI carries read-only fields. Keep only `jq '{name,target,enforcement,conditions,rules,bypass_actors}'` before posting it.
