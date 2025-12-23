def begin_with_vowel(words: list) -> list:
    return [word for word in words if word[0] in 'aAeEiIoOuU']

if __name__ == '__main__':
    word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)
