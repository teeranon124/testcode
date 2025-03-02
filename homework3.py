import unittest


def caesarCipher(s, k):
    k %= 26
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in s:
        if char in lower:
            result += lower[(lower.index(char) + k) % 26]
        elif char in upper:
            result += upper[(upper.index(char) + k) % 26]
        else:
            result += char

    return result


class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")  # เลื่อน 2 ตำแหน่ง
        self.assertEqual(
            caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5),
            "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj",
        )  # เลื่อน 5 ตำแหน่ง
        self.assertEqual(
            caesarCipher("Hello_World!", 4), "Lipps_Asvph!"
        )  # เลื่อน 4 ตำแหน่ง
        self.assertEqual(caesarCipher("abcXYZ", 3), "defABC")  # เลื่อน 3 ตำแหน่ง
        self.assertEqual(caesarCipher("xyzABC", 1), "yzaBCD")  # เลื่อน 1 ตำแหน่ง
        self.assertEqual(caesarCipher("123!@#", 10), "123!@#")  # ไม่มีตัวอักษร เลื่อนไม่ได้
        self.assertEqual(
            caesarCipher("Zero-Test", 26), "Zero-Test"
        )  # เลื่อน 26 ตำแหน่ง (ไม่เปลี่ยนแปลง)
        self.assertEqual(
            caesarCipher("Caesar-Cipher", 13), "Pnrfne-Pvcure"
        )  # เลื่อน 13 ตำแหน่ง
        self.assertEqual(
            caesarCipher("The quick brown fox jumps over the lazy dog", 7),
            "Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn",
        )  # เลื่อน 7 ตำแหน่ง
