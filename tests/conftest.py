import pytest
from selene import browser


@pytest.fixture(autouse=True)
def settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 5
    yield
    browser.quit()
