class Prefix:
    def __init__(self, string):
        self.string = string

    def __getitem__(self, v):
        return self.string[-v:]

    def __len__(self):
        return len(self.string)


class Sufix:
    def __init__(self, string):
        self.string = string

    def __getitem__(self, v):
        return self.string[:v]

    def __len__(self):
        return len(self.string)


def search_text(text, prefix):
    size = len(text) - 1
    i = 0
    matchs = []
    while i <= len(prefix):
        string = prefix[i]
        if string in text:
            matchs.append((len(string), string))
        i += 1
    return max(matchs)


def calculateScore(text, prefixString, suffixString):
    text_score_prefix = search_text(text, Prefix(prefixString))
    text_score_sufix = search_text(text, Sufix(suffixString))
    max_test_score_string = text_score_prefix[1] + text_score_sufix[1]
    if len(max_test_score_string) == len(text) and max_test_score_string != text:
         return min([text_score_prefix[1], text_score_sufix[1]])
    return max_test_score_string


def test_case0():
    text = "engine"
    prefixString = "raven"
    suffixString = "ginko"
    result = calculateScore(text, prefixString, suffixString)
    assert result == "engin"


def test_case1():
    text = "nothing"
    prefixString = "bruno"
    suffixString = "ingenious"
    result = calculateScore(text, prefixString, suffixString)
    result == "noing"


def test_case2():
    text = "ab"
    prefixString = "b"
    suffixString = "a"
    result = calculateScore(text, prefixString, suffixString)
    assert result == "a"


def test_case3():
    text = "ababaababa"
    prefixString = "babab"
    suffixString = "aabb"
    result = calculateScore(text, prefixString, suffixString)
    assert result == "ababaab"


def test_case4():
    text = "hello"
    prefixString = "hell"
    suffixString = "on"
    result = calculateScore(text, prefixString, suffixString)
    assert result == "hello"


def get_name_fn(fn):
    def view(*args):
        fn(*args)
        return fn.__name__
    return view()


if __name__ == '__main__':
    test_cases = [test_case0, test_case1, test_case2, test_case3, test_case4]

    for test_case in test_cases:
        print(get_name_fn(test_case), "OK")
