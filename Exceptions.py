try:
    raise ZeroDivisionError # возбуждаем исключение ZeroDivisionError
except ArithmeticError: # ловим его родителя
    print("Hello from arithmetic error")
    
try:
    raise ZeroDivisionError
except ArithmeticError:
    print("Arithmetic error")
except ZeroDivisionError:
    print("Zero division error")
    
try:
    raise ZeroDivisionError
except ZeroDivisionError: # сначала пытаемся поймать наследника
    print("Zero division error")
except ArithmeticError: # потом ловим потомка
    print("Arithmetic error")
    
#Собственное исключение    
class MyException(Exception): # создаём пустой класс – исключения 
    pass
 
try:
    raise MyException("message") # поднимаем наше исключение
except MyException as e: # ловим его за хвост как шкодливого котёнка
    print(e) # выводим информацию об исключении
    
#Собственное исключение с наследованием    
class ParentException(Exception): # создаём пустой класс – исключения потомка, наследуемся от exception
    pass
 
class ChildException(ParentException): # создаём пустой класс – исключение наследника, наследуемся от ParentException
    pass
 
try:
    raise ChildException("message") # поднимаем исключение-наследник
except ParentException as e: # ловим его родителя
    print(e) # выводим информацию об исключении

#Собственное исключение с наследованием аргументов в конструктор    
class ParentException(Exception):
    def __init__(self, message, error): # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
        super().__init__(message) # помним про вызов конструктора родительского класса
        print(f"Errors: {error}") # печатаем ошибку
 
class ChildException(ParentException): # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, message, error):
        super().__init__(message, error)
 
try:
    raise ChildException("message", "error") # поднимаем исключение-наследник, передаём дополнительный аргумент
except ParentException as e:
    print(e) # выводим информацию об исключении
    
#Площадь квадрата
class NonPositiveDigitException(ValueError):
    pass
 
class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')

a = Square(int(input()))