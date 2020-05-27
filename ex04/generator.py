import time


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if isinstance(text, str) and option in ('shuffle',
                                            'ordered', 'unique', None):
        lst = text.split(sep)
        if option is None:
            return lst
        elif option == 'shuffle':
            x = 0
            tmp = []
            while x < len(lst):
                tmp.append((x * time.time() * 10000000000 + 5675) % 3645)
                x += 1
            tmp, lst = zip(*sorted(zip(tmp, lst)))
            return lst
        elif option == 'ordered':
            return sorted(lst)
        elif option == 'unique':
            lst = list(dict.fromkeys(lst))
            return lst
    else:
        print("ERROR")
        exit()


text = "Le Lorem Ipsum est simplement le le le du faux texte."
print("NONE")
for word in generator(text, sep=" "):
    print(word)
print("SHUFFLE")
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print("UNIQUE")
for word in generator(text, sep=" ", option="unique"):
    print(word)
print("ORDERED")
for word in generator(text, sep=" ", option="ordered"):
    print(word)
text = 1
for word in generator(text, sep=" "):
    print(word)
