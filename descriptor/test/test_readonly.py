import pytest

from descriptor.readonly import HelloMan


def test_readonly_descriptor():
    helloman = HelloMan()

    assert vars(helloman) == {}

    assert helloman.greeting_speech == 'hello'
    assert helloman.changing_greetings == 'hello'

    with pytest.raises(AttributeError):
        helloman.greeting_speech = 'goodbye'

    helloman.changing_greetings = 'goodbye'
    assert helloman.changing_greetings == 'goodbye'
    assert vars(helloman) == {'changing_greetings': 'goodbye'}
