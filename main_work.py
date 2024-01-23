import sys
sys.path.append("/path/to/functions")

from functions.func import infinite as create_string

user_enter_size = int(input("\nВведите размер списка: "))
print("Введите целые значения списка: ")
user_enter_symbols = [int(input()) for number in range(user_enter_size)]
user_enter_iter = int(input("Введите кол-во прохождений по элементам списка: "))

print("\n Результат:\n ", create_string(user_enter_symbols,user_enter_iter))