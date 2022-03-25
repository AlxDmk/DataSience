# ------------------- 1. ---------------------------------
def divide(numerator, denominator):
    try:
        return int(numerator) / int(denominator)
    except (ValueError, ZeroDivisionError) as error:
        return error


print(divide(input('Введите числитель '), input('Введите знаменатель ')))


# --------------------- 2. -------------------------------

def person_data(**data):
    return '; '.join(f"{key}: {data[key]}" for key, value in data.items())


print(person_data(
    email=input('email: '),
    name=input('name: '),
    surname=input('surname: '),
    tel=input('tel: '),
    yearOfBirth=input('Year of birth: '),
    city=input('City: ')))


# ------------------- 3. -------------------------------------


def my_func(num_1, num_2, num_3):
    return sum(sorted([num_1, num_2, num_3])[1:])


print(my_func(3, 1, 4))

# -------------------- 4. ----------------------------------------
exponent = lambda x, y: abs(x) ** int(-abs(y))
print(exponent(12.2, -3))


def sec_exponent(x, y):
    result = 1
    for i in range(1, int(abs(y) + 1)):
        result *= abs(x)
    return 1 / result


print(sec_exponent(12.2, -3))

# --------------------5. ---------------------------------------
# Первый вариант решения:
sum_of_num = 0
flag = True
while flag:
    s = (input('Введите ряд чисел через пробел. ')).split()
    for n in s:
        if n.isdigit():
            sum_of_num += int(n)
        elif n == 'Q':
            flag = False
            break
        else:
            continue
    print(sum_of_num)


# Второй вариант решения:
def item(num=0):
    prompt = (input('Введите ряд чисел через пробел. ')).split()
    for element in prompt:
        if element.isdigit():
            num += int(element)
        elif element == 'Q':
            print(num)
            return
        else:
            continue
    print(num)
    item(num)


item()

# ----------------------- 6. ------------------------------------

int_func = lambda text: text.title()
print(int_func(input('Введите слово в нижнем регистре: ')))

# ------------------------ 7. ----------------------------------------
print(int_func('the quick brown fox jumps over the lazy dog.'))
