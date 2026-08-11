---
name: step-by-step-guidance
description: Use when a task needs to be broken into a clear sequence of actions, checkpoints, and verification steps.
---

# Step-by-Step Guidance

## Purpose
Use this skill to turn a broad or ambiguous request into a practical plan that can be executed safely and checked for completion.

## When to Use
- The goal is clear, but the path is not yet defined.
- A task involves multiple phases, dependencies, or decisions.
- You need a structured checklist or implementation plan.
- The work should be completed in a reliable, repeatable way.

## Workflow
1. Clarify the objective.
   - Restate the goal in one sentence.
   - Note any constraints, assumptions, or required outcomes.

2. Identify the scope.
   - Separate the main task from optional or follow-up work.
   - Determine what success looks like.

3. Break the work into ordered steps.
   - Create a sequence from first action to final verification.
   - Keep each step concrete and actionable.

4. Add decision points and dependencies.
   - Highlight where the next step depends on a previous result.
   - Note any branching logic or alternatives.

5. Define completion checks.
   - Add a simple verification step for each major phase.
   - Confirm what evidence shows the work is complete.

6. Present the plan clearly.
   - Use short headings, numbered steps, and a concise checklist.
   - Offer a default next action if the user wants to start immediately.

## Output Format
Provide the result in this structure:
- Goal
- Scope and constraints
- Step-by-step plan
- Decision points or dependencies
- Completion checklist

## Quality Criteria
- The plan is specific enough to execute without guessing.
- Each step is ordered logically.
- The final checklist can be used to confirm completion.
- Ambiguities are surfaced rather than ignored.

## Example Prompt
"Break this request into a clear step-by-step plan with checkpoints and a completion checklist."
