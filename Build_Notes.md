**DOCUMENT CATEGORY:** AI AGENT DEVELOPMENT

**DOCUMENT ID:** DEV-REF-001

# AI Agent Build 0.1 — Build Notes

*Architecture, Python learning notes, design reasoning, and development checkpoints.*

| Document Information | Details |
|---|---|
| Purpose | Preserve the project's architectural reasoning, technical learning, design decisions, and important development checkpoints. |
| Scope | AI Agent Build 0.1 architecture, Python concepts, workflow design, safety model, and development history. |
| Audience | Project Owner and Development Assistant |
| Owner | Project Owner |
| Version | 1.1 |
| Last Updated | 2026-11-22 |
| Status | Active Working Document |

---

## 1. Project Vision and Direction

### 1.1 Initial Project Direction

The initial planning notes considered starting at **Autonomy Level 2**, with the agent focused on workflow automation.

The early planning emphasized matching the agent's autonomy to the job and avoiding decision authority that the system was not designed to hold.

The initial goal described the agent as a potential **Digital Operations Manager**, with intended assistant roles including:

- Security assistant
- Brand assistant
- Business assistant

The long-term project direction is a **Level 3 Human-in-the-Loop Agent**.

> **Core principle:** The agent prepares. The human decides.

The project owner retains final decision-making authority.

### 1.2 Common Building Mistakes

The initial planning identified several mistakes to avoid:

- Treating a Level 2 agent like a Level 4 agent and giving it decision authority it was not designed for.
- Building workflows that are unclear or incomplete.
- Failing to define a human review rule.

### 1.3 Building Tips

The project planning notes established these guidelines:

- Write the choice-making rules before building.
- Decide which responsibilities belong to the system and which belong to a human.
- Match the agent's autonomy to the job it is expected to perform.

### 1.4 Questions to Answer Before Building

- What workflow will pass through the agent?
- What is the review step, and how often will it happen?
- What is the baseline before the agent launches?
- What will happen when the agent makes its first mistake?

These questions should be answered as the project moves from a simulated workflow toward real operational capabilities.

## 2. AI Agent Fundamentals

### 2.1 What Is an LLM?

LLM stands for **Large Language Model**.

The LLM understands requests, reasons about them, and helps determine what should happen next. It generates instructions or responses, but another program—our Python controller—performs the actual work.

### 2.2 What Is an AI Agent?

An AI agent is a software program that uses an AI model to understand requests, reason about them, use tools to perform actions, evaluate the results, and continue working toward its goal.

The model and the Python controller have different responsibilities. The model can help interpret and prepare; the controller enforces the workflow and controls access to capabilities.

### 2.3 What Is a Workflow?

A workflow is a sequence of steps performed in a specific order to accomplish a goal.

The initial planning notes described a general workflow:

```text
Receive Input
     ↓
Understand
     ↓
Determine Goal
     ↓
Plan
     ↓
Use Tools
     ↓
Evaluate
     ↓
Respond
```

The current Agent Build 0.1 workflow is documented in Section 3.

### 2.4 Data Readiness Checklist

Before connecting the agent to operational data sources, assess readiness:

- [ ] The workflow is fully documented, including all steps and exceptions.
- [ ] All documentation has been checked.
- [ ] All data sources have been checked.
- [ ] Key fields in connected data are at least 90% complete.
- [ ] The knowledge base covers the top questions the agent is expected to handle.

These are readiness checks from the original planning notes. They are not recorded as completed.

## 3. Agent Architecture

### 3.1 Development Checkpoint — 2026-07-22

The July 22, 2026 session focused on understanding the agent's architecture rather than adding new functionality.

The learning objective was to understand **why** the code was structured the way it was before continuing development.

### 3.2 The Agent as a System

The agent is designed as a sequence of stages, with each stage having a defined responsibility.

The July 22, 2026 learning notes described the workflow as:

```text
Startup
   ↓
Receive Task
   ↓
Understand Task
   ↓
Validate Rules
   ↓
Create Plan
   ↓
Execute Plan
   ↓
Review Result
   ↓
Record Metrics
   ↓
Respond
```

