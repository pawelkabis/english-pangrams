def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    phrase = set(sentence.lower())
    if alphabet.difference(phrase):
        print(alphabet.difference(phrase))
        return False
    return True


