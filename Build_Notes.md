# AI Agent Build Documentation 

## What Do You Want To Build

what is the right level of Autonomy for your agent?

* Level 2

* I think I should start at level 2; this level will have the agent dialed in on workflow automation.

### Common Mistakes

* Treating a level 2 agent like it is a level 4 agent, giving the agent decision authority it was not designed for.
* Unclear workflow design.
* No human review rule.

### Building Tips

* Write the choice-making rules before you start building.
* Choose what the system handles and what a human handles.

### Build Questions You Need to Ask Before Building?

* What workflow will flow through this agent?
* What is the review step, and how often will it happen?
* What is the baseline before the agent launches?
* What will you do when the agent makes its first mistake?

### Goal

* Match the agent to the job.
* Digital Operations Manager.
* I want this AI agent to be a security assistant, brand assistant, and business assistant.

### What is a LLM?

* An LLM stands for Large Language Model.
* The LLM understands requests, reasons about them, and decides what should happen next. It generates instructions or responses, but another program (our Python controller) performs the actual work.

### What is an AI Agent?

* An AI agent is a software program that uses an AI model to understand requests, reason about them, use tools to perform actions, evaluate the results, and continue working until it achieves its goal.

### What is a Workflow?

* A workflow is a sequence of steps performed in a specific order to accomplish a goal.

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

### Data Readiness Check list

[] The workflow is fully documented with all steps,and exceptions written down. 

[] All documentation has been checked.

[] All data sources has been checked.

[] Key fields in connected data are at least 90% finished.

[] The knowledge base covers the top questions the agent will face.

## AI Agent Build 0.1 - Build Notes

**Date:** July 22, 2026

---

#### Session Summary

Today I focused on understanding the architecture of the AI Agent rather than adding new functionality.

The goal was to understand *why* the code is structured the way it is before continuing development.

---

### The Agent as a System

Think of the AI Agent as its own operating system.

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

Each stage has a single responsibility.

---

### Understanding `__init__()`

`__init__()` is the constructor.

It automatically runs when an Agent object is created.

Example:

```python
agent = Agent()
```

When this happens, Python creates a new Agent and initializes all of its properties.

Current Agent State:

```python
self.current_task = None
self.task_understanding = {}
self.current_plan = None
self.current_result = None
self.status = "Ready"
```

These properties describe the current state of the agent.

---

### Understanding None

`None` means:

> No value exists yet.

Example:

```python
self.current_task = None
```

The agent currently has no task.

Later:

```python
self.current_task = "Check Email"
```

The property is updated.

---

### Why "current_task" Instead of "task"

`current_task` tells us:

* This is the task the agent is currently working on.
* It is not a previous task.
* It is not a future task.

Good variable names communicate intent.

---

### startup()

Purpose:

Display the AI Agent startup sequence.

Current Responsibilities:

* Display banner
* Display status
* Display version

Future Responsibilities could include:

* Load configuration
* Initialize memory
* Verify tools
* Connect APIs
* Register plugins

The name `startup()` was intentionally chosen because it can grow beyond simply printing a banner.

---

### Presentation vs Functionality

Some methods change the agent.

Examples:

* receive_task()
* understand_task()
* create_plan()
* execute_plan()

Other methods only present information.

Examples:

* startup()
* print_header()

Removing `startup()` would not stop the agent from functioning.

It would only remove the startup interface.

---

### run()

`run()` is the orchestrator.

Its responsibility is to coordinate the workflow.

It does **not** perform the work itself.

Instead it calls each stage in order.

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

---

### Architecture Principle

The orchestrator should know **what** happens.

Each individual method knows **how** it happens.

This allows individual components to be rewritten without changing the overall workflow.

---

### Computer Analogy

| Computer | AI Agent |
| ---------- | --------- |
| BIOS / UEFI | startup() |
| Operating System | run() |
| RAM | Agent State (`self`) |
| Running Process | current_task |
| Scheduler | Workflow |
| Device Drivers | Tools (future) |
| Event Log | Metrics (future) |
| Storage | Memory (future) |

---

### Key Takeaways

