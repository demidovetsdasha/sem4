import unittest
from general import *
from true_table import *


class TestTrueTable(unittest.TestCase):
    def setUp(self):
        self.formula1 = "(a&b)~(!c)"
        self.formula2 = "d|(c&(!a))"
        self.formula3 = "(e~d)&(b->a)"

    def test_reversed_polish_notation(self):
        result1 = reversed_polish_notation(self.formula1)
        result2 = reversed_polish_notation(self.formula2)
        result3 = reversed_polish_notation(self.formula3)
        self.assertEqual(result1, "ab&c!~")
        self.assertEqual(result2, "dca!&|")
        self.assertEqual(result3, "ed~ba>&")

    def test_true_table(self):
        table1, variables1 = true_table(self.formula1, False)
        table2, variables2 = true_table(self.formula2, False)

        result1 = [0, 1, 0, 1, 0, 1, 1, 0]
        result2 = [0, 1, 1, 1, 0, 1, 0, 1]

        for i in range(0, len(result1)):
            self.assertEqual(result1[0], table1[0][len(variables1)])

        for j in range(0, len(result2)):
            self.assertEqual(result2[0], table2[0][len(variables2)])


class TestGeneralFunctions(unittest.TestCase):
    def setUp(self):
        self.formula1 = "(a&b)~(!c)"
        self.formula2 = "d|(c&(!a))"

    def test_sdnf(self):
        table1, variables1 = true_table(self.formula1, False)
        table2, variables2 = true_table(self.formula2, False)

        result1 = create_sdnf(table1, variables1)
        result2 = create_sdnf(table2, variables2)
        self.assertEqual(result1, "((!a)&(!b)&c)|((!a)&b&c)|(a&(!b)&c)|(a&b&(!c))")
        self.assertEqual(result2, "((!a)&(!c)&d)|((!a)&c&(!d))|((!a)&c&d)|(a&(!c)&d)|(a&c&d)")

    def test_sknf(self):
        table1, variables1 = true_table(self.formula1, False)
        table2, variables2 = true_table(self.formula2, False)

        result1 = create_sknf(table1, variables1)
        result2 = create_sknf(table2, variables2)
        self.assertEqual(result1, "(a|b|c)&(a|(!b)|c)&((!a)|b|c)&((!a)|(!b)|(!c))")
        self.assertEqual(result2, "(a|c|d)&((!a)|c|d)&((!a)|(!c)|d)")

    def test_num_sknf(self):
        table1, variables1 = true_table(self.formula1, False)
        table2, variables2 = true_table(self.formula2, False)

        result_bin_sknf1 = binary_num_sknf(table1, variables1)
        result_dec_sknf1 = decimal_num_sknf(table1, variables1)
        self.assertEqual(result_bin_sknf1, "&(000,010,100,111)")
        self.assertEqual(result_dec_sknf1, "&(0,2,4,7)")

        result_bin_sknf2 = binary_num_sknf(table2, variables2)
        result_dec_sknf2 = decimal_num_sknf(table2, variables2)
        self.assertEqual(result_bin_sknf2, "&(000,100,110)")
        self.assertEqual(result_dec_sknf2, "&(0,4,6)")

    def test_num_sdnf(self):
        table1, variables1 = true_table(self.formula1, False)
        table2, variables2 = true_table(self.formula2, False)

        result_bin_sdnf1 = binary_num_sdnf(table1, variables1)
        result_dec_sdnf1 = decimal_num_sdnf(table1, variables1)
        self.assertEqual(result_bin_sdnf1, "|(001,011,101,110)")
        self.assertEqual(result_dec_sdnf1, "|(1,3,5,6)")

        result_bin_sdnf2 = binary_num_sdnf(table2, variables2)
        result_dec_sdnf2 = decimal_num_sdnf(table2, variables2)
        self.assertEqual(result_bin_sdnf2, "|(001,010,011,101,111)")
        self.assertEqual(result_dec_sdnf2, "|(1,2,3,5,7)")

    def test_index_form(self):
        table1, variables1 = true_table(self.formula1, False)
        table2, variables2 = true_table(self.formula2, False)

        result_bin1 = index_form(table1)
        result_bin2 = index_form(table2)
        self.assertEqual(result_bin1, "01010110")
        self.assertEqual(result_bin2, "01110101")

        result_dec1 = index_form_decimal(index_form(table1))
        result_dec2 = index_form_decimal(index_form(table2))
        self.assertEqual(result_dec1, "86")
        self.assertEqual(result_dec2, "117")


if __name__ == "__main__":
    unittest.main()
