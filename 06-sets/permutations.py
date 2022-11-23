# Doesn't get the idea of the task. Make task as I see it in my way
from itertools import product


def find_permutations(x: int, y: int, z: int, n: int):
    if (x + y + z) == n:
        return "Error: failed the condition: x + y + z != n."
    permutations_list = [
        [x, y, z] 
        for x in range(n) 
        for y in range(n) 
        for z in range(n)
        if x + y + z != n
    ]
    return permutations_list


def main():
    permutations = find_permutations(1, 1, 1, 2)
    print(permutations)
    

if __name__ == '__main__':
    main()