* Build the architecture before adding complexity.
* Every method should have one responsibility.
* Every property represents part of the agent's current state.
* The agent should be modular and easy to expand.
* Good naming makes the code easier to understand.
* Think like a software architect, not just a programmer.

> **"The orchestrator should know what needs to happen, not how each step works."**

**AI Agent Build 0.1 --- Build Notes**
**Learning Notes:** Classes, Instances, and Instance Attributes

1. Class = Blueprint
A class defines the structure and behavior that objects created from
it can have.
Example:

```python
class Agent:
    def __init__(self):
        self.status = "Ready"
        self.current_task = None
```

Here, Agent is the class. It defines the initial attributes for an
agent object.
2. Instance (Object) = One Created Agent
An instance is a particular object created from a class.
agent = Agent()
This creates an Agent object and stores a reference to it in the
variable agent.
The instance is not just the data. It is the actual object that holds
its own instance attributes and provides access to its methods.
3. **Instance Attribute** = Data Belonging to That Object
An instance attribute is information stored on a particular object.
self.status = "Ready"
self.current_task = None
self.approval_granted = False
self.current_plan = []
In these examples:

* self refers to the current instance.
* status, current_task, approval_granted, and current_plan are
  instance attribute names.

* "Ready", None, False, and [] are the values stored in those attributes.

An instance's attributes normally belong to that particular instance.
Two Agent instances can have different task or status values.
4. Connecting This to AI Agent Build 0.1
Example from the project:
self.current_plan = self._build_plan(action, object_name)
Read this from right to left:

1. self._build_plan(action, object_name) calls a method on the
   current agent instance.
2. action and object_name are arguments passed to the method.
3. The method returns a value (assuming its implementation returns
   one).
4. self.current_plan = stores that returned value in the current
   instance's current_plan attribute.
Another project example:
self.approval_granted = False
This initializes the current agent instance's approval_granted
attribute to False. The approval workflow must update and enforce this
state correctly before any protected operation can proceed.
Quick Reference
  Term                    Meaning                 Project example
  Class                   Blueprint defining      class Agent:
                          object structure and
                          behavior
  Instance / object       A particular object     agent = Agent()
                          created from a class
  Instance attribute      Data belonging to a     self.current_plan
                          particular object
  Attribute value         The data currently      False, "Ready", or []
                          stored in an attribute  
  Method                  A function defined on a self._build_plan(...)
                          class and called
                          through an object
  Parameter               A name listed in a      def_build_plan(self, action, object_name):
                          method definition
  Argument                A value or variable     action, object_name in the call
                          passed into a method
                      call
Analogy
Think of a class as a form template, an instance as one completed form,
and instance attributes as the fields and values on that particular
form. More precisely, the instance is the object itself---not merely the
data written on it.

### Current Development Checkpoint --- 2026-10-19

#### Confirmed in the current session

* A task such as delete file is identified as action Delete and object File.
* Rule R004 marks the task as requiring human approval.
* The approval prompt accepts a yes or no decision.
* In the observed test, entering no produced Approval denied.,
  Execution stopped., and a final response stating that execution did not occur.

* execute_plan() contains a check for self.approval_required and not self.approval_granted.
* The blocked branch includes a return, according to the user's
  inspection.
* The function also returns early when no plan is available.
* The shown plan loop prints plan steps; the displayed code does not
  itself perform the real-world file deletion.

### Next steps

1. Inspect all assignments to self.approval_granted and confirm it
   becomes True only after an explicit approval.
2. Verify that execute_plan() independently blocks a protected task
   when called directly without approval.
3. Test the safeguard with a harmless simulated task---do not perform
   an actual file deletion.
4. Test the approval-granted path.
5. Review result reporting: printing a plan is not the same as carrying
   out an action, so Completed should not imply a real-world
   operation occurred unless it actually did.
Safety rule
Do not change working code without first inspecting it and explaining
the proposed change. Keep tests harmless and verify the behavior before
moving to the next feature.

**# AI Agent Build Documentation&#x20;**



**## What Do You Want To Build**



what is the right level of Autonomy for your agent?



\* Level 2



\* I think I should start at level 2; this level will have the agent dialed in on workflow automation.



**### Common Mistakes**



\* Treating a level 2 agent like it is a level 4 agent, giving the agent decision authority it was not designed for.

