import logging
import os

from core.helpers.target_host_data.target_host_data import TargetHostData


def get_tank_config_templates_dir_name() -> str:
    return 'tank_config_templates'


def get_target_host_data() -> TargetHostData:
    """Return TargetHostData object, witch contains info about URL and something else"""
    full_target_url = os.environ.get("TARGET_HOST_URL", '')
    logging.info(f"Got target host URL from ENV: '{full_target_url}'")
    return TargetHostData(full_target_url)


def get_test_name() -> str:
    """Example: test_catalog_page_performance"""
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    logging.debug(f"Got current test name: '{test_name}'")
    return test_name


def get_test_file_name() -> str:
    """Example: tests/some_project_dev/test_catalog_page_performance.py"""
    test_file_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[0]
    logging.debug(f"Got current test file name: '{test_file_name}'")
    return test_file_name


def test_name_with_path() -> str:
    """Return example: 'some_project_dev.test_masterprice_page_performance.py.test_masterprice_page_performance'"""
    return get_test_file_name().replace('/', '.') + '.' + get_test_name()


def is_need_send_metrics() -> bool:
    return os.environ.get('SEND_METRICS', '') == "True"


# Data from GitLab CI

def get_git_branch_name() -> str:
    """Return Git branch name from Gitlab-CI Runner Environment"""
    var = 'CI_COMMIT_REF_NAME'
    if os.environ.get(var):
        return os.environ.get(var)
    return 'no_ci_branch_name'


def get_commit_sha() -> str:
    var = 'CI_COMMIT_SHA'
    if os.environ.get(var):
        return os.environ.get(var)
    return 'no_commit_sha'


def get_ci_job_id() -> int:
    var = 'CI_JOB_ID'
    if os.environ.get(var):
        return int(os.environ.get(var))
    return 0


def get_gitlab_user_email() -> str:
    var = 'GITLAB_USER_EMAIL'
    if os.environ.get(var):
        return os.environ.get(var)
    return 'unknown_gitlab_user'
