# Основы языка программирования Python
# условные конструкции. операции сравнения
#Задание «Стоимость доставки»
#Условие задачи
#Напишите программу, которая проверяет вес посылки пользователя в килограммах (переменная weight).
#Если вес не превышает 10 кг, выведите сообщение “Стоимость доставки: 200 руб.”.
#Если вес больше 10 кг, выведите сообщение “Стоимость доставки: 500 руб.”.
import pytest

def get_cost(weight: int):
    if weight <= 10:
        return 'Стоимость доставки: 200 руб.'
    else:
        return 'Стоимость доставки: 500 руб.'

@pytest.mark.parametrize("weight, expected_cost", [
    (0, '200'),  # граничное значение
    (5, '200'),  # значение внутри диапазона
    (10, '200'),  # граничное значение
    (11, '500'),  # значение сразу после границы
    (15, '500'),  # значение внутри диапазона
    (100, '500'),  # большое значение
])
def test_get_cost(weight, expected_cost):
    delivery = get_cost(weight)
    assert expected_cost in delivery, f"Стоимость доставки должна быть {expected_cost} руб. при весе {weight} кг"

if __name__ == '__main__':
    pytest.main([ "--collect-only"])
