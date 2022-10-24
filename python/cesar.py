'''Cypher Cesar'''


def cesar(txt, offset, reverse=False):
    '''Cyphers the word, '''
    txt = txt.lower()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    offset = offset if not reverse else -offset
    cypher = ''.join([abc[(abc.find(letter) + offset) % len(abc)]
                     for (i, letter) in enumerate(txt)])
    return cypher


if __name__ == "__main__":
    print(cesar('Hola', 1))
    print(cesar('ipmb', 1, True))
    print(cesar('Lalo', 1))
    print(cesar('mbmp', 1, True))
    print(cesar('Hola', 2))
    print(cesar('jqnc', 2, True))
