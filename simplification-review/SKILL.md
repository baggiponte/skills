---
name: simplification-review
description: Review code for unnecessary maintenance surface, question requirements, and keep only high-value tests.
disable-model-invocation: true
---

# Simplification review

Optimize for the smallest **maintenance surface**, not the fewest lines. Surface includes supported behaviors, interfaces, configuration, abstractions, dependencies, and test machinery. A few explicit branches can be simpler than a compact abstraction. Working code may already be the simplest option.

## 1. Establish the scope

Follow the user's scope: a codebase, a diff, or its tests. Inspect repository guidance, requirements, entrypoints, dependencies, CI, and representative data. Trace the relevant producers and consumers, including external interfaces; absence of a checked-in caller does not prove something is unused.

Distinguish existing behavior, documented requirements, and assumptions. Tests describe what the code currently enforces, not necessarily what the product needs. Finish with the behavior being protected and the evidence for it identified; mark uncertain consumers explicitly.

## 2. Challenge requirements before implementations

For complexity driven by a requirement, identify the real workflow or failure it protects. Propose the smallest useful rule, with a concrete scenario and its trade-off. Separate business facts from implementation restrictions: display precision need not dictate source formatting, for example.

Resolve only ambiguities that change the recommendation. Offer defaults and ask the owner the few questions that code cannot answer. Treat unconfirmed proposals as proposals; record accepted decisions in the existing domain documentation when editing is authorized.

Keep required security and data-integrity protections even when the failure is rare. Treat hypothetical future workflows as unsupported scope rather than building an extension mechanism for them. Finish with the requirements needed for this review settled or clearly flagged as blockers.

## 3. Review the surface

For each candidate, recommend **keep**, **delete**, **replace**, or **clarify**. Justify it with a consumer, requirement, or plausible failure—not a code-smell label alone.

| Candidate | Review question |
|---|---|
| Modes, flags, output fields, compatibility paths | Who uses this capability? Can we remove it instead of making it more flexible? |
| Wrappers and abstractions | Does this hide meaningful complexity or merely forward calls and rename things? Would deletion eliminate complexity or scatter it across callers? |
| Hand-written utilities | Does the standard library or an existing dependency already provide the operation, parsing, or source metadata? |
| Repeated validation and bookkeeping | Can one authoritative parse or calculation serve all consumers? |
| Types and schemas | Can validated internal states make later checks unnecessary? Untrusted input still needs runtime validation. |
| New libraries or language changes | After adapters, custom errors, configuration, CI, and migration, does total maintenance shrink? Replace a mechanism rather than layering another beneath it. |
| Module boundaries | Does the split isolate a responsibility behind a smaller interface? File length alone does not justify another module. |

### Review tests by the failures they catch

For each test or related group, name a plausible product regression it would detect. Assess assertions as well as test functions.

- Keep domain rules, consequential boundaries, and real external protocols—even when their assertions look obvious.
- Simplify repeated scenarios, elaborate fixtures, and mocks of internal call sequences. Prefer observable behavior through the interface used by callers.
- Remove assertions that freeze harmless implementation details, library behavior, or unused output shape. A simple check of our integration with a library can still be valuable.
- Check that the scenario exercises the claimed failure. A security-sounding test name is not evidence of security coverage.
- Where uncertain, make one plausible temporary mutation: would the test fail if the relevant behavior were wrong? Keep the experiment disposable.

Finish with prioritized, evidence-backed findings. An entire small suite can earn its place; neither test count nor coverage percentage is a deletion target.

## 4. Propose, then change within authorization

For a review request, report the findings without editing. For an authorized simplification, make the smallest coherent change that removes maintenance obligations. Preserve behavior except for requirement changes the owner accepted.

Prefer existing built-ins and dependencies. Keep direct domain logic where no simpler mechanism exists. Split modules only where the resulting interface earns its existence; retain necessary local detail rather than adding generic factories, adapters, or configuration to hide it.

When the user requests an independent review, use the requested model if available. Supply the proposal or changes, relevant requirements, and the simplicity criterion. Report objections and your disposition; treat feedback as evidence, not a checklist of edge cases to implement. State explicitly if the requested reviewer is unavailable.

Finish when each changed behavior is authorized and each new abstraction or dependency has a concrete maintenance benefit.

## 5. Verify and report

Run the relevant existing checks. For behavior-preserving work, compare consequential outputs against the baseline, using representative real data where available. Add or strengthen tests only for plausible regressions introduced or exposed by the change; use disposable checks for one-off investigation.

Report file paths, what maintenance surface disappeared, intentional behavior changes, verification results, and remaining uncertainty. Line counts can describe a diff, but are not evidence of simplification. Stop when the real workflow is protected and the unnecessary obligations are gone—not when another speculative case could be covered.
