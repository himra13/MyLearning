from math import pi

def square(side):
    return side**2

def triangle(height, width):
    return 1/2 * height * width

def circle(radius):
    return pi * radius**2

if __name__ == '__main__':
    area = triangle(12, 4)
    print(f'area = {area}')