import unittest


def gridChallenge(grid):
    n = len(grid)  # จำนวนแถวในกริด
    # เรียงตัวอักษรในแต่ละแถว
    for i in range(n):
        grid[i] = "".join(sorted(grid[i]))

    # ตรวจสอบคอลัมน์
    for col in range(len(grid[0])):  # ใช้ความยาวของแถวแรกเป็นจำนวนคอลัมน์
        for row in range(1, n):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"

    return "YES"


class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge(self):
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")  # test 0
        self.assertEqual(gridChallenge(["uxf", "vof", "hmp"]), "NO")  # test 1
        self.assertEqual(
            gridChallenge(["lyivr", "uweor", "qxwyr", "uikjd"]), "NO"
        )  # test 2
        self.assertEqual(gridChallenge(["a"]), "YES")
        self.assertEqual(gridChallenge(["zzzz", "yyyy", "xxxx", "wwww"]), "NO")
        self.assertEqual(gridChallenge(["abc", "defg", "hij"]), "YES")
        self.assertEqual(
            gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )
        self.assertEqual(
            gridChallenge(["abcde", "fghij", "klmno", "pqrst", "uvwxy"]), "YES"
        )
