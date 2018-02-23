import unittest

from tests.assignments import test_assignment6

suite = unittest.TestLoader().loadTestsFromModule(test_assignment6)
unittest.TextTestRunner(verbosity=2).run(suite)
