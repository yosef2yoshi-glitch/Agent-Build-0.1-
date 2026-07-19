# AI Agent Build Documentation 

## What Do You Want To Build

what is the right level of Autonomy for your agent? 
* Level 2
* I think I should start at level 2, this level will have the agent dialed in on workflow automation.

## Common Mistakes 

* Treating a level 2 agent like it is level 4 agent giving the agent decision authority it was not design for.
* Unclear workflow design. 
* No human review rule.

## Building Tips

* Write the choice making rules before you start building 
* Choose what the system handles and what a human handles 

## Build Questions You Need to Ask Before Building?

* What workflow will flow theough this agent? 
* What is the review step? & how often will it happen? 
* What is the baseline before the agent launches?
* What will you do when the agent makes it's first mistake? 

## Goal

* Match the agent to the job
* Digtal Operations Manager
* I want this AI Agent to to be a security assisant, brand assistant, Buisness assistant 

## What is a LLM? 

* An LLM stands for Large Language Model 
* The LLM understands requests, reasons about them, and decides what should happen next. It generates instructions or responses, but another program (our Python controller) performs the actual work.

## What is a AI Agent? 

* An AI agent is a software program that uses an AI model to understand requests, reason about them, use tools to perform actions, evaluate the results, and continue working until it achieves its goal.

## What is a WorkFlow? 

* A Workflow is a sequence of steps that are performed in specific steps in order to accomplish a goal.

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

# Data Readiness Check list

[] The workflow is fully documented with all steps,and exceptions written down. 

[] All documentation has been checked.

[] All data sources has been checked.

[] Key fields in connected data are at least 90% finished.

[] The knowledge base covers the top questions the agent will face.

[] 