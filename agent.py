class Agent:
    """Main controller for the AI agent."""

    def __init__(self):
        """Initialize the agent."""

        self.current_task = None
        self.current_plan = None
        self.current_result = None
        self.status = "Ready"

    def run(self):
        """Run the complete agent workflow."""

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
        pass

    def understand_task(self):
        """Understand the received task."""
        pass

    def validate_rules(self):
        """Validate the task against the agent's rules."""
        pass

    def create_plan(self):
        """Create a plan to complete the task."""
        pass

    def execute_plan(self):
        """Execute the plan."""
        pass

    def review_result(self):
        """Review the quality of the completed work."""
        pass

    def record_metrics(self):
        """Record metrics about the completed task."""
        pass

    def respond(self):
        """Return the final response."""
        pass
