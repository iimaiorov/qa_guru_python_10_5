import allure
from allure_commons.types import Severity

from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "ymayorov")
@allure.feature("Registration form")
@allure.story("Fill registration form")
@allure.link("https://demoqa.com", name="DemoQA")
def test_should_final_form_with_high_level_step():
    registration_page = RegistrationPage()
    with allure.step("Open registration page"):
        registration_page.open()

    with allure.step("Fill registration form"):
        registration_page.register(users.teacher)

    with allure.step("Check registration data"):
        registration_page.should_have_registered(users.teacher)
