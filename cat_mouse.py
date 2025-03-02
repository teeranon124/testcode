import unittest


def cat_and_mouse(x, y, z):
    distance_a = abs(x - z)
    distance_b = abs(y - z)

    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"


class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(1, 4, 2), "Cat A")  # Cat A ใกล้กว่า
        self.assertEqual(cat_and_mouse(5, 10, 6), "Cat A")  # Cat A ใกล้กว่า

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(4, 1, 2), "Cat B")  # Cat B ใกล้กว่า
        self.assertEqual(cat_and_mouse(10, 5, 6), "Cat B")  # Cat B ใกล้กว่า

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")  # ห่างจาก Cat เท่ากันทั้ง 2 ตัว
        self.assertEqual(
            cat_and_mouse(5, 5, 5), "Mouse C"
        )  # Cat กับ Mouse อยู่ตำแหน่งเดียวกัน


if __name__ == "__main__":
    unittest.main()
