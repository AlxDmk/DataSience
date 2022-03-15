# 1
my_first_list = [1, True, [1, 3, 6], 'some text', 4.45, 3, '45']
for l in my_first_list:
  print(type(l))

# 2 
count = int(input("Введите длину списка: "))
my_second_list = []
for i in range(count):
  my_second_list.append(input('Введите {}-й элемент: '.format(i+1)))
length = count-1 if count % 2 else count
for i in range(0, length , 2):
  my_second_list[i], my_second_list[i+1] = my_second_list[i+1], my_second_list[i]  

# 3
my_string = 'зима '*2 + 'весна '*3 + 'лето '*3 +  'осень '*3 + 'зима'
request = int(input("Введите число месяца "))

list_solution = my_string.split(' ')
print (f'Время года (в списке) для {request}-го месяца: {list_solution[request - 1]}')

dict_solution = {}
for ind, el in enumerate(list_solution, 1):
  dict_solution[ind] = el
print(f'Время года (в словаре) для {request} -го месяца: {dict_solution[request]}')

# 4 
request_1 = input("Введите строку из нескольких слов  ").split(" ")
for ind, el in enumerate(request_1, 1):
  print(ind, el[:10])

# 5
my_rating_list = [7, 5, 3, 3, 2]
my_rating_list.append(int(input("Введите рейтинг ")))
my_rating_list.sort(reverse = True)

# 6
#Сбор данных
dict_of_features = {
  'название': 'Наименование товара',
  'цена': 'Цена товара' ,
  'количество': 'Количество',
  'ед': 'Единица измерения'
}
items = []
while True:
  dict_item = dict()
  for key in dict_of_features:
    dict_item[key] = input(f'{dict_of_features[key]} ')    
  items.append(dict_item) 
  if input('Продолжить добавление? д/н ') == 'н':
    break
    
# Формирование структуры
catalogue = []
for position, item in enumerate(items, 1):
  catalogue.append((position, item))
print(catalogue)

# Сбор аналитики
analytics = dict_of_features.copy()
for key in analytics:
  analytics[key] = []
  
for i in range(len(items)):
  for key in analytics:    
    if items[i][key] not in analytics[key]:
      analytics[key].append(items[i][key])
print(analytics)  
