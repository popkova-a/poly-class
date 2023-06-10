import unittest
import tests.test_poly as test_poly


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(test_poly)
    unittest.TextTestRunner(verbosity=2).run(suite)
