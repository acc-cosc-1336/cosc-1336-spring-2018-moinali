import unittest

from src.midterm import test_exam

suite = unittest.TestLoader().loadTestsFromModule(test_exam)
unittest.TextTestRunner(verbosity=2).run(suite)
