class InvalidData(Exception):
    def __init__(self, massage):
        self.massage = massage


class Processing(Exception):
    def __init__(self, massage):
        self.massage = massage


def current_year(a):
    if a == 2024:
        raise Processing('год указан верно')
    if a != 2024:
        raise InvalidData('неверно указан текущий год')
    return a


try:
    res = current_year(2024)
except InvalidData as e:
    print(f'Ошибка: {e}')
except Processing as e:
    print(f'Внимание: {e}')
finally:
    print('Домашнее задание завершено')





