import unittest

from tests.assignments.test_assign5 import test_assign5

suite = unittest.TestLoader().loadTestsFromModule(test_assign5)
unittest.TextTestRunner(verbosity=2).run(suite)
