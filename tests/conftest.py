import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attach
import project


@pytest.fixture(autouse=True)
def settings():
    browser.config.base_url = project.Config().base_url
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user2025:T$oo8663@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
