class Agent:
    """A simple AI agent with a clear lifecycle for task handling."""

    def __init__(self):
        """Initialize the AI agent."""

        self.current_task = None
        self.task_understanding = {}
        self.current_plan = []
        self.current_result = None
        self.validation_result = None
        self.approval_required = False
        self.approval_granted = False
        self.status = "Ready"

    def startup(self):
        """Display the AI Agent startup banner."""

        print("=" * 60)
        print("                 AI AGENT BUILD 0.1")
        print("=" * 60)
        print("              AI Agent Startup Sequence")
        print("-" * 60)
        print()
        print(f"Status : {self.status}")
        print("Version: 0.1")
        print()

    def print_header(self, title):
        """Print a formatted section header."""

        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)

    def run(self):
        """Run the complete agent workflow."""

        self.startup()
        self.receive_task()
        self.understand_task()
        self.validate_rules()

        if self.validation_result in {"Invalid", "Needs Clarification"}:
            return self.respond()

        self.create_plan()

        if not self.request_approval():
            return self.respond()

        self.execute_plan()
        self.review_result()
        self.record_metrics()
        return self.respond()

    def receive_task(self):
        """Receive a task for the agent."""

        self.current_task = input("Enter a task: ").strip()
        print(f"\nTask Received: {self.current_task}")

    def _detect_action(self, task_text):
        """Identify the likely action from the task text."""

        action_keywords = {
            "Delete": ["delete", "remove"],
            "Create": ["create", "build", "make"],
            "Update": ["update", "edit", "modify"],
            "Check": ["check", "review", "inspect"],
            "Find": ["find", "locate", "search"],
            "Get": ["get", "fetch", "retrieve"],
        }

        for action, keywords in action_keywords.items():
            if any(keyword in task_text for keyword in keywords):
                return action

        return "Unknown"

    def _detect_object(self, task_text):
        """Identify the likely object from the task text."""

        object_keywords = {
            "Email": ["email", "mail"],
            "Computer": ["computer", "system", "device"],
            "User": ["user", "account", "profile"],
            "File": ["file", "folder", "document"],
        }

        for object_name, keywords in object_keywords.items():
            if any(keyword in task_text for keyword in keywords):
                return object_name

        return "Unknown"

    def _build_task_details(self, object_name):
        """Map the object to the task type and outcome."""

        task_details = {
            "task_type": "Unknown",
            "goal": "Unknown",
            "desired_outcome": "Unknown",
        }

        if object_name == "Email":
            task_details = {
                "task_type": "Information",
                "goal": "Review email",
                "desired_outcome": "Identify relevant email",
            }
        elif object_name == "Computer":
            task_details = {
                "task_type": "Information",
                "goal": "Gather computer information",
                "desired_outcome": "Return computer information",
            }
        elif object_name == "User":
            task_details = {
                "task_type": "Information",
                "goal": "Gather user information",
                "desired_outcome": "Return user information",
            }
        elif object_name == "File":
            task_details = {
                "task_type": "File Management",
                "goal": "Locate or manage a file",
                "desired_outcome": "Complete the requested file operation",
            }

        return task_details

    def understand_task(self):
        """Understand the received task."""

        if not self.current_task:
            return

        task_text = self.current_task.lower()
        action = self._detect_action(task_text)
        object_name = self._detect_object(task_text)
        task_details = self._build_task_details(object_name)

        self.task_understanding = {
            "task": self.current_task,
            "action": action,
            "object": object_name,
            **task_details,
        }

        self.print_header("Task Understanding")
        print(f"Task: {self.task_understanding['task']}")
        print(f"Action: {self.task_understanding['action']}")
        print(f"Object: {self.task_understanding['object']}")
        print(f"Task Type: {self.task_understanding['task_type']}")
        print(f"Goal: {self.task_understanding['goal']}")
        print(f"Desired Outcome: {self.task_understanding['desired_outcome']}")

    def validate_rules(self):
        """Validate the task against the agent's rules."""

        self.print_header("Validate Rules")

        # Reset validation state
        self.validation_result = "Valid"
        self.approval_required = False

        # Rule R001: A task must exist
        if not self.current_task:
            self.validation_result = "Invalid"
            print("Rule R001: Task is required.")
            return
        print("Rule R001: Task received ................ PASS")

        # Rule R002: The task must be understood
        if not self.task_understanding:
            self.validation_result = "Invalid"
            print("Rule R002: Task understanding required.")
            return
        print("Rule R002: Task understanding ........... PASS")

        # Rule R003: The task must identify an object
        if self.task_understanding["object"] == "Unknown":
            self.validation_result = "Needs Clarification"
            print("Rule R003: Task object .................. NEEDS CLARIFICATION")
            return
        print("Rule R003: Task object .................. PASS")

        # Rule R004: Potentially destructive actions require approval
        action = self.task_understanding["action"]
        if action == "Delete":
            self.approval_required = True
            self.validation_result = "Approval Required"
            print("Rule R004: Safety check ................ APPROVAL REQUIRED")
            print("Human approval is required before execution.")
            return
        print("Rule R004: Safety check ................ PASS")

        print()
        print(f"Validation Result: {self.validation_result}")
        print(f"Approval Required : {self.approval_required}")

    def _build_plan(self, action, object_name):
        """Build a plan for a recognized action and object."""

        if action == "Check" and object_name == "Computer":
            return [
                "Identify the computer information required",
                "Gather the required computer information",
                "Organize the information",
                "Prepare the results for the user",
            ]

        if action == "Check" and object_name == "Email":
            return [
                "Identify the email information required",
                "Retrieve the relevant email information",
                "Review the information",
                "Prepare the results for the user",
            ]

        if action == "Find" and object_name == "File":
            return [
                "Identify the file being requested",
                "Search the available file locations",
                "Verify the correct file",
                "Prepare the file information for the user",
            ]

        return [
            "Determine the requirements of the task",
            "Identify the information or tools required",
            "Prepare the task for execution",
        ]

    def create_plan(self):
        """Create a plan for completing the task."""

        self.print_header("Create Plan")

        if self.validation_result in {"Invalid", "Needs Clarification"}:
            print("Planning stopped.")
            print(f"Validation Status: {self.validation_result}")
            return self.current_plan

        action = self.task_understanding["action"]
        object_name = self.task_understanding["object"]
        self.current_plan = self._build_plan(action, object_name)

        print("Plan:")
        for number, step in enumerate(self.current_plan, start=1):
            print(f"{number}. {step}")

        return self.current_plan

    def request_approval(self):
        """Request human approval when required."""

        self.print_header("Approval Check")

        if not self.approval_required:
            self.approval_granted = True
            print("Approval not required.")
            print("Execution may continue.")
            return True

        print("This task requires human approval.")
        print(f"Task: {self.current_task}")
        print(f"Action: {self.task_understanding['action']}")
        print(f"Object: {self.task_understanding['object']}")

        approval = input("\nApprove this task? (yes/no): ").strip().lower()

        if approval == "yes":
            self.approval_granted = True
            print("Approval granted.")
            return True

        self.approval_granted = False
        print("Approval denied.")
        print("Execution stopped.")
        return False

    def execute_plan(self):
        """Execute the current plan and store the result."""

        self.print_header("Execute Plan")

        if not self.current_plan:
            print("No plan to execute.")
            self.current_result = {
                "task": self.current_task,
                "status": "No plan available",
            }
            return self.current_result

        print("Executing plan:")
        for step in self.current_plan:
            print(f"- {step}")

        self.current_result = {
            "task": self.current_task,
            "action": self.task_understanding.get("action", "Unknown"),
            "object": self.task_understanding.get("object", "Unknown"),
            "status": "Completed",
            "steps_completed": len(self.current_plan),
        }

        return self.current_result

    def review_result(self):
        """Review the result of the completed task."""

        self.print_header("Review Result")

        if self.current_result is None:
            self.current_result = {
                "task": self.current_task,
                "status": "No result available",
            }

        print("Review complete.")
        print(f"Status: {self.current_result['status']}")
        print(f"Task: {self.current_result['task']}")
        return self.current_result

    def record_metrics(self):
        """Record metrics about the completed task."""

        self.print_header("Record Metrics")

        metrics = {
            "task": self.current_task,
            "plan_steps": len(self.current_plan),
            "approval_required": self.approval_required,
            "validation_status": self.validation_result,
        }

        print("Metrics:")
        for key, value in metrics.items():
            print(f"- {key}: {value}")

        return metrics

    def respond(self):
        """Return the final response."""

        self.print_header("Respond")

        if self.validation_result in {"Invalid", "Needs Clarification"}:
            message = (
                f"Task could not be completed because the request needs more detail. "
                f"Current status: {self.validation_result}"
            )
        elif self.current_result:
            message = (
                f"Task completed: {self.current_task}. "
                f"Status: {self.current_result.get('status', 'Unknown')}. "
                f"Plan steps: {len(self.current_plan)}."
            )
        else:
            message = f"Task completed: {self.current_task}"

        print(message)
        return message