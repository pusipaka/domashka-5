# Урок №8. Строки
# Задание №1
# На вход подается 1 строка без пробелов.
# По данной строке определите, является ли она палиндромом
# (то есть, можно ли прочесть ее наоборот, как, например, слово "шалаш").
# Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном случае.
 string=input()
 if string==string[::-1]:
     print("yes",string[::-1])
 else:
     print("no")
# Задание №2
# Дана строка, длина которой не превосходит 1000.
# Вам требуется преобразовать все идущие подряд пробелы в один.
#  Выведите измененную строку.
print((" ").join(input().split()))


