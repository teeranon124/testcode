import unittest


def alternate(s):
    max_length = 0
    unique_chars = list(set(s))

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            first, second = unique_chars[i], unique_chars[j]
            strings = ""

            for char in s:
                if char == first or char == second:
                    strings += char

            valid = True
            for k in range(len(strings) - 1):
                if strings[k] == strings[k + 1]:
                    valid = False
                    break

            if valid:
                max_length = max(max_length, len(strings))

    return max_length


class TestAlternate(unittest.TestCase):
    def test_abaacdabd_should_return_4(self):
        self.assertEqual(alternate("abaacdabd"), 4)  # "abab" มีความยาว 4

    def test_beabeefeab_should_return_5(self):
        self.assertEqual(alternate("beabeefeab"), 5)  # "babab" มีความยาว 5

    def test_aaaa_should_return_0(self):
        self.assertEqual(alternate("aaaa"), 0)  # สลับไม่ได้

    def test_abababab_should_return_8(self):
        self.assertEqual(alternate("abababab"), 8)  # "abababab" มีความยาว 8

    def test_abcabc_should_return_4(self):
        self.assertEqual(alternate("abcabc"), 4)  # "abab" มีความยาว 4

    def test_abacaba_should_return_3(self):
        self.assertEqual(alternate("abacaba"), 3)  # "bcb" มีความยาว 3

    def test_xyxyxy_should_return_6(self):
        self.assertEqual(alternate("xyxyxy"), 6)  # "xyxyxy" มีความยาว 6

    def test_xxyyzz_should_return_0(self):
        self.assertEqual(alternate("xxyyzz"), 0)  # สลับไม่ได้

    def test_a_should_return_0(self):
        self.assertEqual(alternate("a"), 0)  # สลับไม่ได้

    def test_ab_should_return_2(self):
        self.assertEqual(alternate("ab"), 2)  # "ab" มีความยาว 2
