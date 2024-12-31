from main import clip_punctuation_start, clip_punctuation_end, process_word


def test_clip_punctuation_start():
    assert clip_punctuation_start("'(Foo...)'") == "Foo...)'"


def test_clip_punctuation_end():
    assert clip_punctuation_end("'(Foo...)'") == "'(Foo"


def test_process_word():
    assert process_word("'(Foo...)'") == "foo"
