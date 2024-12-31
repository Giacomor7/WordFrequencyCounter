document = "text.txt"


def clip_punctuation_start(word):
    """
    Remove any punctuation that precedes a word e.g. ("hello") -> hello")
    :param word: str - word that may contain initial punctuation
    :return: str - word with initial punctuation removed
    """
    while len(word) > 0 and not word[0].isalpha():
        word = word[1:]
    return word


def clip_punctuation_end(word):
    """
    Remove any punctuation that succeeds a word e.g. ("hello") -> ("hello
    :param word: str - word that may contain final punctuation
    :return: str - word with final punctuation removed
    """
    while len(word) > 0 and not word[-1].isalpha():
        word = word[:-1]
    return word


def process_word(word):
    """
    Process word by trimming punctuation and converting to lowercase
    :param word: str - word to process
    :return: str - processed word
    """
    return clip_punctuation_end(clip_punctuation_start(word.lower()))


def main():
    word_frequencies = {}
    with open(document, 'r') as file:
        for line in file:
            for word in line.split():
                processed_word = process_word(word)
                if len(processed_word) > 0:
                    if processed_word in word_frequencies:
                        word_frequencies[processed_word] += 1
                    else:
                        word_frequencies[processed_word] = 1
    return word_frequencies


if __name__ == '__main__':
    print(main())
