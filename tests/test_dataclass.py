from dataclasses import dataclass, fields
from typing import Optional, Tuple, Union

from pyask.dataclass import optional_fields


def test_optional_fields():
    @dataclass
    class A:
        a: Optional[int]
        b: Tuple[int, int]
        c: Union[int, str]

    assert optional_fields(A) == (fields(A)[0],)
    assert optional_fields(A(1, (2, 3), "hello")) == (fields(A)[0],)
