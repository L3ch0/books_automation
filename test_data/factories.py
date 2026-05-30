"""Shared data factories used across the test suite."""
import random
import string
import uuid
from dataclasses import dataclass


@dataclass
class UserRecord:
    first_name: str
    last_name: str
    email: str
    age: str
    salary: str
    department: str


@dataclass
class FormData:
    first_name: str
    last_name: str
    email: str
    mobile: str
    gender: str
    dob: str  # MM/DD/YYYY
    subject: str
    hobby: str
    address: str
    state: str
    city: str


def make_user_record(**overrides) -> UserRecord:
    uid = uuid.uuid4().hex[:6]
    defaults = {
        "first_name": f"Test{uid}",
        "last_name": "Auto",
        "email": f"test{uid}@qa.local",
        "age": str(random.randint(20, 60)),
        "salary": str(random.randint(30000, 150000)),
        "department": random.choice(["QA", "Dev", "Ops", "HR"]),
    }
    defaults.update(overrides)
    return UserRecord(**defaults)


def make_form_data(**overrides) -> FormData:
    defaults = {
        "first_name": "Jane",
        "last_name": "Tester",
        "email": "jane.tester@example.com",
        "mobile": "9123456789",
        "gender": "Female",
        "dob": "03/22/1995",
        "subject": "Chemistry",
        "hobby": "Reading",
        "address": "99 Automation Blvd",
        "state": "NCR",
        "city": "Delhi",
    }
    defaults.update(overrides)
    return FormData(**defaults)


# Static parametrize datasets

WEB_TABLE_RECORDS = [
    make_user_record(first_name="Alpha", department="QA"),
    make_user_record(first_name="Beta", department="Dev"),
    make_user_record(first_name="Gamma", department="Ops"),
]

LOGIN_CASES = [
    ("valid_placeholder", "ValidPass1!", True),
    ("wrong_user_xyz", "badpassword", False),
    ("", "empty_user", False),
]
