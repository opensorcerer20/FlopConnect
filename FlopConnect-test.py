import unittest
from FlopConnect import checkPairs, translateCard, checkStraights, checkFlushes, Hand, Flop, Card

class TestFlopConnect(unittest.TestCase):
    def test_checkPairs(self):
        # Check first card in hand matches
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("a", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Check pocket pair matches
        hand = Hand(Card("b", "s"), Card("b", "n"))
        flop = Flop(Card("b", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Check second card in hand matches
        hand = Hand(Card("f", "s"), Card("b", "n"))
        flop = Flop(Card("b", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Test no match
        hand = Hand(Card("f", "s"), Card("g", "n"))
        flop = Flop(Card("b", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertFalse(result)

        # Test pocket pair but no match
        hand = Hand(Card("f", "s"), Card("f", "n"))
        flop = Flop(Card("b", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertFalse(result)

    def test_checkStraights(self):
        # edge case A2 and 789
        # three straight cards on flop, none in hand
        hand = Hand(Card("m", "s"), Card("a", "n"))
        flop = Flop(Card("f", "n"), Card("g", "s"), Card("h", "n"))
        result = checkStraights(hand, flop)
        self.assertFalse(result)

        # test ace low
        hand = Hand(Card("m", "s"), Card("j", "n"))
        flop = Flop(Card("a", "n"), Card("d", "s"), Card("e", "n"))
        result = checkStraights(hand, flop)
        self.assertTrue(result)

        # test ace high
        hand = Hand(Card("m", "s"), Card("a", "n"))
        flop = Flop(Card("a", "n"), Card("i", "s"), Card("l", "n"))
        result = checkStraights(hand, flop)
        self.assertTrue(result)

        # two straight cards in hand
        # hand = Hand(Card("i", "s"), Card("j", "n"))
        # flop = Flop(Card("a", "n"), Card("b", "s"), Card("k", "n"))
        # result = checkStraights(hand, flop)
        # self.assertTrue(result)

        # one straight card in hand
        # hand = Hand(Card("a", "s"), Card("j", "n"))
        # flop = Flop(Card("b", "n"), Card("l", "s"), Card("k", "n"))
        # result = checkStraights(hand, flop)
        # self.assertTrue(result)


    def test_checkFlushes(self):
        # Test suited hand, one on flop matches
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "n"), Card("d", "s"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # Test one suit in hand, two on flop matches
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "n"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # one suit in hand, three on flop
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, two on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, three on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, none on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "n"), Card("d", "n"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)

        # one suit in hand, one on flop
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "s"), Card("d", "n"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)

        # one suit in hand, none on flop
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "n"), Card("d", "n"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)


if __name__ == '__main__':
  unittest.main()
