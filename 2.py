def lotto():
    '''
    LOTTO simulator.
    :return: information about the number of hits.
    '''
    entered_number_1 = input("Podaj pierwszą liczbę.")
    set_of_entered_numbers = []

    while True:
        if entered_number_1.isdigit() == False or int(entered_number_1) not in range(1, 50):
            print("Enter integer between 1 and 49.")
            entered_number_1 = input("Enter the first number.")
        else: break

    set_of_entered_numbers.append(int(entered_number_1))
    entered_number_2 = input("Enter the second number.")

    while True:
        if entered_number_2.isdigit() == False or int(entered_number_2) not in range(1, 50) or int(entered_number_2) in set_of_entered_numbers:
            print("Enter new integer between 1 and 49.")
            entered_number_2 = input("Enter the second number.")
        else: break

    set_of_entered_numbers.append(int(entered_number_2))
    entered_number_3 = input("Enter the third number.")

    while True:
        if entered_number_3.isdigit() == False or int(entered_number_3) not in range(1, 50) or int(entered_number_3) in set_of_entered_numbers:
            print("Enter new integer between 1 and 49.")
            entered_number_3 = input("Enter the third number.")
        else: break

    set_of_entered_numbers.append(int(entered_number_3))
    entered_number_4 = input("Enter the fourth number.")

    while True:
        if entered_number_4.isdigit() == False or int(entered_number_4) not in range(1, 50) or int(entered_number_4) in set_of_entered_numbers:
            print("Enter new integer between 1 and 49.")
            entered_number_4 = input("Enter the fourth number.")
        else: break

    set_of_entered_numbers.append(int(entered_number_4))
    entered_number_5 = input("Enter the fifth number.")

    while True:
        if entered_number_5.isdigit() == False or int(entered_number_5) not in range(1, 50) or int(entered_number_5) in set_of_entered_numbers:
            print("Enter new integer between 1 and 49.")
            entered_number_5 = input("Enter the fifth number.")
        else: break

    set_of_entered_numbers.append(int(entered_number_5))
    entered_number_6 = input("Enter the sixth number.")

    while True:
        if entered_number_6.isdigit() == False or int(entered_number_6) not in range(1, 50) or int(entered_number_6) in set_of_entered_numbers:
            print("Enter new integer between 1 and 49.")
            entered_number_6 = input("Enter the sixth number.")
        else: break

    set_of_entered_numbers.append(int(entered_number_6))

    print(sorted(set_of_entered_numbers))

    import random
    numbers_selected_at_random = []

    a = 6

    while a > 0:
        numbers_selected_at_random.append(random.randint(1, 49))
        a -= 1

    print(numbers_selected_at_random)

    numbers_in_both_lists = list(set(set_of_entered_numbers).intersection(numbers_selected_at_random))
    how_many_identical = len(numbers_in_both_lists)

    return f"Number of hits: {how_many_identical}"

print(lotto())







































    



























