import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def test_something(self):
        print('test')
        self.assertEqual(True, True)  # add assertion here
        #self.assertRaises()

    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()
