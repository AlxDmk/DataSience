from collections import namedtuple
import statistics as st

Enterprise = namedtuple('Enterprise', 'name q1, q2, q3, q4, year', defaults=[0])
spam_dict = {}
for _ in range(int(input('Введите кол-во предприятий'))):
    args = input('Введите через пробел наименование и квартальные (1-4) значения прибыли').split()
    args.append(sum(map(int, args[1:])))
    spam_dict[_] = Enterprise._make(args)
    
average = st.mean(i.year for i in spam_dict.values())

dict_result = {}
for i  in spam_dict.values():
    dict_result.setdefault('{}'.format(('Ниже среднего: ', 'Выше среднего: ')[i.year>average]), []).append(i.name) 

print(average, dict_result, sep='\n')
