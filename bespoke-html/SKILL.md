---
name: bespoke-html
description: Build bespoke local HTML tools when the user requests one or when visual evidence, substantial option comparisons, or batch corrections make chat cumbersome. Use proactively when a workspace materially reduces review effort or errors; keep straightforward questions in chat.
---

# Bespoke HTML

Make a small, throwaway tool for a specific review task, not a replacement for ordinary conversation. Honor explicit text-only requests and keep native permission prompts where the harness requires them.

## 1. Choose the medium and shape the interaction

Resolve what you can from the available material first. Unless the user explicitly requested a tool, use chat when a short question and answer suffice. Choose HTML when inspecting evidence beside editable fields, keeping substantial alternatives visible, or reviewing a batch makes the task materially easier or less error-prone. Include the effort of opening the page and returning answers in that judgment. Judge by the task, not the question count: one detailed image may justify a page; several simple clarifications may not.

When chat suffices, ask there and stop this workflow. Otherwise, build proactively without making the user request a tool. Identify the user-owned decisions or uncertainties and the evidence needed to answer each.

- **Decisions:** put the question, meaningful options and trade-offs together, with room for rationale or another approach. Label recommendations; leave choices unanswered until the user selects one.
- **Evidence review:** put the specific question above the relevant image, document, comparison, or extracted record, with editable proposed readings nearby. Highlight uncertainty and show enough original context to check it; add zoom for small visual details. Set numeric input steps for the domain (`step="any"` when unconstrained), or use text with `inputmode="decimal"`; browser defaults must not reject valid precision.

Allow unsure, skipped, or alternative answers where appropriate. For batches, make explicit review status visible and preserve edits during navigation.

Finish with every question paired with the context and control needed to answer it.

## 2. Build a throwaway workspace

Default to a temporary directory; an existing gitignored scratch location is also suitable. Keep the tool outside version control and deployed assets. Use a static HTML page with inline CSS/JavaScript, native controls, and inline task data. A short data array can drive repeated cards; no reusable form engine is needed.

Keep evidence local, with only needed assets alongside the page and source identifiers preserved. Use file URLs or a loopback-only static server as needed, rather than serving a whole personal folder. A minimal loopback helper may save answers into the workspace when that makes returning them easier; limit it to review assets and the answer file. Broader hosting or persistence requires agreement, not a new application stack.

Make the layout usable in a narrow window and with a keyboard. If retaining a draft helps, store it locally, say where, and leave the form usable if storage is unavailable.

Finish with every evidence asset reachable from the workspace and nothing published or added to the product.

## 3. Close the answer loop

Use one self-contained answer format suited to the task: Markdown for decisions and rationale, or JSON for structured corrections. Export question/item identifiers, source references when needed, answers, and unanswered/unreviewed status. Partial answers must be exportable too.

Provide copy or download with a visible text fallback, or a clearly identified local answer file when using a save helper. Browser-local drafts are not automatically visible to the agent: tell the user exactly how to return the result. With a save helper, distinguish autosaved drafts from submitted answers and wait for submission or the user's explicit go-ahead; autosaving is not an answer handoff.

Finish when the answers can leave the page without losing their meaning or attaching the entire workspace.

## 4. Verify and hand off

Check rendering, representative evidence, a changed answer, exported values, and restoration if draft saving is present. Keep these checks disposable rather than extending the project's permanent test surface. State any verification limit.

Open the page when the environment allows. Provide its path or local URL, what to review, and answer-return instructions. If browser delivery is unavailable, provide the HTML as an artifact or fall back transparently to chat.

Finish when the user can access the workspace and knows how to return answers.

## 5. Use the answers

Separate explicit answers and corrections from untouched or unresolved items. A prefilled value is a proposal, not a confirmed answer. Apply answers only within the original task's authorization; choices in a form grant no blanket permission to modify files, commit, publish, or deploy.

Finish when each returned item has been handled under that authorization or listed back as open, without substituting the agent's recommendation for the user's answer.
