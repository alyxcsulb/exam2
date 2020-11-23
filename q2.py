# random letter generator
#revised answer for midterm 2 from lecture

def main():
    START = ord('A')
    END = ord('Z')
    COUNT = 30

    import random

    rand_letters = [chr(random.randint(START, END)) for _ in range(COUNT)]

    print(sorted(rand_letters, reverse=False))
    unique = list(set(rand_letters))
    print(sorted(unique, reverse=True))

main()