from selene import browser, have, by

from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage


def test_should_final_form_text():
    browser.open('/')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('test@ya.ru')
    browser.element('#genterWrapper').element(by.text('Male')).click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#hobbiesWrapper').element(by.text('Sports')).click()
    browser.element('#uploadPicture').type('test.txt')
    browser.element('#currentAddress').type('Moscow, Russia')
    browser.element('#subjectsInput').type('English').press_enter()
    date_picker = browser.element('#dateOfBirthInput')
    date_picker.click()
    year_dropdown = browser.element(".react-datepicker__year-select")
    year_dropdown.click()
    year_option = year_dropdown.element('//option[@value="1990"]')
    year_option.click()
    month_dropdown = browser.element('.react-datepicker__month-select')
    month_dropdown.click()
    month_option = month_dropdown.element('//option[@value="4"]')
    month_option.click()
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


def test_should_final_form_with_page_object():
    student = User(first_name='Ivan',
                   last_name='Ivanov',
                   email='test@ya.ru',
                   phone='1234567890',
                   gender='Male',
                   address='Moscow, Russia',
                   city='Delhi', state='NCR',
                   birth_date='01',
                   birth_month='May',
                   birth_year='1990',
                   subjects='English',
                   hobbies='Sports',
                   picture='test.txt')
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.fill_email(student.email)
    registration_page.select_gender(student.gender)
    registration_page.fill_mobile(student.phone)
    registration_page.select_hobbies(student.hobbies)
    registration_page.upload_picture(student.picture)
    registration_page.fill_address(student.address)
    registration_page.fill_subjects(student.subjects)
    registration_page.select_date_of_birth(student.birth_year, student.birth_month, student.birth_date)
    registration_page.select_state(student.state)
    registration_page.select_city(student.city)
    registration_page.submit()
    registration_page.should_have_registered(student)
