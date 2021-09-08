from decorator.function_decorator.wraps import do_something, do_something_else


class TestWraps:

    def test_unwrap(self):
        assert do_something.__name__ == 'wrapper'
        assert do_something.__doc__ == 'Wrapper'

    def test_wrap(self):
        assert do_something_else.__name__ == 'do_something_else'
        assert do_something_else.__doc__ == 'Do something else'