\* Unclear workflow design.

\* No human review rule.



**### Building Tips**



\* Write the choice-making rules before you start building.

\* Choose what the system handles and what a human handles.



**### Build Questions You Need to Ask Before Building?**



\* What workflow will flow through this agent?

\* What is the review step, and how often will it happen?

\* What is the baseline before the agent launches?

\* What will you do when the agent makes its first mistake?



**### Goal**



\* Match the agent to the job.

\* Digital Operations Manager.

\* I want this AI agent to be a security assistant, brand assistant, and business assistant.



**### What is a LLM?**



\* An LLM stands for Large Language Model.

\* The LLM understands requests, reasons about them, and decides what should happen next. It generates instructions or responses, but another program (our Python controller) performs the actual work.



**### What is an AI Agent?**



\* An AI agent is a software program that uses an AI model to understand requests, reason about them, use tools to perform actions, evaluate the results, and continue working until it achieves its goal.



**### What is a Workflow?**



\* A workflow is a sequence of steps performed in a specific order to accomplish a goal.



Receive Input

&#x20;     ↓

Understand

&#x20;     ↓

Determine Goal

&#x20;     ↓

Plan

&#x20;     ↓

Use Tools

&#x20;     ↓

Evaluate

&#x20;     ↓

Respond



**### Data Readiness Check list**



[] The workflow is fully documented with all steps,and exceptions written down.&#x20;



[] All documentation has been checked.



[] All data sources has been checked.



[] Key fields in connected data are at least 90% finished.



[] The knowledge base covers the top questions the agent will face.



**## AI Agent Build 0.1 - Build Notes**



**\*\*Date:\*\*** July 22, 2026



**---**



**#### Session Summary**



Today I focused on understanding the architecture of the AI Agent rather than adding new functionality.



The goal was to understand *\*why\** the code is structured the way it is before continuing development.



**---**



**### The Agent as a System**



Think of the AI Agent as its own operating system.



