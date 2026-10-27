---
name: pr-descriptions
description: Write or revise pull request and merge request bodies as reviewer decision support, with meaningful evidence instead of activity logs.
---

# PR descriptions

A PR description is **decision support, not an activity log**. Include information that helps a reviewer understand the intent, assess consequences, or judge confidence in the change.

## Explain the change

Read the actual change and its originating request before drafting. Explain why it is needed, important behavior changes, and non-obvious trade-offs. Include risks or compatibility consequences when they affect the reviewer's decision.

Scale the body to the change. A short summary can be the entire description. Keep fields a repository template requires; omit optional headings that would carry nothing.

## Earn confidence claims

Report testing only when it actually exercises the changed behavior or a consequential invariant. State the scenario and observed result, with the limits of what that establishes. Distinguish executed checks from proposed checks.

Routine mechanical checks and another model's approval are not evidence that the change works. Leave those activities out of the body rather than relabeling them as validation, verification, or testing. For a skill or prompt, effectiveness requires observing its behavior on realistic tasks, not checking its packaging.

State verification gaps that affect confidence. Otherwise, omit an unsupported testing section rather than adding ceremonial checks or a stock disclaimer.

## Show the behavior

Include a before/after comparison or a demo of the new feature when a visual or behavioral change is easier to judge by seeing it. Keep inputs, data, and framing consistent across comparisons. Use the lightest format that makes the change clear: screenshots for static differences, a short recording for interactions, or sample input/output for non-visual behavior. Choose capture tools to suit the task; browser automation is optional.

Capture the actual behavior, label what each item shows, and include it in the description. After publishing, confirm that reviewers can view the evidence, including in private repositories; use durable links rather than local paths or expiring URLs. Skip media when text conveys the change equally well.

On GitHub, upload media with `--attach` on `gh pr create`, `gh pr edit` or `gh pr comment` (gh 2.99 or later), never by committing it to the branch. Reference each file by its local path in the body, then pass it as `--attach ./after.png` (alt text after `#` applies only to files the body does not reference): gh uploads it to GitHub's own attachment storage and rewrites the path in place; attached files the body does not reference are appended at the end. Limits: 50 files per command, 10 MiB per image, video (mp4, mov, webm) renders as a player with a plan-dependent size cap. Uploads are permanent and cannot be deleted, so attach only final media. It needs write access to the repository, does not work on GitHub Enterprise Server, and fails from Claude Code cloud sessions, whose GitHub proxy rejects binary uploads; there, hand the files to the user instead. On a partial failure gh keeps the successful uploads and exits non-zero, so check the exit code and re-read the body.

## Prune before publishing

Apply this filter to every sentence:

> What reviewer decision does this sentence support? If removing it hides no important intent, consequence, risk, or evidence, delete it.

The body is ready when every retained sentence and evidence item serves a reviewer decision, and every confidence claim is supported by what was actually observed.

## Assign the PR

When opening a PR or MR, assign it to the authenticated user unless the user requests another assignee. On GitHub, use `--assignee @me`; elsewhere, resolve the current account through the platform’s CLI or API. Verify the assignee on the created PR or MR. If account resolution or assignment fails, report it rather than guessing or silently leaving it unassigned.
