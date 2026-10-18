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

Checks that miss that bar, and another model's approval, stay out of the body under any heading. For a skill or prompt, effectiveness requires observing its behavior on realistic tasks, not checking its packaging.

State verification gaps that affect confidence. Otherwise, omit an unsupported testing section rather than adding ceremonial checks or a stock disclaimer.

## Prune before publishing

Apply this filter to every sentence:

> What reviewer decision does this sentence support? If removing it hides no important intent, consequence, risk, or evidence, delete it.

Finish when every retained sentence serves a reviewer decision and every confidence claim is supported by what was actually observed.
