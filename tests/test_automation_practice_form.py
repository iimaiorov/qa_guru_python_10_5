from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage


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
                   file_name='test.txt')
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.fill_email(student.email)
    registration_page.select_gender(student.gender)
    registration_page.fill_mobile(student.phone)
    registration_page.select_hobbies(student.hobbies)
    registration_page.upload_picture(student.file_name)
    registration_page.fill_address(student.address)
    registration_page.fill_subjects(student.subjects)
    registration_page.select_date_of_birth(student.birth_year, student.birth_month, student.birth_date)
    registration_page.select_state(student.state)
    registration_page.select_city(student.city)
    registration_page.submit()
    registration_page.should_have_registered(student)
