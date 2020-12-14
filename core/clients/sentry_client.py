from __future__ import annotations
import logging
from typing import Optional

import sentry_sdk
from sentry_sdk import configure_scope, Hub

from core import env


class SentryClient:
    """Attention: Singleton object, use by SentryClient.get_instance().capture_exception()
    Close class instance by SentryClient.close_instance()"""
    __instance = None
    # Look in Sentry project config
    __dsn_url: str = "your_dsn_url"

    __overload_job_url: Optional[str] = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            logging.debug("Creating SentryClient instance")
            cls.__instance = SentryClient()
        return cls.__instance

    def init_client(self):
        logging.debug(f'Init sentry SDK with {self.__dsn_url=}')
        release_name = env.get_git_branch_name() + '_' + env.get_commit_sha()
        sentry_sdk.init(self.__dsn_url, release=release_name)

    def set_overload_job_url(self, overload_job_url: str) -> SentryClient:
        self.__overload_job_url = overload_job_url
        return self.get_instance()

    def capture_exception(self, exception=None):
        with configure_scope() as scope:
            scope.set_level('info')
            scope.set_user({'email': env.get_gitlab_user_email()})
            scope.set_tag('host_url', env.get_target_host_data().full_url)
            scope.set_tag('git_branch_in_ci', env.get_git_branch_name())
            # Replace '/' to '.' needs for compatibility with Prometheus format
            scope.set_tag('test', env.test_name_with_path())
            scope.set_tag('ci_job_id', env.get_ci_job_id())
            if self.__overload_job_url:
                scope.set_extra('overload_job_url', self.__overload_job_url)

        # Yes, we use concurrency issues
        # https://docs.sentry.io/platforms/python/troubleshooting/#addressing-concurrency-issues
        with Hub(Hub.current):
            self.init_client()
            event_id = sentry_sdk.capture_exception(exception, scope)
        event_sentry_url = f"https://your_sentry_instance_url/?query={event_id}"
        logging.warning(f"--- Sentry captured exception URL is: '{event_sentry_url}' ---")

    @classmethod
    def close_instance(cls):
        """Sentry class instance must be closed in the end of test, because class properties inherited in the same
        pytest gw-runner"""
        if cls.__instance:
            logging.info('Close Sentry class instance')
            cls.__instance = None
