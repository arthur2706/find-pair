import unittest
import sys, os
tests_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,tests_root + '/../')

from find_pair import validate, find_gifts_pair, find_gifts_trio

class ValidateTest(unittest.TestCase):
    def setUp(self):
        self.invalid1 = tests_root + '/invalid1.txt'
        self.invalid2 = tests_root + '/invalid2.txt'
        self.empty = tests_root + '/empty.txt'
        self.pricefile = tests_root + '/prices.txt'
        pass

    def test_validate1(self):
        try:
            validate(self.pricefile, 2500)
        except:
            self.fail("Should not fail, valid input!")

    def test_validate2(self):
        self.assertRaises(ValueError, validate, self.pricefile, -2500)

    def test_validate3(self):
        self.assertRaises(ValueError, validate, self.invalid1, 2500)

    def test_validate4(self):
        self.assertRaises(ValueError, validate, self.invalid2, 2500)

    def test_validate5(self):
        self.assertRaises(ValueError, validate, self.empty, 2500)


class FindPairTest(unittest.TestCase):
    def setUp(self):
        self.pricefile = tests_root + '/prices.txt'
        pass

    def test_pair_1(self):
        gifts, budget = validate(self.pricefile, 2500)
        selected_gifts = find_gifts_pair(gifts, budget)
        self.assertEqual(selected_gifts[0]['name'], "Candy Bar")
        self.assertEqual(selected_gifts[0]['price'], 500)
        self.assertEqual(selected_gifts[1]['name'], "Earmuffs")
        self.assertEqual(selected_gifts[1]['price'], 2000)

    def test_pair_2(self):
        gifts, budget = validate(self.pricefile, 2300)
        selected_gifts = find_gifts_pair(gifts, budget)
        self.assertEqual(selected_gifts[0]['name'], "Paperback Book")
        self.assertEqual(selected_gifts[0]['price'], 700)
        self.assertEqual(selected_gifts[1]['name'], "Headphones")
        self.assertEqual(selected_gifts[1]['price'], 1400)

    def test_pair_3(self):
        gifts, budget = validate(self.pricefile, 10000)
        selected_gifts = find_gifts_pair(gifts, budget)
        self.assertEqual(selected_gifts[0]['name'], "Earmuffs")
        self.assertEqual(selected_gifts[0]['price'], 2000)
        self.assertEqual(selected_gifts[1]['name'], "Bluetooth Stereo")
        self.assertEqual(selected_gifts[1]['price'], 6000)

    def test_pair_4(self):
        gifts, budget = validate(self.pricefile, 1100)
        selected_gifts = find_gifts_pair(gifts, budget)
        self.assertFalse(selected_gifts)

    def test_pair_5(self):
        gifts, budget = validate(self.pricefile, 0)
        selected_gifts = find_gifts_pair(gifts, budget)
        self.assertFalse(selected_gifts)


class FindTrioTest(unittest.TestCase):
    def setUp(self):
        self.pricefile = tests_root + '/prices.txt'
        pass

    def test_trio_1(self):
        gifts, budget = validate(self.pricefile, 2500)
        selected_gifts = find_gifts_trio(gifts, budget)
        self.assertEqual(selected_gifts[0]['name'], "Candy Bar")
        self.assertEqual(selected_gifts[0]['price'], 500)
        self.assertEqual(selected_gifts[1]['name'], "Paperback Book")
        self.assertEqual(selected_gifts[1]['price'], 700)
        self.assertEqual(selected_gifts[2]['name'], "Detergent")
        self.assertEqual(selected_gifts[2]['price'], 1000)

    def test_trio_2(self):
        gifts, budget = validate(self.pricefile, 3100)
        selected_gifts = find_gifts_trio(gifts, budget)
        self.assertEqual(selected_gifts[0]['name'], "Paperback Book")
        self.assertEqual(selected_gifts[0]['price'], 700)
        self.assertEqual(selected_gifts[1]['name'], "Detergent")
        self.assertEqual(selected_gifts[1]['price'], 1000)
        self.assertEqual(selected_gifts[2]['name'], "Headphones")
        self.assertEqual(selected_gifts[2]['price'], 1400)

    def test_trio_3(self):
        gifts, budget = validate(self.pricefile, 2900)
        selected_gifts = find_gifts_trio(gifts, budget)
        self.assertEqual(selected_gifts[0]['name'], "Candy Bar")
        self.assertEqual(selected_gifts[0]['price'], 500)
        self.assertEqual(selected_gifts[1]['name'], "Detergent")
        self.assertEqual(selected_gifts[1]['price'], 1000)
        self.assertEqual(selected_gifts[2]['name'], "Headphones")
        self.assertEqual(selected_gifts[2]['price'], 1400)


    def test_trio_3(self):
        gifts, budget = validate(self.pricefile, 10000)
        selected_gifts = find_gifts_trio(gifts, budget)
        self.assertEqual(selected_gifts[0]['name'], "Headphones")
        self.assertEqual(selected_gifts[0]['price'], 1400)
        self.assertEqual(selected_gifts[1]['name'], "Earmuffs")
        self.assertEqual(selected_gifts[1]['price'], 2000)
        self.assertEqual(selected_gifts[2]['name'], "Bluetooth Stereo")
        self.assertEqual(selected_gifts[2]['price'], 6000)


    def test_trio_4(self):
        gifts, budget = validate(self.pricefile, 1100)
        selected_gifts = find_gifts_trio(gifts, budget)
        self.assertFalse(selected_gifts)

    def test_trio_5(self):
        gifts, budget = validate(self.pricefile, 0)
        selected_gifts = find_gifts_trio(gifts, budget)
        self.assertFalse(selected_gifts)


if __name__ == '__main__':
    unittest.main()