\`\`\`text

Startup

&#x20;   ↓

Receive Task

&#x20;   ↓

Understand Task

&#x20;   ↓

Validate Rules

&#x20;   ↓

Create Plan

&#x20;   ↓

Execute Plan

&#x20;   ↓

Review Result

&#x20;   ↓

Record Metrics

&#x20;   ↓

Respond

\`\`\`



Each stage has a single responsibility.



**---**



**### Understanding \`\_\_init\_\_()\`**



\`\_\_init\_\_()\` is the constructor.



It automatically runs when an Agent object is created.



Example:



\`\`\`python

agent = Agent()

\`\`\`



When this happens, Python creates a new Agent and initializes all of its properties.



Current Agent State:



\`\`\`python

self.current_task = None

self.task_understanding = {}

self.current_plan = None

self.current_result = None

self.status = "Ready"

\`\`\`



These properties describe the current state of the agent.



**---**



**### Understanding None**



\`None\` means:



\> No value exists yet.



Example:



\`\`\`python

self.current_task = None

\`\`\`



The agent currently has no task.



Later:



\`\`\`python

self.current_task = "Check Email"

\`\`\`



The property is updated.



**---**



**### Why "current_task" Instead of "task"**



\`current_task\` tells us:



\* This is the task the agent is currently working on.

\* It is not a previous task.

\* It is not a future task.



Good variable names communicate intent.



**---**



**### startup()**



Purpose:



Display the AI Agent startup sequence.



Current Responsibilities:



\* Display banner

\* Display status

\* Display version



Future Responsibilities could include:



\* Load configuration

\* Initialize memory

\* Verify tools

\* Connect APIs

\* Register plugins



The name \`startup()\` was intentionally chosen because it can grow beyond simply printing a banner.



**---**



**### Presentation vs Functionality**



Some methods change the agent.



Examples:



\* receive_task()

\* understand_task()

\* create_plan()

\* execute_plan()



Other methods only present information.



Examples:



\* startup()

\* print_header()



Removing \`startup()\` would not stop the agent from functioning.



It would only remove the startup interface.



**---**



**### run()**



\`run()\` is the orchestrator.



Its responsibility is to coordinate the workflow.



It does **\*\*not\*\*** perform the work itself.



Instead it calls each stage in order.



\`\`\`text

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

\`\`\`



**---**



**### Architecture Principle**



The orchestrator should know **\*\*what\*\*** happens.



Each individual method knows **\*\*how\*\*** it happens.



This allows individual components to be rewritten without changing the overall workflow.



**---**



**### Computer Analogy**



\| Computer | AI Agent |

\| ---------- | --------- |

\| BIOS / UEFI | startup() |

\| Operating System | run() |

\| RAM | Agent State (\`self\`) |

\| Running Process | current_task |

\| Scheduler | Workflow |

\| Device Drivers | Tools (future) |

\| Event Log | Metrics (future) |

\| Storage | Memory (future) |



**---**



**### Key Takeaways**



\* Build the architecture before adding complexity.

\* Every method should have one responsibility.

\* Every property represents part of the agent's current state.

\* The agent should be modular and easy to expand.

\* Good naming makes the code easier to understand.

\* Think like a software architect, not just a programmer.



\> **\*\*"The orchestrator should know what needs to happen, not how each step works."\*\***



**\*\*AI Agent Build 0.1 --- Build Notes\*\***

**\*\*Learning Notes:\*\*** Classes, Instances, and Instance Attributes



1\. Class = Blueprint

A class defines the structure and behavior that objects created from

it can have.

Example:



\`\`\`python

class Agent:

&#x20;   def \_\_init\_\_(self):

&#x20;       self.status = "Ready"

&#x20;       self.current_task = None

\`\`\`



Here, Agent is the class. It defines the initial attributes for an

agent object.

2\. Instance (Object) = One Created Agent

An instance is a particular object created from a class.

agent = Agent()

This creates an Agent object and stores a reference to it in the

variable agent.

The instance is not just the data. It is the actual object that holds

its own instance attributes and provides access to its methods.

3\. **\*\*Instance Attribute\*\*** = Data Belonging to That Object

An instance attribute is information stored on a particular object.

self.status = "Ready"

self.current_task = None

self.approval_granted = False

self.current_plan = []

In these examples:



\* self refers to the current instance.

\* status, current_task, approval_granted, and current_plan are

&#x20; instance attribute names.



\* "Ready", None, False, and [] are the values stored in those attributes.



An instance's attributes normally belong to that particular instance.

Two Agent instances can have different task or status values.

4\. Connecting This to AI Agent Build 0.1

Example from the project:

self.current_plan = self.\_build_plan(action, object_name)

Read this from right to left:



1\. self.\_build_plan(action, object_name) calls a method on the

&#x20;  current agent instance.

2\. action and object_name are arguments passed to the method.

3\. The method returns a value (assuming its implementation returns

&#x20;  one).

4\. self.current_plan = stores that returned value in the current

&#x20;  instance's current_plan attribute.

Another project example:

self.approval_granted = False

This initializes the current agent instance's approval_granted

attribute to False. The approval workflow must update and enforce this

state correctly before any protected operation can proceed.

Quick Reference

&#x20; Term                    Meaning                 Project example

&#x20; Class                   Blueprint defining      class Agent:

&#x20;                         object structure and

&#x20;                         behavior

&#x20; Instance / object       A particular object     agent = Agent()

&#x20;                         created from a class

&#x20; Instance attribute      Data belonging to a     self.current_plan

&#x20;                         particular object

&#x20; Attribute value         The data currently      False, "Ready", or []

&#x20;                         stored in an attribute &#x20;

&#x20; Method                  A function defined on a self.\_build_plan(...)

&#x20;                         class and called

&#x20;                         through an object

&#x20; Parameter               A name listed in a      def_build_plan(self, action, object_name):

&#x20;                         method definition

&#x20; Argument                A value or variable     action, object_name in the call

&#x20;                         passed into a method

&#x20;                     call

Analogy

Think of a class as a form template, an instance as one completed form,

and instance attributes as the fields and values on that particular

form. More precisely, the instance is the object itself---not merely the

data written on it.



**### Current Development Checkpoint --- 2026-10-19**



**#### Confirmed in the current session**



\* A task such as delete file is identified as action Delete and object File.

\* Rule R004 marks the task as requiring human approval.

\* The approval prompt accepts a yes or no decision.

\* In the observed test, entering no produced Approval denied.,

&#x20; Execution stopped., and a final response stating that execution did not occur.



\* execute_plan() contains a check for self.approval_required and not self.approval_granted.

\* The blocked branch includes a return, according to the user's

&#x20; inspection.

\* The function also returns early when no plan is available.

\* The shown plan loop prints plan steps; the displayed code does not

&#x20; itself perform the real-world file deletion.



**### Next steps**



1\. Inspect all assignments to self.approval_granted and confirm it

&#x20;  becomes True only after an explicit approval.

2\. Verify that execute_plan() independently blocks a protected task

&#x20;  when called directly without approval.

3\. Test the safeguard with a harmless simulated task---do not perform

&#x20;  an actual file deletion.

4\. Test the approval-granted path.

5\. Review result reporting: printing a plan is not the same as carrying

&#x20;  out an action, so Completed should not imply a real-world

&#x20;  operation occurred unless it actually did.

Safety rule

Do not change working code without first inspecting it and explaining

the proposed change. Keep tests harmless and verify the behavior before

moving to the next feature.
---

## AI Agent Build 0.1 — Safety Architecture Notes

### Development Checkpoint — 2026-11-21

**Focus:** Approval state and authorization integrity.

### Why This Review Is Necessary

The current approval model uses a Boolean instance attribute:

```python
self.approval_granted = False
```

A Boolean can tell the agent whether approval is marked as granted, but it does not identify exactly what the human approved.

This creates a potential stale-approval problem. For example, if the same Agent instance handles more than one task, approval for an earlier task must not authorize a later task.

### Agreed Approval Principle

> One human approval authorizes one specific task and its associated plan. If the task or plan changes, the agent must obtain fresh approval.

Approval must be tied to the work that was actually presented to the human—not merely to a general `True` state.

### Proposed Approval Record

The following instance attributes were proposed as a way to record the approved work:

```python
self.approved_task = None
self.approved_action = None
self.approved_object = None
self.approved_plan = None
```

These names represent the task, action, object, and plan that were approved.

**Status:** Design direction agreed. Do not mark these attributes or their enforcement as implemented until the source code has been updated, reviewed, and tested.

### Validation State Must Be Reset

When a new task is processed, previous approval information must be invalidated.

The review identified that `validate_rules()` currently resets:

```python
self.validation_result = "Valid"
self.approval_required = False
```

It does not currently reset `self.approval_granted` in the reviewed source.

The intended safeguard is to prevent approval from one task carrying over to another task. The approved-task record must also be cleared when a new task begins validation.

### Approval Is Not the Same as Approval Not Being Required

The reviewed `request_approval()` method currently sets `self.approval_granted = True` when approval is not required.

That behavior conflates two different states:

- Approval is not required for this task.
- A human explicitly approved this task.

The implementation should represent these states clearly. A task that does not require human approval may be allowed to proceed under policy, but that should not be recorded as though a human explicitly approved it.

### Execution Must Verify the Approved Work

Before execution, the agent should verify that the current task details and current plan still match the approved task details and plan.

If the task or plan has changed since approval, execution must stop and fresh approval must be requested.

A plan snapshot or other reliable comparison method may be needed. The exact implementation method remains to be reviewed and agreed before code changes.

### Current Review Status

- The existing approval and execution logic has been reviewed.
- A stale-approval risk was identified.
- The one-approval-per-specific-task-and-plan principle was agreed.
- The proposed approval-record attributes were identified.
- No source-code changes are recorded as completed in this checkpoint.
- Real file, system, email, and cloud operations remain out of scope while execution is simulated and the safeguards are being strengthened.

### Next Steps

1. Continue the code review in `agent.py`, starting with `request_approval()`.
2. Review how approval is requested, recorded, denied, and returned.
3. Review `execute_plan()` and its independent execution guard.
4. Decide how to preserve and compare the exact approved plan.
5. Agree on the implementation before editing code.
6. Add tests for stale approval, changed task details, changed plans, approval denial, and valid approval.
7. Run the full test suite and document the observed results.

**Safety rule:** Never treat an old approval, a changed plan, an unclear response, or an approval-not-required state as permission to execute a different action.
