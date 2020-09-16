import pytest
from _pytest.fixtures import FixtureRequest

from core import env
from core.helpers.overload_service_helper import OverloadServiceHelper


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

    overload_service = OverloadServiceHelper()

    if __is_test_failed(request):
        if env.is_need_send_metrics():
            send_test_metrics(request, overload_service)

    overload_service.log_overload_job_url()
    close_clients()


def send_test_metrics(request: FixtureRequest, overload_service: OverloadServiceHelper):
    pass
    # TODO Go to Sentry Client and configurate it

    # sentry_instance = SentryClient.get_instance()
    # overload_job_url = overload_service.get_overload_job_url()
    # if overload_job_url:
    #     sentry_instance.set_overload_job_url(overload_job_url)
    # sentry_instance.capture_exception(request.node.exception)


def close_clients():
    pass
    # TODO Go to Sentry Client and configurate it
    # SentryClient.close_instance()


def __is_test_failed(request: FixtureRequest) -> bool:
    # For good test exit by CTRL+C check attr 'rep_call' exists in request.node
    return hasattr(request.node, 'rep_call') and request.node.rep_call.failed