This is the project's original high-level workflow description. The individual methods and their implementation may evolve as the architecture develops.

### 3.3 The `Agent` Class and `__init__()`

`__init__()` is the constructor. Python runs it when an `Agent` object is created.

Example:

```python
agent = Agent()
```

When this happens, Python creates a new `Agent` object and initializes its attributes.

The July 2026 notes recorded this example of initial agent state:

```python
self.current_task = None
self.task_understanding = {}
self.current_plan = None
self.current_result = None
self.status = "Ready"
```

These attributes describe information held by that particular agent instance.

> **Note:** This is a learning example from the July 2026 notes. It is not a claim that these lines represent the latest contents of `agent.py`.

### 3.4 Understanding `None`

`None` is Python's special value meaning that no value is currently assigned.

For example:

```python
self.current_task = None
```

At initialization, the agent has no current task.

Later, the attribute may be assigned a task:

```python
self.current_task = "Check Email"
```

The attribute now refers to the assigned task.

### 3.5 Why Use `current_task` Instead of `task`?

The name `current_task` communicates that the value represents the task the agent is currently working on.

It distinguishes the active task from a previous task or a future task.

Good names communicate intent and make code easier to understand.

### 3.6 The `startup()` Method

**Purpose:** Display the AI agent's startup sequence.

The July 2026 notes identified these presentation responsibilities:

- Display the banner.
- Display the status.
- Display the version.

The notes also identified possible future startup responsibilities:

- Load configuration.
- Initialize memory.
- Verify tools.
- Connect APIs.
- Register plugins.

These were listed as possible future responsibilities, not as implemented features.

The name `startup()` was intentionally selected because the method could grow beyond displaying a banner.

### 3.7 Presentation Versus Functionality

The original learning notes distinguished methods that affect the agent's workflow or state from methods that primarily present information.

Examples identified as workflow or state-related methods:

- `receive_task()`
- `understand_task()`
- `create_plan()`
- `execute_plan()`

Examples identified as presentation methods:

- `startup()`
- `print_header()`

Removing `startup()` would remove the startup interface, but would not by itself stop the agent's core workflow from functioning.

### 3.8 The `run()` Method: Orchestrator

`run()` is the orchestrator. Its responsibility is to coordinate the workflow.

It does not perform every task itself. Instead, it calls the individual stages in the intended order.

The workflow recorded in the original notes was:

```text
run()
  ↓
startup()
  ↓
receive_task()
  ↓
understand_task()
  ↓
validate_rules()
  ↓
create_plan()
  ↓
execute_plan()
  ↓
review_result()
  ↓
record_metrics()
  ↓
respond()
```

### 3.9 Architecture Principle

> The orchestrator should know **what** needs to happen. Each individual method should know **how** its own stage happens.

This separation allows individual components to be reviewed or changed without unnecessarily rewriting the overall workflow.

### 3.10 Computer Analogy

The original notes used a computer-system analogy to explain the architecture:

| Computer Concept | AI Agent Concept |
|---|---|
| BIOS / UEFI | `startup()` |
| Operating system | `run()` |
| RAM | Agent state (`self`) |
| Running process | `current_task` |
| Scheduler | Workflow |
| Device drivers | Tools (future) |
| Event log | Metrics (future) |
| Storage | Memory (future) |

This is a conceptual analogy, not a literal equivalence between an operating system and the Python agent.

## 4. Python Learning Notes

### 4.1 Class: Blueprint

A class defines the structure and behavior that objects created from it can have.

Example:

```python
class Agent:
    def __init__(self):
        self.status = "Ready"
        self.current_task = None
```

Here, `Agent` is the class. It defines initial attributes for an agent object.

### 4.2 Instance / Object: One Created Agent

An instance is a particular object created from a class.

```python
agent = Agent()
```

This creates an `Agent` object and stores a reference to it in the variable `agent`.

The instance is not just the data. It is the actual object that holds its own instance attributes and provides access to its methods.

### 4.3 Instance Attribute: Data Belonging to That Object

An instance attribute is information stored on a particular object.

