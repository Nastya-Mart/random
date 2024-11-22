import random


def generate_password(n):
    password = ""

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += str(i) + str(j)

    return password

n = random.randint(3, 20)
print(f"Сгенерированное число: {n}")

result = generate_password(n)
print(f'Нужный пароль: {result}')


