from typing import TypedDict
from typing_extensions import Required

class UserCreationType(TypedDict):
    login: Required[str]
    password: Required[str]
