from typing import Iterable, Any, Optional

__all__ = ["first"]


def first(iterable: Iterable[Any], default: Optional[Any] = None) -> Any:
    """
    Get first of an `Iterable` or default
    :param iterable: any `Iterable`
    :param default: value to return if the iterable is empty. None by default.
    :return: first of an `Iterable` or default
    """
    try:
        return next(iter(iterable))
    except StopIteration:
        return default
