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
    def test_sorted_grid_should_return_yes(self):
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")  # test 0

    def test_unsorted_grid_should_return_no(self):
        self.assertEqual(gridChallenge(["uxf", "vof", "hmp"]), "NO")  # test 1

    def test_mixed_grid_should_return_no(self):
        self.assertEqual(
            gridChallenge(["lyivr", "uweor", "qxwyr", "uikjd"]), "NO"
        )  # test 2

    def test_single_character_grid_should_return_yes(self):
        self.assertEqual(gridChallenge(["a"]), "YES")

    def test_reverse_sorted_rows_should_return_no(self):
        self.assertEqual(gridChallenge(["zzzz", "yyyy", "xxxx", "wwww"]), "NO")

    def test_varied_length_grid_should_return_yes(self):
        self.assertEqual(gridChallenge(["abc", "defg", "hij"]), "YES")

    def test_larger_sorted_grid_should_return_yes(self):
        self.assertEqual(
            gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )

    def test_perfectly_sorted_grid_should_return_yes(self):
        self.assertEqual(
            gridChallenge(["abcde", "fghij", "klmno", "pqrst", "uvwxy"]), "YES"
        )
