import solution as sol

def test_test01():
    from solution import make_sarcastic
    text = "I'm so happy "
    expected = "I'm so happy \s"
    result = make_sarcastic(text)
    assert expected == result, result

def test_test02():
    from solution import make_sarcastic
    text = "You should do it "
    expected = "You should do it \s"
    result = make_sarcastic(text)
    assert expected == result, result

    text = "Eat This "
    expected = "Eat This \s"
    result = make_sarcastic(text)
    assert expected == result, result

def test_test03():
    from solution import make_sarcastic
    text = "No Whitespace"
    expected = "No Whitespace \s"
    result = make_sarcastic(text)
    assert expected == result, result

    text = "  Whitespace at beginning"
    expected = "  Whitespace at beginning \s"
    result = make_sarcastic(text)
    assert expected == result, result

    text = "Too much trailing whitespace    "
    expected = "Too much trailing whitespace \s"
    result = make_sarcastic(text)
    assert expected == result, result

def test_test04():
    from solution import make_sarcastic
    text = "Life is Great!"
    expected = "Life is Great! \s"
    result = make_sarcastic(make_sarcastic(text))
    assert expected == result, result

    text = "I'm already sarcastic \s"
    expected = "I'm already sarcastic \s"
    result = make_sarcastic(text)
    assert expected == result, result

def test_test05():
    from solution import make_sarcastic
    text = "  Life is Great!   "
    expected = "  Life is Great! \s"
    result = make_sarcastic(make_sarcastic(make_sarcastic(text)))
    assert expected == result, result