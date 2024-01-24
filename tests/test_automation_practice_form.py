from selene import browser, be, have, by
import os

current_dir = os.path.abspath('test.txt')


def test_should_final_form_text():
    browser.open('/')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('test@ya.ru')
    browser.element('#genterWrapper').element(by.text('Male')).click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#hobbiesWrapper').element(by.text('Sports')).click()
    browser.element('#uploadPicture').type(current_dir)
    browser.element('#currentAddress').type('Moscow, Russia')
    browser.element('#subjectsInput').type('English').press_enter()
    # browser.element('#dateOfBirthInput').type('01 May 1990').press_enter()
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
    month_option = month_dropdown.element('//option[@value="4"]')
    month_option.click()
    # Select the day
    day = browser.all('.react-datepicker__day').filtered_by(have.exact_text('1')).first()
    day.click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('td:nth-child(2)').should(have.texts(
        'Ivan Ivanov',
        'test@ya.ru',
        'Male',
        '1234567890',
        '01 May,1990',
        'English',
        'Sports',
        'test.txt',
        'Moscow, Russia',
        'NCR Delhi'
    ))
    browser.element('#closeLargeModal').click()

