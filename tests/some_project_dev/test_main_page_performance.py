from core.asserts import assert_test_result_status
from core.performance_test_runner import run_performance_test
from tests.some_project_dev.some_project_dev_config_helper import get_project_dev_config_file_path


class TestMainPagePerformance:
    def test_main_page_performance(self):
        result_status = run_performance_test(
            config_template_file_path=get_project_dev_config_file_path('config_main_page_ya_dev.yaml'),
            ammo_template_file_path=get_project_dev_config_file_path('ammo_main_page_ya_dev.txt'))

        assert_test_result_status(result_status)
