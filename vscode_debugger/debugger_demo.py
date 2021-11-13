def ticket(passenger_type):
    if passenger_type == 'A':
        fare = 50
    elif passenger_type == 'S':
        fare = 45
    elif passenger_type == 'C' or passenger_type == 'E':
        fare = 25
    else:
        fare = 40
    return fare

p = input("passenger type [A]dult, [S]tudent, [C]hild, [E]lder, [O]thers: ")
print(ticket(p))