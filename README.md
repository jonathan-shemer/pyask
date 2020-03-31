# Ask

A set of pure utility methods for python. 

## dataclass
```python
def optional_fields(dataclass) -> Tuple[Field, ...]:
    """
    Lists all `Optional` fields in a dataclass instance or class
    :param dataclass: dataclass instance or class
    :return: tuple of all `Optional` fields of the given dataclass
    """
```

## iterable
```python
def first(iterable: Iterable[Any], default: Optional[Any] = None) -> Any:
    """
    Get first of an `Iterable` or default
    :param iterable: any `Iterable`
    :param default: value to return if the iterable is empty. None by default.
    :return: first of an `Iterable` or default
    """
```