import nov17lab

def test_read_phrases():
    phrases = nov17lab.read_phrases()
    for phrase in phrases:
        assert "\n" not in phrase

def test_freq_sort():
    strs = ["ad", "abs", "sort", "sort", "abs", "abs"]
    expect = ["abs", "sort", "ad"]
    assert nov17lab.freq_sort(strs) == expect

def test_sort_by_words():
    strs = ["ask about agreements", "aSk", "AsK AgreeMenTS", "ABOut AsK", "    abOuT"]
    expect = ["ask", "about", "agreements"]
    assert nov17lab.sort_by_words(strs) == expect

def test_sort_by_phrases():
    strs = ["ask about agreements","AsK   abouT    AgreeMenTS", "AsK about    "]
    expect = ["ask about agreements", "ask about"]
    assert nov17lab.sort_by_phrases(strs) == expect

def main():
    test_read_phrases()
    test_freq_sort()
    test_sort_by_words()
    test_sort_by_phrases()
    print("all tests passed")

if __name__=="__main__":
    main()