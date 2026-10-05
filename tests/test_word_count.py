from doc_probe import word_count


def test_mission_example():
    assert word_count("Hello,  world!\n") == 2


def test_empty_and_whitespace_only_text_has_no_words():
    assert word_count("") == 0
    assert word_count(" \n\t ") == 0
