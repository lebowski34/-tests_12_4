import unittest
import logging
from main import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('TestRunner', -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')
            runner.walk()
    def test_run(self):
        try:
            runner = Runner(12345)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')
            runner.run()

if __name__ == '__main__':
    unittest.main()
