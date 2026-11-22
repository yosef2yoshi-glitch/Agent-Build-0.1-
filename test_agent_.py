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
        self.assertIsNone(self.agent.approved_task)
        self.assertIsNone(self.agent.approved_plan)
        self.assertEqual(self.agent.current_result["status"], "Denied")
        self.assertFalse(self.agent.current_result["executed"])

    def test_approved_task_and_plan_are_recorded(self):
        """A yes response records the exact task details and plan."""
        with patch("builtins.input", return_value="yes"):
            approved = self.agent.request_approval()

        self.assertTrue(approved)
        self.assertTrue(self.agent.approval_granted)
        self.assertEqual(self.agent.approved_task, "delete file")
        self.assertEqual(self.agent.approved_action, "Delete")
        self.assertEqual(self.agent.approved_object, "File")
        self.assertEqual(self.agent.approved_plan, ("Simulated deletion",))

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
        self.assertTrue(
            any("Execution blocked:" in message for message in printed_messages)
        )

    def test_execution_is_blocked_if_task_changes_after_approval(self):
        """Approval for one task cannot authorize a different task."""
        with patch("builtins.input", return_value="yes"):
            self.agent.request_approval()

        self.agent.current_task = "delete another file"

        with patch("builtins.print"):
            result = self.agent.execute_plan()

        self.assertEqual(result["status"], "Blocked")
        self.assertFalse(result["executed"])

    def test_execution_is_blocked_if_plan_changes_after_approval(self):
        """Changing even one plan step requires fresh approval."""
        with patch("builtins.input", return_value="yes"):
            self.agent.request_approval()

        self.agent.current_plan = ["Simulated deletion", "Delete another file"]

        with patch("builtins.print"):
            result = self.agent.execute_plan()

        self.assertEqual(result["status"], "Blocked")
        self.assertFalse(result["executed"])

    def test_new_validation_clears_previous_approval(self):
        """Validating a new task invalidates the previous approval."""
        with patch("builtins.input", return_value="yes"):
            self.agent.request_approval()

        self.agent.current_task = "delete a different file"
        self.agent.task_understanding = {
            "task": self.agent.current_task,
            "action": "Delete",
            "object": "File",
        }

        with patch("builtins.print"):
            self.agent.validate_rules()

        self.assertFalse(self.agent.approval_granted)
        self.assertIsNone(self.agent.approved_task)
        self.assertIsNone(self.agent.approved_action)
        self.assertIsNone(self.agent.approved_object)
        self.assertIsNone(self.agent.approved_plan)

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
        """A task without an approval requirement can proceed without approval."""
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

    def test_no_approval_required_does_not_claim_human_approval(self):
        """Skipping approval must not set approval_granted to True."""
        self.agent.approval_required = False

        with patch("builtins.print"):
            approved = self.agent.request_approval()

        self.assertTrue(approved)
        self.assertFalse(self.agent.approval_granted)


if __name__ == "__main__":
    unittest.main()