Examples:

```python
self.status = "Ready"
self.current_task = None
self.approval_granted = False
self.current_plan = []
```

In these examples:

- `self` refers to the current instance.
- `status`, `current_task`, `approval_granted`, and `current_plan` are instance attribute names.
- `"Ready"`, `None`, `False`, and `[]` are the values stored in those attributes.

An instance's attributes normally belong to that particular instance. Two `Agent` instances can have different task or status values.

### 4.4 Connecting This to Agent Build 0.1

The original learning notes included this example:

```python
self.current_plan = self._build_plan(action, object_name)
```

Read the statement from right to left:

1. `self._build_plan(action, object_name)` calls a method on the current agent instance.
2. `action` and `object_name` are arguments passed to the method.
3. The method returns a value, assuming its implementation returns one.
4. `self.current_plan =` stores that returned value in the current instance's `current_plan` attribute.

Another example:

```python
self.approval_granted = False
```

This initializes the current agent instance's `approval_granted` attribute to `False`. The approval workflow must update and enforce this state correctly before any protected operation can proceed.

### 4.5 Quick Reference

| Term | Meaning | Project Example |
|---|---|---|
| Class | Blueprint defining object structure and behavior | `class Agent:` |
| Instance / object | A particular object created from a class | `agent = Agent()` |
| Instance attribute | Data belonging to a particular object | `self.current_plan` |
| Attribute value | Data currently stored in an attribute | `False`, `"Ready"`, or `[]` |
| Method | A function defined on a class and called through an object | `self._build_plan(...)` |
| Parameter | A name listed in a method definition | `action` in a method definition |
| Argument | A value or variable passed into a method call | `action` in a method call |

### 4.6 Analogy: Class, Instance, and Attributes

Think of a class as a form template, an instance as one completed form, and instance attributes as the fields and values on that particular form.

More precisely, the instance is the object itself—not merely the data written on it.

## 5. Safety Architecture and Authorization

### 5.1 Development Checkpoint — 2026-10-19

The October 19, 2026 checkpoint recorded the following observations from the code and behavior reviewed at that time.

**Confirmed in that session:**

- A task such as `delete file` was identified as action `Delete` and object `File`.
- Rule R004 marked the task as requiring human approval.
- The approval prompt accepted a yes-or-no decision.
- In the observed test, entering `no` produced `Approval denied.`, `Execution stopped.`, and a final response stating that execution did not occur.
- `execute_plan()` contained a check for `self.approval_required` and `not self.approval_granted`.
- The blocked branch included a `return`, according to the user's inspection.
- The function also returned early when no plan was available.
- The shown plan loop printed plan steps; the displayed code did not itself perform the real-world file deletion.

These statements describe what was observed in that historical review. They should not be treated as verification of the current source code.

### 5.2 October 19 Follow-Up Items

The checkpoint identified these next steps:

1. Inspect all assignments to `self.approval_granted` and confirm it becomes `True` only after explicit approval.
2. Verify that `execute_plan()` independently blocks a protected task when called directly without approval.
3. Test the safeguard with a harmless simulated task. Do not perform an actual file deletion.
4. Test the approval-granted path.
5. Review result reporting. Printing a plan is not the same as carrying out an action, so `Completed` should not imply a real-world operation occurred unless it actually did.

### 5.3 Development Checkpoint — 2026-11-21

**Focus:** Approval state and authorization integrity.

The current approval model reviewed at that checkpoint used a Boolean instance attribute:

```python
self.approval_granted = False
```

A Boolean can tell the agent whether approval is marked as granted, but it does not identify exactly what the human approved.

This creates a potential stale-approval problem. For example, if the same `Agent` instance handles more than one task, approval for an earlier task must not authorize a later task.

### 5.4 Agreed Approval Principle

> **Decision:** One human approval authorizes one specific task and its associated plan. If the task or plan changes, the agent must obtain fresh approval.

Approval must be tied to the work that was actually presented to the human—not merely to a general `True` state.

### 5.5 Proposed Approval Record

The following instance attributes were proposed as a way to record the approved work:

