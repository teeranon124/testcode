import unittest


def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")  # 3 หาร 3 ลงตัว
        self.assertEqual(fizzbuzz(9), "Fizz")  # 9 หาร 3 ลงตัว

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")  # 5 หาร 5 ลงตัว
        self.assertEqual(fizzbuzz(10), "Buzz")  # 10 หาร 5 ลงตัว

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")  # 15 หารทั้ง 3 และ 5 ลงตัว
        self.assertEqual(fizzbuzz(30), "FizzBuzz")  # 30 หารทั้ง 3 และ 5 ลงตัว

    def test_number(self):
        self.assertEqual(fizzbuzz(2), "2")  # 2 ไม่หาร 3 หรือ 5 ลงตัว
        self.assertEqual(fizzbuzz(7), "7")  # 7 ไม่หาร 3 หรือ 5 ลงตัว


if __name__ == "__main__":
    unittest.main()
