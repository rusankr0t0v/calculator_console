"""
Основной модуль программы калькулятор
"""
import math_utils.operations



def main(number_a = False, number_b = False, operator = False):
    """
    Главная функция, запускается при старте программы.
    После получения всех параметров, вызывает функцию action()
    :param number_a: Число А - по умолчанию False
    :param number_b: Число Б - по умолчанию False
    :param operator: Оператор - по умолчанию False
    :return: None
    """
    while number_a is False or number_b is False or operator is False:
        try:
            if number_a is False:
                number_a = int(input('Введите число A: '))
            elif number_b is False:
                number_b = int(input('Введите число B: '))
            elif operator is False:
                inp_oper = input('Введите оператор: \n "+" сложение \n "-" вычитание \n '
                                 '"*" умножение \n "/" деление \n')
                if (inp_oper == '+' or inp_oper == '-' or inp_oper == '*' or
                        inp_oper == '/' or inp_oper == '^'):
                    operator = inp_oper
        except ValueError:
            print('Вы ввели не число')
    action(number_a, number_b, operator)


def action(number_a, number_b, operator):
    """
    Функция получает два числа и оператор.
    В зависимости от оператора вызывает нужную функцию из math_utils.operations.
    Выводит в консоль результат математической операции
    :param number_a: Число А
    :param number_b: Число Б
    :param operator: Оператор
    :return: None
    """
    print('Ответ:')
    if operator == '+':
        print(math_utils.operations.add(number_a, number_b))
    elif operator == '-':
        print(math_utils.operations.subtract(number_a, number_b))
    elif operator == '/':
        if number_b == 0:
            print('На 0 делить нельзя!')
        else:
            print(math_utils.operations.divide(number_a, number_b))
    elif operator == '*':
        print(math_utils.operations.multiply(number_a, number_b))


if __name__ == '__main__':
    main()