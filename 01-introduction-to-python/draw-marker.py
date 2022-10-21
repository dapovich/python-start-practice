# Program to draw character 'D' with markers 'H'
def main():
    thickness = 3
    lenght = 28
    c = "H"

    # Top layer
    for item in range(thickness - 1, -1, -1):
        print(c * (lenght - item * thickness))

    # Medium layer
    for item in range(thickness * 3):
        print((c * (thickness + 2)) + (c * (thickness + 2)).center(thickness * 14))

    # Down layer
    for item in range(0, thickness):
        print(c * (lenght - item * thickness))


if __name__ == "__main__":
    main()
