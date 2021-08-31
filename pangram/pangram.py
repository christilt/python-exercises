def is_pangram(sentence):
    return all(x in sentence.lower() for x in 'abcdefghijklmnopqrstuvwxyz')
