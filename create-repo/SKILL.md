---
name: create-repo
description: Create a GitHub repository and protect its default branch with this skill's ruleset. Use whenever a new repository is created.
---

`gh repo create`, template repositories and personal accounts cannot attach a ruleset, so the ruleset is posted right after creation.

1. Create the repository with `gh repo create`. Ask for visibility when the user has not given it.
2. Post the ruleset in this folder:
   `gh api repos/OWNER/NAME/rulesets --method POST --input ruleset.json`
   Done when `gh api repos/OWNER/NAME/rules/branches/DEFAULT_BRANCH` lists `pull_request`. Report `https://github.com/OWNER/NAME/rules/<id>`.
3. Once the repository's CI has run, offer to require its checks: add a `required_status_checks` rule with the job names as contexts (`integration_id: 15368`) and PUT the ruleset back to `repos/OWNER/NAME/rulesets/<id>`.

## Gotchas

- A private repository on a free plan answers 403: rulesets there need a paid plan. Tell the user the repository exists unprotected and keep its visibility.
- On any error, show GitHub's message and leave `ruleset.json` as it is.
- A ruleset exported from the GitHub UI carries read-only fields. Post `jq '{name,target,enforcement,conditions,rules,bypass_actors}'` of it.
