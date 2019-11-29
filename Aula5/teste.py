#!/usr/bin/env python3
import unittest



def soma(n1,n2):
    return n1 +n2


def subtrai(n1,n2):
    return n1 - n2


class Teste(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(soma(2,2),4)
        self.assertLess(soma(5,5),12)

    def teste_subtrai(self):
        self.assertEqual(subtrai(10,2),8)
        self.assertGreater(subtrai(10,4),3)

if __name__ == '__main__':
    unittest.main()


    # assert soma(3,2) == 5, "modulo soma falhou"
    # assert soma(3,4) == 6, "modulo soma2 falhou"


