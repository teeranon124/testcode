import unittest


def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"
    return "Funny"


class TestFunnyString(unittest.TestCase):
    def test_acxz_is_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")  # ผลต่างของ s และ r เท่ากัน

    def test_bcxz_is_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")  # ผลต่างของ s และ r ไม่เท่ากัน

    def test_abcd_is_funny(self):
        self.assertEqual(funnyString("abcd"), "Funny")  # ผลต่างของ s และ r เท่ากัน

    def test_aaaa_is_funny(self):
        self.assertEqual(funnyString("aaaa"), "Funny")  # ทุกตัวอักษรเหมือนกัน ผลต่างเป็น 0

    def test_abba_is_funny(self):
        self.assertEqual(funnyString("abba"), "Funny")  # ผลต่างของ s และ r เท่ากัน

    def test_ivvkxq_is_not_funny(self):
        self.assertEqual(funnyString("ivvkxq"), "Not Funny")  # ผลต่างของ s และ r ไม่เท่ากัน

    def test_xxyy_is_funny(self):
        self.assertEqual(funnyString("xxyy"), "Funny")  # ผลต่างของ s และ r เท่ากัน

    def test_ivvkx_is_not_funny(self):
        self.assertEqual(funnyString("ivvkx"), "Not Funny")  # ผลต่างของ s และ r ไม่เท่ากัน

    def test_long_string_is_not_funny(self):
        self.assertEqual(
            funnyString(
                "fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury"
            ),
            "Not Funny",
        )
