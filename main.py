import unittest


# Function runs all tests
def run_all_tests():
    try:
        # Create a TestLoader instance
        loader = unittest.TestLoader()
        # Find tests that contain 'test_*.py' in folder tests
        tests = loader.discover(start_dir='tests', pattern='test_*.py')
        # Create a TextTestRunner instance with verbosity
        testRunner = unittest.TextTestRunner(verbosity=2)
        # Run the tests and capture the result
        result = testRunner.run(tests)
    # Catch exception when error occurred while tests running
    except Exception as e:
        print(f"An error occurred while running tests: {e}")


# Call the function to run all tests
run_all_tests()
