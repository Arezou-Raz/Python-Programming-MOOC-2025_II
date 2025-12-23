import string

def remove_punctuation(text: str) -> str:
    return ''.join(char for char in text if char not in string.punctuation)

def most_common_words(filename: str, lower_limit: int) -> dict:
    with open(filename, 'r') as file:
        text = file.read()

    text = remove_punctuation(text)
    words = text.split()

    words_counts = {word : words.count(word) for word in words}

    return {word : count for word, count in words_counts.items() if count >= lower_limit}

if __name__ == '__main__':
    most_common_words("comprehensions.txt", 3)
