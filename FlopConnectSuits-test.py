import unittest
from FlopConnectSuits import checkPairs, checkStraights, checkFlushes, flopHasDuplicateCard, Hand, Flop, Card

class TestFlopConnect(unittest.TestCase):
    def test_checkPairs(self):
        # Check first card in hand matches
        hand = Hand(Card("a", "s"), Card("b", "d"))
        flop = Flop(Card("a", "d"), Card("d", "s"), Card("e", "d"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Check pocket pair matches
        hand = Hand(Card("b", "s"), Card("b", "d"))
        flop = Flop(Card("b", "h"), Card("d", "s"), Card("e", "d"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Check second card in hand matches
        hand = Hand(Card("f", "s"), Card("b", "d"))
        flop = Flop(Card("b", "h"), Card("d", "s"), Card("e", "d"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Test no match
        hand = Hand(Card("f", "s"), Card("g", "d"))
        flop = Flop(Card("b", "d"), Card("d", "s"), Card("e", "d"))
        result = checkPairs(hand, flop)
        self.assertFalse(result)

        # Test pocket pair but no match
        hand = Hand(Card("f", "s"), Card("f", "d"))
        flop = Flop(Card("b", "d"), Card("d", "s"), Card("e", "d"))
        result = checkPairs(hand, flop)
        self.assertFalse(result)

    def test_checkStraights(self):
        # edge case A2 and 789
        # three straight cards on flop, none in hand
        hand = Hand(Card("m", "s"), Card("a", "d"))
        flop = Flop(Card("f", "d"), Card("g", "s"), Card("h", "d"))
        result = checkStraights(hand, flop)
        self.assertFalse(result)

        # test ace low
        hand = Hand(Card("m", "s"), Card("j", "d"))
        flop = Flop(Card("a", "d"), Card("d", "s"), Card("e", "d"))
        result = checkStraights(hand, flop)
        self.assertTrue(result)

        # test ace high
        hand = Hand(Card("m", "s"), Card("a", "d"))
        flop = Flop(Card("a", "h"), Card("i", "s"), Card("l", "d"))
        result = checkStraights(hand, flop)
        self.assertTrue(result)

        # two straight cards in hand
        hand = Hand(Card("i", "s"), Card("j", "d"))
        flop = Flop(Card("a", "d"), Card("b", "s"), Card("k", "d"))
        result = checkStraights(hand, flop)
        self.assertTrue(result)

        # one straight card in hand
        # also tests jack straight; tests that the straight potential goes below jack to 10
        hand = Hand(Card("a", "s"), Card("j", "d"))
        flop = Flop(Card("b", "d"), Card("l", "s"), Card("k", "d"))
        result = checkStraights(hand, flop)
        self.assertTrue(result)


    def test_checkFlushes(self):
        # Test suited hand, one on flop matches
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "d"), Card("d", "s"), Card("e", "d"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # Test one suit in hand, two on flop matches
        hand = Hand(Card("a", "s"), Card("b", "d"))
        flop = Flop(Card("c", "d"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # one suit in hand, three on flop
        hand = Hand(Card("a", "s"), Card("b", "d"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, two on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "d"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, three on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, none on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "d"), Card("d", "d"), Card("e", "d"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)

        # one suit in hand, one on flop
        hand = Hand(Card("a", "s"), Card("b", "d"))
        flop = Flop(Card("c", "s"), Card("d", "d"), Card("e", "d"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)

        # one suit in hand, none on flop
        hand = Hand(Card("a", "s"), Card("b", "d"))
        flop = Flop(Card("c", "d"), Card("d", "d"), Card("e", "d"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)

    def test_flopHasDuplicateCard(self):
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("a", "s"), Card("d", "s"), Card("e", "d"))
        result = flopHasDuplicateCard(hand, flop)
        self.assertTrue(result)

        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("d", "s"), Card("a", "s"), Card("e", "d"))
        result = flopHasDuplicateCard(hand, flop)
        self.assertTrue(result)

        hand = Hand(Card("b", "s"), Card("a", "s"))
        flop = Flop(Card("a", "s"), Card("d", "s"), Card("e", "d"))
        result = flopHasDuplicateCard(hand, flop)
        self.assertTrue(result)

        hand = Hand(Card("a", "s"), Card("a", "h"))
        flop = Flop(Card("a", "d"), Card("d", "s"), Card("e", "d"))
        result = flopHasDuplicateCard(hand, flop)
        self.assertFalse(result)

    # def test_unTranslateHand(self):
    #     result = unTranslateHand("9sAc")
    #     self.assertIsInstance(result, Hand)
    #     self.assertEqual(result.numbers, "hm")
    #     self.assertEqual(result.suits, "sc")

        # result = unTranslateHand("10sAc")
        # self.assertIsInstance(result, Hand)
        # self.assertEqual(result.numbers, "im")
        # self.assertEqual(result.suits, "sc")


# python3 -m FlopConnectSuits-test -v

if __name__ == '__main__':
  unittest.main()
