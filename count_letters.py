def count_letters(word):
    
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

if __name__ == '__main__':
    input()