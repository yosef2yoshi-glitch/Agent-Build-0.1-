class Agent:
    """A simple AI agent."""

    def __init__(self):
        """Initialize the AI agent."""

        self.current_task = None
        self.task_understanding = {}
        self.current_plan = None
        self.current_result = None
        self.validation_result = None
        self.approval_required = False
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
        self.create_plan()
        self.execute_plan()
        self.review_result()
        self.record_metrics()

        return self.respond()

    def receive_task(self):
        """Receive a task for the agent."""

        self.current_task = input("Enter a task: ")

        print(f"\nTask Received: {self.current_task}")

    def understand_task(self):
        """Understand the received task."""

        # Convert the task to lowercase for keyword matching
        task = self.current_task.lower()

        # Default values
        action = "Unknown"
        object_name = "Unknown"
        task_type = "Unknown"
        goal = "Unknown"
        desired_outcome = "Unknown"

        # Identify the action
        if "check" in task:
            action = "Check"
        elif "create" in task:
            action = "Create"
        elif "delete" in task:
            action = "Delete"
        elif "update" in task:
            action = "Update"
        elif "find" in task:
            action = "Find"
        elif "get" in task:
            action = "Get"

        # Identify the object
        if "email" in task:
            object_name = "Email"
        elif "computer" in task:
            object_name = "Computer"
        elif "user" in task:
            object_name = "User"
        elif "file" in task:
            object_name = "File"

        # Identify the task type and goal
        if object_name == "Email":
            task_type = "Information"
            goal = "Review email"
            desired_outcome = "Identify relevant email"

        elif object_name == "Computer":
            task_type = "Information"
            goal = "Gather computer information"
            desired_outcome = "Return computer information"

        elif object_name == "User":
            task_type = "Information"
            goal = "Gather user information"
            desired_outcome = "Return user information"

        elif object_name == "File":
            task_type = "File Management"
            goal = "Locate or manage a file"
            desired_outcome = "Complete the requested file operation"

        # Store the agent's understanding
        self.task_understanding = {
            "task": self.current_task,
            "action": action,
            "object": object_name,
            "task_type": task_type,
            "goal": goal,
            "desired_outcome": desired_outcome
        }

        # Display the agent's understanding
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

        if action in ["Delete"]:
            self.approval_required = True
            self.validation_result = "Approval Required"

            print("Rule R004: Safety check ................ APPROVAL REQUIRED")
            print("Human approval is required before execution.")
            return

        print("Rule R004: Safety check ................ PASS")

        print()
        print(f"Validation Result: {self.validation_result}")
        print(f"Approval Required : {self.approval_required}")

    def create_plan(self):
        """Create a plan for completing the task."""

        self.print_header("Create Plan")

        # Do not create a plan if validation failed
        if self.validation_result != "Valid":
            print("Planning stopped.")
            print(f"Validation Status: {self.validation_result}")
            return

        # Get information from the task understanding
        action = self.task_understanding["action"]
        object_name = self.task_understanding["object"]

        # Start with an empty plan
        self.current_plan = []

        # Create a plan based on the action and object
        if action == "Check" and object_name == "Computer":

            self.current_plan = [
                "Identify the computer information required",
                "Gather the required computer information",
                "Organize the information",
                "Prepare the results for the user"
            ]

        elif action == "Check" and object_name == "Email":

            self.current_plan = [
                "Identify the email information required",
                "Retrieve the relevant email information",
                "Review the information",
                "Prepare the results for the user"
            ]

        elif action == "Find" and object_name == "File":

            self.current_plan = [
                "Identify the file being requested",
                "Search the available file locations",
                "Verify the correct file",
                "Prepare the file information for the user"
            ]

        else:

            self.current_plan = [
                "Determine the requirements of the task",
                "Identify the information or tools required",
                "Prepare the task for execution"
            ]

        # Display the plan
        print("Plan:")

        for number, step in enumerate(self.current_plan, start=1):
            print(f"{number}. {step}")

    def execute_plan(self):
        """Execute the current plan."""

        self.print_header("Execute Plan")

        print("Execution stage is not implemented yet.")

    def review_result(self):
        """Review the result of the completed task."""

        self.print_header("Review Result")

        print("Review stage is not implemented yet.")

    def record_metrics(self):
        """Record metrics about the completed task."""

        self.print_header("Record Metrics")

        print("Metrics stage is not implemented yet.")

    def respond(self):
        """Return the final response."""

        self.print_header("Respond")

        print("Response stage is not implemented yet.")