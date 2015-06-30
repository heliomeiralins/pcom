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
            [1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0,
                0, 0, -1, 0, 1, 0, 0, 0, -1, 0]
        )

    def test_hdb3(self):
        b = BinaryData('0b10000')
        self.assertEqual(
            list(b.hdb3()),
            [1, 0, 0, 0, 1]
        )
        c = BinaryData('0b010111000010110100000000001011010100001')
        self.assertEqual(
            list(c.hdb3()),
            [0, 1, 0, -1, 1, -1, 0, 0, 0, -1, 1, 0, -1, 1, 0, -1, 1, 0, 0,
             1, -1, 0, 0, -1, 0, 0, 1, 0, -1, 1, 0, -1, 0, 1, 0, 0, 0, 1, -1]
        )
        d = BinaryData('0b0101110000')
        self.assertEqual(
            list(d.hdb3()),
            [0, 1, 0, -1, 1, -1, 0, 0, 0, -1]
        )

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

    def test_mlt3(self):
        self.assertEqual(
            list(self.b.mlt3()),
            [1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0]
        )
        c = BinaryData('0b10100111001')
        self.assertEqual(
            list(c.mlt3()),
            [1, 1, 0, 0, 0, -1, 0, 1, 1, 1, 0]
        )

    def test_miller(self):
        c = BinaryData('0b11001011000111101')
        self.assertEqual(
            list(c.miller()),
            [-1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1,
                1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1]
        )
