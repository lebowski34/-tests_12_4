import unittest
import logging
from main import Runner

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('runner_tests.log', mode='w', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s: %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        print("Running test_walk")
        try:
            runner = Runner('TestRunner', -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')
            runner.walk()

    def test_run(self):
        print("Running test_run")
        try:
            runner = Runner(12345)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')
            runner.run()

if __name__ == '__main__':
    unittest.main()
