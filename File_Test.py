import unittest
from unittest import TestCase

class File_Test:
    def openfile(self):
        fp = open("score.csv", "r", encoding="utf-8")
        excel = fp.readlines()
        return excel

    def test_construtor(self):
        file = Score()
        self.assertIsNotNone(file)

if __name__ == "__main__":
    unittest.main()