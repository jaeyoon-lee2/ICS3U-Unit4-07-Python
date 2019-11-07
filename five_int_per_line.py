#!/user/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Nov 2019
# This program prints out all the valid RGB values


def main():
    # this function prints out all the valid RGB values

    # process & output
    for counter in range(1000, 2001):
        if counter % 5 != 4:
            print(counter, " ", end = "")
        else:
            print(counter)


if __name__ == "__main__":
    main()
