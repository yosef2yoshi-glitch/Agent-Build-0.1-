"""Automated safety tests for AI Agent Build 0.1.

Run from the project directory with:
    python3 -m unittest -v test_agent_

These tests use simulated tasks only. They do not perform real file operations.
"""

import unittest
from unittest.mock import patch

from agent import Agent


class TestAgentSafety(unittest.TestCase):
    """Test approval and execution safeguards."""

    def setUp(self):
        """Create a fresh agent for each test."""
        self.agent = Agent()
        self.agent.current_task = "delete file"
        self.agent.task_understanding = {
            "task": "delete file",
            "action": "Delete",
            "object": "File",
            "task_type": "File Management",
            "goal": "Locate or manage a file",
            "desired_outcome": "Complete the requested file operation",
        }
        self.agent.current_plan = ["Simulated deletion"]
        self.agent.approval_required = True
        self.agent.approval_granted = False
        self.agent.validation_result = "Approval Required"

    def test_denied_approval_records_denied_result(self):
        """Answering 'no' records denial and does not execute the plan."""
        with patch("builtins.input", return_value="no"):
            approved = self.agent.request_approval()

        self.assertFalse(approved)
        self.assertFalse(self.agent.approval_granted)
        self.assertEqual(self.agent.current_result["status"], "Denied")
        self.assertFalse(self.agent.current_result["executed"])

    def test_execution_is_blocked_without_required_approval(self):
        """A direct execute_plan call cannot bypass required approval."""
        with patch("builtins.print") as mocked_print:
            result = self.agent.execute_plan()

        self.assertEqual(result["status"], "Blocked")
        self.assertFalse(result["executed"])
        printed_messages = [
            str(call.args[0])
            for call in mocked_print.call_args_list
            if call.args
        ]
        self.assertIn(
            "Execution blocked: required approval was not granted.",
            printed_messages,
        )

    def test_denied_workflow_does_not_execute_plan(self):
        """The normal workflow returns after approval is denied."""
        self.agent.startup = lambda: None
        self.agent.receive_task = lambda: setattr(
            self.agent, "current_task", "delete file"
        )
        self.agent.understand_task = lambda: setattr(
            self.agent,
            "task_understanding",
            {
                "task": "delete file",
                "action": "Delete",
                "object": "File",
                "task_type": "File Management",
                "goal": "Locate or manage a file",
                "desired_outcome": "Complete the requested file operation",
            },
        )

        def fake_validate_rules():
            self.agent.validation_result = "Approval Required"
            self.agent.approval_required = True

        self.agent.validate_rules = fake_validate_rules
        self.agent.create_plan = lambda: setattr(
            self.agent, "current_plan", ["Simulated deletion"]
        )

        def deny_approval():
            self.agent.approval_granted = False
            self.agent.current_result = {
                "task": self.agent.current_task,
                "status": "Denied",
                "executed": False,
                "reason": "Human approval was denied.",
            }
            return False

        self.agent.request_approval = deny_approval

        def fail_if_executed():
            self.fail("execute_plan() should not be called after denial")

        self.agent.execute_plan = fail_if_executed

        with patch("builtins.print"):
            response = self.agent.run()

        self.assertIn("Task denied", response)
        self.assertIn("Execution did not occur", response)

    def test_non_destructive_task_without_required_approval_is_not_blocked(self):
        """The safeguard should not block when approval is not required."""
        self.agent.approval_required = False
        self.agent.approval_granted = False
        self.agent.current_task = "check computer"
        self.agent.task_understanding = {
            "task": "check computer",
            "action": "Check",
            "object": "Computer",
        }
        self.agent.current_plan = ["Simulated computer check"]

        with patch("builtins.print"):
            result = self.agent.execute_plan()

        self.assertEqual(result["status"], "Completed")


if __name__ == "__main__":
    unittest.main()
