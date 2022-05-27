from collections import deque

hex_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
bin_numbers = dict(zip(hex_numbers,[i for i in range(len(hex_numbers))]))

def convert(hex_num):
    converted_hex_num = deque(hex_num.upper())
    return converted_hex_num

def sum_hex(first, second):
    first = first.copy()
    second = second.copy()
    
    if len(second) > len(first):
        first, second = second, first
        
    second.extendleft('0' * (len(first) - len(second)))
    
    result = deque()
    carry_over = 0 
    
    for i in range(len(first) -1, -1, -1):
        first_num = bin_numbers[first[i]]
        second_num = bin_numbers[second[i]]
        
        result_num = first_num + second_num + carry_over
        
        if result_num >= 16:
            carry_over = 1
            result_num -= 16
        else:
            carry_over = 0 
        result.appendleft(hex_numbers[result_num])
        
    if carry_over == 1:
        result.appendleft('1')
        
    return result

def mult_hex(first, second):
    first = first.copy()
    second = second.copy()
    if len(second) > len(first):
        first, second = second, first
    second.extendleft('0' * (len(first) - len(second)))
    
    result = deque('0')
    for i in range(len(first) - 1, -1, -1):
        second_num = bin_numbers[second[i]]
        
        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)
        spam.extend('0' * (len(first) - i -1))
        result = sum_hex(result, spam)
    
    return result

a = convert(input('Введите первое число'))
b = convert(input('Введите второе число'))
print(sum_hex(a, b))
print(mult_hex(a, b))