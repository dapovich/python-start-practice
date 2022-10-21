def main():
    # Design parameters
    height = 10
    width = height * 3
    pattern = "(.)"

    if height < 11:
        print("Design limitation: height must be greater than 11")
        return "Can't design carpet with such height"
    
    for stick_count in range(1, height, 2):
        print((pattern * stick_count).center(width, ":"))

    print(3 * pattern + 'Welcome :)'.center(width - 6 * len(pattern), ":") + 3 * pattern)

    for stick_count in range(height - 2, 0, -2):
        print((pattern * stick_count).center(width, ":"))


if __name__ == '__main__':
    main()
