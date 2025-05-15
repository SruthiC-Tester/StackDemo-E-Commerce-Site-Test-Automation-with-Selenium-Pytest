import pytest

def pytest_configure(config):
    config.option.log_cli = True
    config.option.log_file = 'browserstack.log'
    config.option.log_file_level = 'INFO'

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == 'call' and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            screenshot_name = f"{item.name}_failed.png"
            capture_screenshot(driver, screenshot_name)
            report.extras = getattr(report, "extras", [])
            report.extras.append(extras.image(screenshot_name))


def capture_screenshot(driver, name):
    print(f"Taking screenshot: {name}")
    try:
        driver.get_screenshot_as_file(name)
        print(f"Screenshot saved: {name}")
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")