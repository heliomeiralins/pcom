import unittest

from line_codes import BinaryData


class TestLineCodes(unittest.TestCase):

    def setUp(self):
        self.b = BinaryData('0b10110001101')

    def test_nrzl(self):
        self.assertEqual(
            list(self.b.nrz_l()), [1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1])

    def test_nrzm(self):
        self.assertEqual(
            list(self.b.nrz_m()), [1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1])

    def test_nrzs(self):
        self.assertEqual(
            list(self.b.nrz_s()), [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1])

    def test_unipolarrz(self):
        self.assertEqual(
            list(self.b.unipolar_rz()),
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]
        )

    def test_polarrz(self):
        self.assertEqual(
            list(self.b.polar_rz()),
            [1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1,
                0, -1, 0, 1, 0, 1, 0, -1, 0, 1, 0]
        )

    def test_ami(self):
        self.assertEqual(
            list(self.b.ami()),
            [1, 0, -1, 1, 0, 0, 0, -1, 1, 0, -1]
        )

    @unittest.skip('Not implemented')
    def test_hdb3(self):
        raise NotImplementedError

    def test_manchester(self):
        self.assertEqual(
            list(self.b.manchester()),
            [1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1,
                1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1]
        )

    def test_dif_manchester(self):
        self.assertEqual(
            list(self.b.dif_manchester()),
            [-1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1,
                1, 1, -1, 1, -1, 1, -1, -1, 1, -1]
        )
