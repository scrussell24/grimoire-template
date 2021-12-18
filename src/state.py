from dataclasses import dataclass
from typing import Tuple


@dataclass
class State:
    foo: str = "foo"
    bar: str = "bar"