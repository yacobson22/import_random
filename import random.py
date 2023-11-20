import random

def generate_random_numbers(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(random.randint(1, 100))
    return random_numbers

def main():
    n = int(input("Сколько случайных чисел вы хотите сгенерировать? "))
    random_numbers = generate_random_numbers(n)
    print("Сгенерированные случайные числа:")
    for num in random_numbers:
        print(num)

if __name__ == "__main__":
    main()
