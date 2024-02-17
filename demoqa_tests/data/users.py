import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    gender: str
    address: str
    city: str
    state: str
    birth_date: str
    birth_month: str
    birth_year: str
    subjects: str
    hobbies: str
    file_name: str


teacher = User(first_name='Karina',
               last_name='Mathew',
               email='test23@ya.ru',
               phone='0987654321',
               gender='Female',
               address='New York, USA',
               city='Delhi', state='NCR',
               birth_date='15',
               birth_month='November',
               birth_year='1980',
               subjects='Hindi',
               hobbies='Music',
               file_name='test.txt')
