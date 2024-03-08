from mockito import mock, verify
import unittest

from Group6 import Group6

class AssignmentTest(unittest.TestCase):
    def test_should_issue_Assignment_pending_message(self):
        out = mock()

        Group6(out)

        verify(out).write("Assignment Pending\n")
