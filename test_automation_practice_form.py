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
    # Open the date picker
    date_picker = browser.element('#dateOfBirthInput')
    date_picker.click()
    # Select the year
    year_dropdown = browser.element(".react-datepicker__year-select")
    year_dropdown.click()
    year_option = year_dropdown.element('//option[@value="1990"]')
    year_option.click()
    # Select the month
    month_dropdown = browser.element('.react-datepicker__month-select')
    month_dropdown.click()
    month_option = month_dropdown.element('//option[@value="4"]')  # May is the 5th month, but indexing starts at 0
    month_option.click()
    # Select the day
    day = browser.all('.react-datepicker__day').filtered_by(have.exact_text('1')).first()
    day.click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form'))
    browser.element('#closeLargeModal').click()
