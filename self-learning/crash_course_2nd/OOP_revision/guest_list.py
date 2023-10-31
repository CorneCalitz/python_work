"""Program used to fetch a list of names from a txt file"""

import sys


def addToList(_file_path):
    name = input("Name of person who is showing up\n>>>")
    personages = input("1 or 2 people\n>>>")
    sleep = input("Y/N are they sleeping here\n>>>")

    with open(_file_path, 'a') as f:
        f.write(f"{name}#{personages}%{sleep}\n")


def getList(_file_path):
    count = 0
    with open(_file_path, 'r') as f:
        for line in f:
            hash_pos = line.find("#")
            name = line[:hash_pos]
            guest_num = line[hash_pos + 1]
            sleep = line[hash_pos + 3]
            count += int(guest_num)

            print(name, guest_num, sleep)
        print("total: ", count)
        print('')


if __name__ == "__main__":
    path = 'List of guests.txt'
    while True:
        print("Guest list adder")
        print("1. Input name")
        print("2. Check list of guests and details")
        response = input(">>>")

        if response == "1":
            addToList(path)

        elif response == "2":
            getList(path)

        else:
            print("No response given")
