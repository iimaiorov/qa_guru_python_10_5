import dataclasses
from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Subject(Enum):
    MATHS = 'Maths'
    PHYSICS = 'Physics'
    CHEMISTRY = 'Chemistry'
    ENGLISH = 'English'
    HISTORY = 'History'
    COMPUTER_SCIENCE = 'Computer Science'


class Hobby(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'
    DANCING = 'Dancing'
    OTHER = 'Other'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    gender: Gender
    address: str
    city: str
    state: str
    birth_date: str
    birth_month: str
    birth_year: str
    subjects: Subject
    hobbies: Hobby
    file_name: str


teacher = User(first_name='Karina',
               last_name='Mathew',
               email='test23@ya.ru',
               phone='0987654321',
               gender=Gender.FEMALE,
               address='New York, USA',
               city='Delhi', state='NCR',
               birth_date='15',
               birth_month='November',
               birth_year='1980',
               subjects=Subject.COMPUTER_SCIENCE,
               hobbies=Hobby.MUSIC,
               file_name='test.txt')

