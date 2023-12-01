def is_uppercase(s):
    for char in s:
        if not ('A' <= char <= 'Z'):
            return False
    return True


def get_input():
    return input("Введіть текст для перевірки: ")


def show_result(r):
    print(r)


while __name__ == '__main__':
    show_result(is_uppercase(get_input()))
