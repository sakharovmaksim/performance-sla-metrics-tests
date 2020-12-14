import pytest
from _pytest.fixtures import FixtureRequest

from core import env
from core.helpers.test_result_data import TestResultData


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Hack https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
    setattr(item, "rep_" + rep.when, rep)
    # Create attribute request.node.exception for request.node if test failed
    if rep.when == "call" and rep.failed:
        setattr(item, "exception", call.excinfo.value)


@pytest.fixture(autouse=True)
def run_test(request):
    # Test running here
    yield

    test_result_data = TestResultData()

    if __is_test_failed(request):
        if env.is_need_send_metrics():
            send_test_metrics(request, test_result_data)

    test_result_data.log_overload_url()
    test_result_data.delete_test_logs_dir()
    close_clients()


def send_test_metrics(request: FixtureRequest, test_result_data: TestResultData):
    # TODO Go to Sentry Client and configurate it
    pass


def close_clients():
    # TODO Go to Sentry Client and configurate it
    # SentryClient.close_instance()
    pass


def __is_test_failed(request: FixtureRequest) -> bool:
    # For good test exit by CTRL+C check attr 'rep_call' exists in request.node
    return hasattr(request.node, 'rep_call') and request.node.rep_call.failed
