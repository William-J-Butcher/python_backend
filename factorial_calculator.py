""""Создайте класс-функцию Python, которая считает факториал числа при вызове экземпляра. 
Экземпляр должен запоминать последние k значений. Параметр k передаётся при создании экземпляра. 
Добавьте метод для просмотра ранее вызываемых значений и их факториалов. Добавьте к ним логирование 
ошибок и полезной информации.Также реализуйте возможность запуска из командной строки с передачей параметров."""

import logging
import argparse

class FactorialCalculator:

    def __init__(self, k):
        self.k = k
        self.history = []
        self.logger = logging.getLogger('FactorialCalculator')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def calculate_factorial(self, n):
        try:
            if n < 0:
                raise ValueError("Factorial is not defined for negative numbers")
            elif n == 0 or n == 1:
                result = 1
            else:
                result = 1
                for i in range(2, n + 1):
                    result *= i
            self.history.append((n, result))
            if len(self.history) > self.k:
                self.history.pop(0)
            self.logger.info(f"Calculated factorial of {n}: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error calculating factorial of {n}: {str(e)}")
            raise

    def view_history(self):
        for n, result in self.history:
            print(f"Factorial of {n}: {result}")

def main():
    parser = argparse.ArgumentParser(description='Factorial Calculator')
    parser.add_argument('k', type=int, help='Number of recent values to remember')
    parser.add_argument('n', type=int, nargs='*', help='Numbers to calculate factorial')
    args = parser.parse_args()
    calculator = FactorialCalculator(args.k)
    for num in args.n:
        calculator.calculate_factorial(num)
    calculator.view_history()

if __name__ == '__main__':
    main()

# запустить этот скрипт из командной строки, передавая параметры, например:
#     python factorial_calculator.py 3 5 3 4 2
# В этом примере мы создаем экземпляр класса FactorialCalculator с k=3 и считаем 
# факториалы чисел 5, 3, 4 и 2. Затем мы выводим историю последних 3 значений.





