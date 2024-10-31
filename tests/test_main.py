import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        # Тестовый запуск main, проверка вывода
        self.assertEqual(main(), None)

if __name__ == '__main__':
    unittest.main()
