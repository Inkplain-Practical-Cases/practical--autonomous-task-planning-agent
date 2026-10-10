# Autonomous Task Planning Agent

Build a dependency-aware internal operations planner that validates goals, decomposes bounded work, schedules ready tasks, persists execution state, requests human approval for privileged actions and terminates deterministically. Six cumulative Python/FastAPI stages use safe offline tool fixtures and failure-injection tests.

An Inkplain practical case: a real project built step by step.

## How this repository works

Every step of the lesson has its own branch, and each one contains all steps up to it:

```bash
git clone https://github.com/Inkplain-Practical-Cases/practical--autonomous-task-planning-agent.git
cd practical--autonomous-task-planning-agent
git branch -r            # list the step branches
git checkout step-01-…   # code after step 1
```

`main` holds the final, complete version.
