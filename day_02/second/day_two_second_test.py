# test_my_module.py
from file_utils.read_file import read_file

import unittest
from main import main


class DayTwoSecondAssignmentTest(unittest.TestCase):

    def test_correct_sum(self):
        file = read_file("example_input.txt")

        self.assertEqual(main(file), 2286)


if __name__ == '__main__':
    unittest.main()
