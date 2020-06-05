from unittest import TestCase

from funkcje.gra import kololowanko


class Test(TestCase):
    def setUp(self):
        self.wartosc = 3

    def test_kololowanko(self):
        self.assertEqual(kololowanko(self.wartosc), ("3", "red"))

