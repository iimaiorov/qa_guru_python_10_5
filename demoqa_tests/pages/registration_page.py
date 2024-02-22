from selene import have, command, by, browser
from demoqa_tests.data.users import User
from demoqa_tests.resource import path


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#genterWrapper')
        self.mobile = browser.element('#userNumber')
        self.hobbies = browser.element('#hobbiesWrapper')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.subjects = browser.element('#subjectsInput')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.registered_user_data = browser.element('.table-responsive').all('td:nth-child(2)')

    def open(self):
        browser.open('/')
        browser.element('[aria-label="Consent"]').click()
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).should(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, first_name):
        self.first_name.type(first_name)

    def fill_last_name(self, last_name):
        self.last_name.type(last_name)

    def fill_email(self, email):
        self.email.type(email)

    def select_gender(self, gender):
        self.gender.element(by.text(gender.value)).click()

    def fill_mobile(self, mobile):
        self.mobile.type(mobile)

    def select_hobbies(self, hobbies):
        self.hobbies.element(by.text(hobbies.value)).click()

    def upload_picture(self, file_name):
        self.picture.send_keys(path(file_name))

    def fill_address(self, address):
        self.address.type(address)

    def fill_subjects(self, subjects):
        self.subjects.type(subjects.value).press_enter()

    def select_date_of_birth(self, year, month, day):
        self.date_of_birth.click()
        self.year.type(year)
        self.month.type(month)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def select_state(self, state):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()
        return self

    def select_city(self, city):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()
        return self

    def submit(self):
        self.submit_button.click()

    def should_have_registered(self, user):
        self.registered_user_data.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender.value,
            user.phone,
            f'{user.birth_date} {user.birth_month},{user.birth_year}',
            user.subjects.value,
            user.hobbies.value,
            user.file_name,
            user.address,
            f'{user.state} {user.city}'
        ))

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_mobile(user.phone)
        self.select_hobbies(user.hobbies)
        self.upload_picture(user.file_name)
        self.fill_address(user.address)
        self.fill_subjects(user.subjects)
        self.select_date_of_birth(user.birth_year, user.birth_month, user.birth_date)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit()
        return self
