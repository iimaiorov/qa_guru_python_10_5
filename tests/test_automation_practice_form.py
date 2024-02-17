from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage


def test_should_final_form_with_high_level_step():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(users.teacher)
    registration_page.should_have_registered(users.teacher)
