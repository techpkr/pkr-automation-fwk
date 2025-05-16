# conftest.py
from glob import glob
import pytest
from utils.slack_helper import send_slack_message
from utils.testrail_helper import add_result_for_case

#1 Load fixtures from files in ./tests/fixtures/
# pick only .py files
pytest_plugins = [
    fixture_file.replace("/", ".").replace(".py", "")
    for fixture_file in glob(
        "tests/fixtures/[!__]*.py",
        recursive=True
    )
]

#2 Add method pytest_addoption(parser) ->  to add custom parsers + testrail too for pytest.
#3 Hooks pytest_configure(config) ->  to modify Pytest's behavior (eg:- logging, skipping).
#4 Other static imports needed 
#5 slack notification
def pytest_sessionfinish(session, exitstatus):
    # Prepare a simple summary message
    total = session.testscollected
    failed = len(session.testsfailed) if hasattr(session, 'testsfailed') else 0
    passed = total - failed
    message = f"Test session finished: Total={total}, Passed={passed}, Failed={failed}, Exit status={exitstatus}"
    send_slack_message(message)


#6 push results to testrail
# Example: You can map test names to TestRail case IDs here
TESTRAIL_CASES_MAPPING = {
    "test_get_users": 101,
    "test_create_user": 102,
    # Add more mappings for your tests here
}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook runs after each test phase (setup/call/teardown)
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":  # only report the test call phase result
        test_name = item.name
        case_id = TESTRAIL_CASES_MAPPING.get(test_name)
        if case_id:
            if rep.passed:
                status = 1
            elif rep.failed:
                status = 5
            elif rep.skipped:
                status = 3
            else:
                status = 3  # fallback to skipped

            comment = f"Automated test run: {test_name} {rep.outcome}"
            add_result_for_case(case_id, status, comment)
