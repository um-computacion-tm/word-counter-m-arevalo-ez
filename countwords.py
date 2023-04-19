
def count_words(phrase):

    result = {}

    for word in phrase.split(' '):

        lower_word = word.lower()

        if lower_word in result:

            result[lower_word] += 1

        else:

            result[lower_word] = 1

    return result

if __name__ == "__main__":
    input()