from selene import browser, be, have
import os

current_dir = os.path.abspath(os.path.dirname('test.txt'))


def test_should_final_form_text():
    browser.open('/')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('test@ya.ru')
    browser.element('#genterWrapper').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#hobbiesWrapper').click()
    browser.element('#uploadPicture').type(current_dir)
    browser.element('#currentAddress').type('Moscow, Russia')
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('#dateOfBirthInput').type(
        '01 May 1990')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form'))
    browser.element('#closeLargeModal').click()
