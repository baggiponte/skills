#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/run-spark-curator.sh "objective text" [-C DIR] [-o FILE] [--json]
  scripts/run-spark-curator.sh -f OBJECTIVE_FILE [-C DIR] [-o FILE] [--json]

Options:
  -f, --objective-file FILE   Read objective text from FILE
  -C, --cd DIR                Target repository/workdir (default: .)
  -o, --output FILE           Write final assistant message to FILE
      --json                  Emit JSONL events from codex exec
  -h, --help                  Show this help
EOF
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYSTEM_PROMPT_FILE="$SCRIPT_DIR/../references/system-prompt.md"

WORKDIR="."
OBJECTIVE=""
OBJECTIVE_FILE=""
OUTPUT_FILE=""
USE_JSON=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    -f|--objective-file)
      OBJECTIVE_FILE="${2:-}"
      shift 2
      ;;
    -C|--cd)
      WORKDIR="${2:-}"
      shift 2
      ;;
    -o|--output)
      OUTPUT_FILE="${2:-}"
      shift 2
      ;;
    --json)
      USE_JSON=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      if [[ -z "$OBJECTIVE" ]]; then
        OBJECTIVE="$1"
      else
        echo "error: multiple objective arguments provided" >&2
        usage >&2
        exit 2
      fi
      shift
      ;;
  esac
done

if [[ ! -f "$SYSTEM_PROMPT_FILE" ]]; then
  echo "error: missing prompt file: $SYSTEM_PROMPT_FILE" >&2
  exit 1
fi

if [[ -n "$OBJECTIVE_FILE" ]]; then
  if [[ ! -f "$OBJECTIVE_FILE" ]]; then
    echo "error: objective file not found: $OBJECTIVE_FILE" >&2
    exit 1
  fi
  OBJECTIVE="$(cat "$OBJECTIVE_FILE")"
fi

if [[ -z "${OBJECTIVE// }" ]]; then
  echo "error: objective is required" >&2
  usage >&2
  exit 2
fi

CMD=(
  codex exec
  --model gpt-5.3-codex-spark
  --sandbox read-only
  --ephemeral
  --cd "$WORKDIR"
)

if [[ -n "$OUTPUT_FILE" ]]; then
  CMD+=(--output-last-message "$OUTPUT_FILE")
fi

if [[ "$USE_JSON" -eq 1 ]]; then
  CMD+=(--json)
fi

{
  cat "$SYSTEM_PROMPT_FILE"
  printf "\n\n## Objective\n%s\n" "$OBJECTIVE"
} | "${CMD[@]}" -
