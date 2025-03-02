import unittest


def alternatingCharacters(s):
    count = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            count += 1
    return count


class TestAlternatingCharacters(unittest.TestCase):
    def test_all_AAAA_should_remove_3(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)  # ลบ 3 ตัว เหลือ "A"

    def test_all_BBBBB_should_remove_4(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)  # ลบ 4 ตัว เหลือ "B"

    def test_alternating_ABABABAB_should_remove_0(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)  # ไม่ต้องลบ

    def test_alternating_BABABA_should_remove_0(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)  # ไม่ต้องลบ

    def test_AAABBB_should_remove_4(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)  # ลบ 4 ตัว เหลือ "AB"

    def test_AABBAABB_should_remove_4(self):
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)  # ลบ 4 ตัว เหลือ "ABAB"

    def test_ABABABAA_should_remove_1(self):
        self.assertEqual(alternatingCharacters("ABABABAA"), 1)  # ลบ 1 ตัว เหลือ "ABABABA"

    def test_ABBABBAA_should_remove_3(self):
        self.assertEqual(alternatingCharacters("ABBABBAA"), 3)  # ลบ 3 ตัว เหลือ "ABABABA"

    def test_long_hackerrank_case_should_remove_660(self):
        self.assertEqual(
            alternatingCharacters(
                "BABABBBBBABBABBBAAABBBBBBBBABBBBBABBBAABBBBABBBBBBBAABABBBBBBABBABBBBBBBBBABBBBBABBABBBBABABBBBBBBBBBBBBBBBBBBABBBBBAABABBBBBBBBBBBABABBBABBBABBBBBBBBBBABBBBBABBBABBBABBABBBBBBAABBBABABBBAABABAABBBBAABBBBBBBBBAAABBABABBABBBABBBBABBBBBABABBBBABABBBAABBABBAABBBBBBABBABBBBBBBBBBBBBBBBBABBBBBBABBBBBBBBABBABBBBBBBBBAAABBBBBBBBBABBABABBBAAABBBBBBABBABBBBBBBABBBBBABBBABBAABAABAAABABBBBBBBABBBBABBBBBABBBBBBABBABBBBBBBBBBBBBBBBBABBABBBAABBBBBAABABBBBBBAABBBBBBBBBABBBBBABBABBBBBBBBBABBBBBBABBBABBBBBABBBBBBBBBBBBBBBBBBABBBBBBBBBBABBBBABABBBBBBBBABBBBBBBBBABBBBBAAABBBBABABABBBBABBBBBBBBBBAABBBBBBBBABBAABBBBBBBBBABAABBBBBBBBBBBBABBBBABABBBBBBBBABBBBBBBBBBBBABBBBABBBBBABBBBBBBBBBABBAABBBABBBBBBBBBABBBBAABBBBBBBBABABABBBBBABBBBBBBBBBBBBBBBBBABBBBABBBBBABBABABAABBBABBBBBBBBBAABABABBBBBBBBAABBBBABBABBBABBBBAABBABABBBBABAABBBBBBBBBBABBABBBBBABAABBBBBBBBBBBBABABBBBBBBBBBABAABABBBBABBBBBBBBBBBBBABBBBBABBABBAABBBBABBBBBBBBBBBAABBBBBBBBBBBBBBAABABBBBBABBBBBBBBBABBBBABBBBABABBABBBBABABBBABABAAABBBBAAAAAABBBA"
            ),
            660,
        )  # test case จาก Hackerrank
