import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """dataclass student"""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """def post init = launched afted __init__"""
        self.login = self.name[0] + self.surname
