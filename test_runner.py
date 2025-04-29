import unittest
import importlib

class TestAssignmentOne(unittest.TestCase):
    def test_01(self):
        self.assertTrue(answers.answer_01)
    def test_02(self):
        self.assertEqual(answers.answer_02, 4)
    def test_03(self):
        self.assertGreaterEqual(answers.answer_03(1.61), 1)
        self.assertGreaterEqual(answers.answer_03(21.095), 13)
        self.assertGreaterEqual(answers.answer_03(42.195), 26)
        self.assertLessEqual(answers.answer_03(1.61), 2)
        self.assertLessEqual(answers.answer_03(21.095), 14)
        self.assertLessEqual(answers.answer_03(42.195), 27)
    def test_04(self):
        self.assertGreaterEqual(answers.answer_04(1.0), 1.6)
        self.assertGreaterEqual(answers.answer_04(13.1), 21)
        self.assertGreaterEqual(answers.answer_04(26.2), 42)
        self.assertLessEqual(answers.answer_04(1.0), 1.7)
        self.assertLessEqual(answers.answer_04(13.1), 22)
        self.assertLessEqual(answers.answer_04(26.2), 43)
    def test_05(self):
        self.assertGreaterEqual(answers.answer_05(212), 100.0)
        self.assertLessEqual(answers.answer_05(32), 0.0)
    def test_06(self):
        self.assertGreaterEqual(answers.answer_06(100), 212.0)
        self.assertLessEqual(answers.answer_06(0), 32.0)
    def test_07(self):
        self.assertEqual(answers.answer_07("world"), 'Hello, world!')
        self.assertEqual(answers.answer_07("Python"), 'Hello, Python!')
        self.assertEqual(answers.answer_07("Skywalker"), 'Hello, Skywalker!')
    def test_08(self):
        self.assertEqual(answers.answer_08(1000), '1,000')
        self.assertEqual(answers.answer_08(10000), '10,000')
        self.assertEqual(answers.answer_08(100000), '100,000')
        self.assertEqual(answers.answer_08(1000000), '1,000,000')
        self.assertEqual(answers.answer_08(10000000), '10,000,000')
    def test_09(self):
        self.assertTrue(answers.answer_09(0))
        self.assertTrue(answers.answer_09(2))
        self.assertFalse(answers.answer_09(1))
        self.assertFalse(answers.answer_09(3))
        self.assertFalse(answers.answer_09(5))
    def test_10(self):
        self.assertTrue(answers.answer_10(5, 1))
        self.assertTrue(answers.answer_10(5, 5))
        self.assertFalse(answers.answer_10(5, 2))
        self.assertFalse(answers.answer_10(5, 3))
        self.assertFalse(answers.answer_10(5, 4))
        self.assertTrue(answers.answer_10(4, 1))
        self.assertTrue(answers.answer_10(4, 2))
        self.assertTrue(answers.answer_10(4, 4))
        self.assertFalse(answers.answer_10(4, 3))

chapter_name = "使用資料類別運算顯示與判斷"
answers = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentOne)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"您在「{chapter_name}」章節的 {number_of_test_runs} 道練習題中答對了 {number_of_successes} 題。")