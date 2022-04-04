# ----------------- 1. ----------------------
with open('file_5_1.txt', 'w', encoding='utf-8') as my_file1:
    while True:
        line = input('Введите строку ')
        if line == "":
            break
        my_file1.writelines(line + '\n')
#
# ----------------- 2. ----------------------
with open('file_5_2.txt', encoding='utf-8') as my_file2:
    content = my_file2.readlines()
    print(f'Количество строк в файле: {len(content)}')
    for k, n in enumerate(content, 1):
        print('В строке № {}  слов: {}'.format(k, len(n)))

# ----------------- 3. ----------------------
from functools import reduce

with open('file_5_3.txt', 'r', encoding='utf-8') as my_file3:
    data_ = my_file3.readlines()
    print(data_)

employees = [{x: float(y)} for x, y in dict(n.split() for n in data_).items()]
print(employees)

top_rated = [name for n in employees for name, income in n.items() if float(income) > 20000]
average_salary = reduce(lambda x, y: x + y, [sal for n in employees for sal in n.values()]) / len(employees)

print(f'Сотрудники с доходом от 20 000: {top_rated}')
print('Средняя зарплата: {:.2f}'.format(average_salary))

# ----------------- 4. ----------------------
import adds.dictionary as dic

with open('file_5_4_input.txt', 'r', encoding='utf-8') as in_put, \
        open('file_5_4_output.txt', 'w', encoding='utf-8') as out_put:
    while True:
        df = in_put.readline().strip()
        if not df:
            break
        line = [n.strip() for n in df.split('—')]
        line[0] = dic.translate(line[0])
        out_put.write(" — ".join(line) + '\n')

# ----------------- 5. ----------------------
import random

list_of_nums = " ".join([str(random.randint(1, 999)) for i in range(10)])
with open('file_5_5.txt', 'w+', encoding='utf-8') as file:
    file.write(list_of_nums)
    file.seek(0)
    result = file.read().split()
result = reduce(lambda x, y: int(x) + int(y), result)
print(result)

# ----------------- 6. ----------------------
result_dict = {}
with open('file_5_6.txt', encoding='utf-8') as sub:
    for line in sub:
        subject, hours = line.split(':')
        total_hours = sum(map(int, ''.join(i for i in hours if i == " " or '0' <= i <= '9').split()))
        result_dict[subject] = total_hours
print(result_dict)

# ----------------- 7. ----------------------
import json

financial_stats = {}
with open('file_5_7.txt', encoding='utf-8') as fin_stat, open('my_json.json', 'w', encoding='utf-8') as json_file:
    profit_companies = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in fin_stat}

    average_profit = sum(int(profit) for profit in profit_companies.values() if int(profit) > 0) / len(
        [int(profit) for profit in profit_companies.values() if int(profit) > 0])

    output = [profit_companies, {"average_profit": average_profit}]

    json.dump(output, json_file)
