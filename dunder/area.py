def rectangle(width, height):
    return width * height

def square(s):
    return s**2

# we can leverage this as the test code block
if __name__ == '__main__':
    print(rectangle(3,5))
    print('this is test code')

    # QA
    w = int(input("width = "))
    h = int(input("height = "))
    print(rectangle(w, h))