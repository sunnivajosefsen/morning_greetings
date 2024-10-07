import unittest

# Import all test cases
import tests.test_contacts as test1
import tests.test_contacts_manager as test2
import tests.test_logger as test3
import tests.test_message_generator as test4
import tests.test_message_sender as test5

if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestSuite()
    
    # Add all tests from each module
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test1))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test2))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test3))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test4))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test5))
    
    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
