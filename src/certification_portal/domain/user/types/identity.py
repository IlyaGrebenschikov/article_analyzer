from typing import TypedDict
from typing_extensions import Required

class UserIdType(TypedDict):
    id: Required[int]


class UserLoginType(TypedDict):
    login: Required[str]


class UserIdentityType(TypedDict):
    id: Required[int]
    login: Required[str]
