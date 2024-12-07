import unittest
import random

# Функция для деления двух чисел
def divide(a, b):
    if b == 0:
        raise ValeuError("Деление на ноль недопустимо.")
      return a / b

# Функция для проверки четности числа
def is_even(num):
    return num % 2 == 0

class TestMathOperations(unittest.TestCase):

    def test_divide(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
      print(f"Тест: делим {a} на {b}")
      result = divide(a, b)
      print(f"Результат: {result}")
      self.assertIsIntance(result, float)

      def test_is_even(self):
          num = random.randint(1, 100)
          print(f"Тест: число {num} является {'четным' if is_even(num) else 'нечетным'}.")

if __name__ == "__main__":
    unittest.main()
