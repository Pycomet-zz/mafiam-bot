from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

from datetime import date


@dataclass
class User:
    "User Class Repr"
    id: int = 0
    language: str = "en"


@dataclass_json(letter_case=LetterCase.CAMEL)  ## To camel case in Json for exports
@dataclass
class Account:
    "Account Model For Registering Users"
    nickname: str
    user_id: int
    sex: str = ""
    lang: str = "en"
    secret_question: str = ""
    secret_answer: str = ""
    code: str = ""


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Referral:
    "Referral Model To Database"
    user_id: int
    ref_code: str
    ref_user_id: int
    status: str = "A"
