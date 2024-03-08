from mockito import mock, verify
import unittest

from group6 import group6

class AssignmentTest(unittest.TestCase):
    def test_should_issue_Assignment_pending_message(self):
        out = mock()

        group6(out)

        verify(out).write("Assignment Pending\n")
