import random
def generate_password(n):

    password = []
    used_numbers = set()

    for i in range(1, 21):
        if i != n and i not in used_numbers:
            for j in range(i + 1, 21):
                if j not in used_numbers and (n % (i + j) == 0):
                    password.append(str(i) + str(j))
                    used_numbers.add(i)
                    used_numbers.add(j)
                    break
    return ''.join(password)

for n in range(3, 21):
    print(f"Для числа {n}: {generate_password(n)}")