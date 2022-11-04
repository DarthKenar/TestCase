from unittest import TestCase, main
from main import Solution as S
class TestString(TestCase):
    
    def upperNextToLowerTest(self):
        self.assertEqual(S.upperNextToLower("ahjJa"),[2,3])
        self.assertEqual(S.upperNextToLower("aasdDknpqn"),[3,4])
        self.assertEqual(S.upperNextToLower("aAsdDknpqn"),[0,1])
        self.assertEqual(S.upperNextToLower("aasdkKJnpqn"),[4,5])
        self.assertEqual(S.upperNextToLower("aasdaknpqnN"),[9,10])
        self.assertEqual(S.upperNextToLower("apsS"),[2,3])
        self.assertEqual(S.upperNextToLower("AasdDknpqn"),[0,1])

        self.assertIsNone(S.upperNextToLower("aasdgknpqn"))
        self.assertIsNone(S.upperNextToLower(""))
        self.assertIsNone(S.upperNextToLower("E"))

if __name__ == "__main__":
    main()





