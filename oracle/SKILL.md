---
name: oracle
description: Submit an implementation plan to GPT 5.2-xhigh for review by a senior engineer persona. The Oracle provides direct, honest critique focused on simplicity and pragmatic excellence. Use when you have a detailed implementation plan and want a second opinion before coding. Triggers on "review my plan", "get Oracle feedback", "consult the Oracle", "plan review", or when you want senior engineer critique on an implementation approach.
---

# Oracle

Submit implementation plans for review by GPT 5.2-xhigh, configured as a senior engineer with god-tier expertise and a philosophy of pragmatic excellence.

The Oracle will not write code or make changes—it only provides feedback as a text review.

## When to Consult the Oracle

- Before implementing a non-trivial feature
- When choosing between multiple approaches
- When you suspect you might be over-engineering
- When you want a sanity check on a design

## Preparing Your Plan

Structure your submission with these sections:

### 1. Context (Required)

Explain the problem or goal. What are you trying to accomplish? What constraints exist? What does success look like?

```markdown
## Context

We need to add real-time notifications to the dashboard. Users should see
updates within 2 seconds of events occurring. Current architecture uses
REST polling every 30 seconds.
```

### 2. Implementation Plan (Required)

Your proposed approach. Be specific—include file changes, data flows, key decisions.

```markdown
## Implementation Plan

1. Add WebSocket server using socket.io
2. Create NotificationService that publishes to Redis pub/sub
3. WebSocket server subscribes to Redis and pushes to connected clients
4. Frontend replaces polling with WebSocket connection
5. Graceful degradation: fall back to polling if WebSocket fails
```

### 3. Questions / Skepticisms (Optional)

Points you're uncertain about. Alternatives you considered. Things that feel wrong but you can't articulate why.

```markdown
## Questions

- Is Redis pub/sub overkill? Could we just broadcast directly from the WebSocket server?
- Should we use Server-Sent Events instead of WebSockets since we only need server->client?
- The graceful degradation feels like it doubles the complexity. Is it worth it?
```

## Invoking the Oracle

Write your plan to a file, then run the oracle script:

```bash
# From a file
scripts/oracle.sh /path/to/plan.md

# From stdin
cat plan.md | scripts/oracle.sh

# Using heredoc
scripts/oracle.sh <<'EOF'
## Context
...

## Implementation Plan
...

## Questions
...
EOF
```

The Oracle writes its review to `/tmp/oracle-review-{timestamp}.md` and prints the path.

## What the Oracle Provides

The review includes:

- **Verdict**: Is the plan sound or does it need work?
- **What Works**: Acknowledgment of solid decisions
- **Critical Issues**: Problems that must be addressed
- **Recommendations**: Concrete alternatives, not vague suggestions
- **Answers to Questions**: Direct responses to your skepticisms
- **The Simplest Thing That Could Work**: Often, a simpler path exists

## The Oracle's Philosophy

The Oracle embodies pragmatic excellence:

- KISS principle: the simplest solution that works
- No gold plating or engineering for engineering's sake
- Backwards compatibility matters less than clean design
- Patterns serve code, not vice versa
- Architectural humility: the best code stays out of the user's way

Expect direct feedback. The Oracle doesn't hedge or sugarcoat.
