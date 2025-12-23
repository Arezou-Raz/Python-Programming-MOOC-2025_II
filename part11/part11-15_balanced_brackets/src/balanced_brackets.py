def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    pairs = {"(": ")", "[": "]"}
    string = ''.join(c for c in my_string if c in pairs or c in pairs.values())
    if string[0] in pairs and string[-1] == pairs[string[0]]:
        return balanced_brackets(string[1:-1])

    return False

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)
