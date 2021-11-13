# This code will not run __main__ code from area.py
import area

def kg_pound(kg):
    return 2.204 * kg

# special variable
if __name__ == '__main__':
    print('Test dunder')
    print(kg_pound(10))
    print(area.rectangle(4, 7))