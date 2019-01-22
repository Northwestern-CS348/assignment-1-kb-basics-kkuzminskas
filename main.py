import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase
import util

class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)


    def test1(self):
        ask1 = read.parse_input("fact: (color bigbox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(aswer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (color ?X red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox")
        self.assertEqual(str(answer[1]), "?X : pyramid3")
        self.assertEqual(str(answer[2]), "?X : pyramid4")


    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : red")

    def test5(self):
        ask1 = read.parse_input("fact: (color ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : red")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : blue")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : blue")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : green")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : red")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : red")

    #assert tests
    def test6(self):
        self.KB.kb_assert(read.parse_input("fact: (color box34 blue)"))
        self.KB.kb_assert(read.parse_input("fact: (color box34 red)"))

        a = self.KB.kb_ask(read.parse_input("fact: (color box34 ?Y)"))
        self.assertEqual(str(a[0]), "?Y : blue")
        self.assertEqual(str(a[1]), "?Y : red")


        b = self.KB.kb_ask(read.parse_input("fact: (color box34 blue)"))
        self.assertEqual(b[0].bindings, [])

        c = self.KB.kb_ask(read.parse_input("fact: (color box400 blue)"))
        self.assertEqual(c, False)

        print("Test 6 passed!")


    def test7(self):
        self.KB.kb_assert(read.parse_input("fact: (color box37 blue)"))
        self.KB.kb_assert(read.parse_input("fact: (color box37 blue)"))
        self.assertEqual(True, True)
        ask1 = read.parse_input("fact: (color ?X blue)")
        answer = self.KB.kb_ask(ask1)

        self.assertEqual(str(answer[0]), "?X : littlebox")
        self.assertEqual(str(answer[1]), "?X : pyramid1")
        self.assertEqual(str(answer[2]), "?X : box37")

        print("{!r}".format(answer))

class KBTest2(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb2.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)


    def test2_1(self):
        ask1 = read.parse_input("fact: (attacked Ai Nosliw)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(aswer.list_of_bindings[0][1][0], ask1)
        print("test 2_1 passed!")

    def test2_2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)
        print("test 2_2 passed!")

    def test2_3(self):
        a1 = read.parse_input("fact: (inst Harry Wizard)")
        a2 = read.parse_input("fact: (inst Ron Wizard)")
        a3 = read.parse_input("fact: (inst Hermione Sorceress)")
        self.KB.kb_assert(a1)
        self.KB.kb_assert(a2)
        self.KB.kb_assert(a3)

        ask1 = read.parse_input("fact: (inst ?X Wizard)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Harry")
        self.assertEqual(str(answer[1]), "?X : Ron")

        ask2 = read.parse_input("fact: (inst ?X Sorceress)")
        print(' Asking if', ask2)
        answer2 = self.KB.kb_ask(ask2)

        self.assertEqual(str(answer2[0]), "?X : Sarorah")
        self.assertEqual(str(answer2[1]), "?X : Hermione")



        print("test 2_3 passed!")

def test2_4(self):
    ask1 = read.parse_input("fact: (hero ?Y)")
    print(' Asking if', ask1)
    answer = self.KB.kb_ask(ask1)
    self.assertEqual(str(answer[0]), "?Y : Ai")
    print("test 2_4 passed!")


def test2_5(self):
    ask1 = read.parse_input("fact: (color ?X ?Y)")
    print(' Asking if', ask1)
    answer = self.KB.kb_ask(ask1)
    self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : red")
    self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : blue")
    self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : blue")
    self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : green")
    self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : red")
    self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : red")

#assert tests
def test2_6(self):
    self.KB.kb_assert(read.parse_input("fact: (color box34 blue)"))
    self.KB.kb_assert(read.parse_input("fact: (color box34 red)"))

    a = self.KB.kb_ask(read.parse_input("fact: (color box34 ?Y)"))
    self.assertEqual(str(a[0]), "?Y : blue")
    self.assertEqual(str(a[1]), "?Y : red")


    b = self.KB.kb_ask(read.parse_input("fact: (color box34 blue)"))
    self.assertEqual(b[0].bindings, [])

    c = self.KB.kb_ask(read.parse_input("fact: (color box400 blue)"))
    self.assertEqual(c, False)

    print("Test 6 passed!")


def test2_7(self):
    self.KB.kb_assert(read.parse_input("fact: (color box37 blue)"))
    self.KB.kb_assert(read.parse_input("fact: (color box37 blue)"))
    self.assertEqual(True, True)
    ask1 = read.parse_input("fact: (color ?X blue)")
    answer = self.KB.kb_ask(ask1)

    self.assertEqual(str(answer[0]), "?X : littlebox")
    self.assertEqual(str(answer[1]), "?X : pyramid1")
    self.assertEqual(str(answer[2]), "?X : box37")

    print("{!r}".format(answer))



if __name__ == '__main__':
    unittest.main()
