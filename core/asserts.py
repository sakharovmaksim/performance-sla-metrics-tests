import logging
import unittest

from core import env


def assert_equal(expected, actual, comment_message: str = "Expected and actual do not equals"):
    logging.info(f"Asserting that expected '{str(expected)}' is equals with actual '{str(actual)}'")
    unittest.TestCase().assertEqual(first=expected, second=actual, msg=comment_message)


def assert_not_equal(expected, actual, comment_message: str = "Expected and actual are equals and it is bad"):
    logging.info(f"Asserting that expected '{str(expected)}' is not equals with actual '{str(actual)}'")
    unittest.TestCase().assertNotEqual(first=expected, second=actual, msg=comment_message)


# Project asserts

def assert_test_result_status(result_status: int):
    logging.info(f"Asserting that test {result_status=} equals 0")
    assert_equal(0, result_status, f"Performance test {env.test_name_with_path()} failed, "
                                   f"test's {result_status=} is not 0")