```python
self.approved_task = None
self.approved_action = None
self.approved_object = None
self.approved_plan = None
```

These names represent the task, action, object, and plan that were approved.

> **Status:** Design direction agreed. Do not mark these attributes or their enforcement as implemented until the source code has been updated, reviewed, and tested.

### 5.6 Validation State Must Be Reset

When a new task is processed, previous approval information must be invalidated.

The November 21 review identified that `validate_rules()` reset:

```python
self.validation_result = "Valid"
self.approval_required = False
```

It did not reset `self.approval_granted` in the source reviewed at that time.

The intended safeguard is to prevent approval from one task carrying over to another task. The approved-task record must also be cleared when a new task begins validation.

### 5.7 Approval Is Not the Same as Approval Not Being Required

The reviewed `request_approval()` method set `self.approval_granted = True` when approval was not required.

That behavior conflates two different states:

- Approval is not required for this task.
- A human explicitly approved this task.

The implementation should represent these states clearly. A task that does not require human approval may be allowed to proceed under policy, but that should not be recorded as though a human explicitly approved it.

### 5.8 Execution Must Verify the Approved Work

Before execution, the agent should verify that the current task details and current plan still match the approved task details and plan.

If the task or plan has changed since approval, execution must stop and fresh approval must be requested.

A plan snapshot or other reliable comparison method may be needed. The exact implementation method remains to be reviewed and agreed before code changes.

### 5.9 November 21 Review Status

The checkpoint recorded:

- The existing approval and execution logic had been reviewed.
- A stale-approval risk was identified.
- The one-approval-per-specific-task-and-plan principle was agreed.
- The proposed approval-record attributes were identified.
- No source-code changes were recorded as completed in that checkpoint.
- Real file, system, email, and cloud operations remained out of scope while execution was simulated and safeguards were being strengthened.

### 5.10 Next Steps from the November 21 Checkpoint

1. Continue the code review in `agent.py`, starting with `request_approval()`.
2. Review how approval is requested, recorded, denied, and returned.
3. Review `execute_plan()` and its independent execution guard.
4. Decide how to preserve and compare the exact approved plan.
5. Agree on the implementation before editing code.
6. Add tests for stale approval, changed task details, changed plans, approval denial, and valid approval.
7. Run the full test suite and document the observed results.

> **Safety:** Never treat an old approval, a changed plan, an unclear response, or an approval-not-required state as permission to execute a different action.

## 6. Architecture Takeaways and Continuing Principles

The original learning notes established these architecture takeaways:

- Build the architecture before adding complexity.
- Every method should have one responsibility.
- Every property represents part of the agent's current state.
- The agent should be modular and easy to expand.
- Good naming makes code easier to understand.
- Think like a software architect, not just a programmer.

> The orchestrator should know what needs to happen, not how each step works.

The safety and development principles established through later reviews add the following requirements:

- Keep task understanding separate from authorization.
- Keep authorization separate from planning and execution.
- A human approval applies only to the specific task and plan reviewed.
- A changed task or plan requires fresh approval.
- Do not confuse an action that does not require approval with an action that received explicit human approval.
- Keep execution simulated and harmless while safeguards are being developed.
- Verify results before reporting that an operation completed.
- Inspect current source code before proposing or making code changes.
- Explain proposed changes and obtain approval before implementation.

## 7. Current Project Checkpoint

**Last documented checkpoint:** 2026-11-21

**Current focus:** Review and strengthen task-specific, plan-specific human approval before making further execution changes.

**Next development action:** Inspect the latest `agent.py`, beginning with `request_approval()`, then review `execute_plan()` and the approval-state lifecycle.

**Implementation status:** The task-and-plan-bound approval record is a proposed design direction. The November 21 checkpoint did not record those changes as implemented.

**Execution limitation:** The reviewed workflow was simulated. Printing plan steps is not equivalent to performing real-world actions.

**Documentation note:** This Build Notes document consolidates the unique material from the supplied source. Repeated copies of the original planning and architecture sections were removed; unique learning explanations, decisions, safety notes, and dated checkpoints were retained.
