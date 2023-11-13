from typing import Any


def __assert_wrapper(value: Any, error_message: str, error_limit: int = 100):
    if not value:
        raise AssertionError(error_message[:error_limit])


def equal(
        actual_result: Any,
        expected_result: Any,
        message: str,
        error_message: str | None = None,
):
    if error_message is None:
        error_message = (
            f"(equal){message}, actual: {actual_result}, expected: {expected_result}"
        )
    __assert_wrapper(actual_result == expected_result, error_message=error_message)


def word_in_text(
        actual_result: Any,
        expected_result: Any,
        message: str,
        error_message: str | None = None,
):
    if error_message is None:
        error_message = (
            f"(equal){message}, actual: {actual_result}, expected: {expected_result}"
        )
    __assert_wrapper(expected_result in actual_result, error_message=error_message)
