import unittest

from tests.assignments.assignment7 import test_assign7

suite = unittest.TestLoader().loadTestsFromModule(test_assign7)
unittest.TextTestRunner(verbosity=2).run(suite)
