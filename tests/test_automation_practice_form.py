from demoqa_tests.pages.registration_page import RegistrationPage


def test_should_final_form_with_page_object():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('test@ya.ru')
    registration_page.select_gender('Male')
    registration_page.fill_mobile('1234567890')
    registration_page.select_hobbies('Sports')
    registration_page.upload_picture('test.txt')
    registration_page.fill_address('Moscow, Russia')
    registration_page.fill_subjects('English')
    registration_page.select_date_of_birth('1990', 'May', '01')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit()
    registration_page.should_have_registered('Ivan',
                                             'Ivanov',
                                            'test@ya.ru',
                                             'Male',
                                             '1234567890',
                                             '01',
                                             'May',
                                             '1990',
                                             'English',
                                             'Sports',
                                             'test.txt',
                                             'Moscow, Russia',
                                             'NCR',
                                             'Delhi'
                                             )
