"""
We can now write a test module like this:

# content of test_module.py
import pytest


def test_func_fast():
    pass


@pytest.mark.slow
def test_func_slow():
    pass
"""
import pytest


def pytest_addoption(parser):
    """from https://docs.pytest.org/en/latest/example/simple.html"""
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    """from https://docs.pytest.org/en/latest/example/simple.html"""
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    """from https://docs.pytest.org/en/latest/example/simple.html"""
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


def pytest_report_header():
    """just a header"""
    return "\n\n These tests were made by Igor Khotianovich \n " \
           "NRNU MEPhI, 2020"" \n\n"
