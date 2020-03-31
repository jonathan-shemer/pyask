import pyask


def test_iterable():
    sentinel = object()
    assert pyask.first([]) is None
    assert pyask.first([], sentinel) == sentinel
    assert pyask.first(range(10)) == 0
    assert pyask.first(['a', 'b']) == 'a'
