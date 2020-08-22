import unittest

# load all tests in the test directory
loader = unittest.TestLoader()
suite = loader.discover(".")

# verbose output
runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)