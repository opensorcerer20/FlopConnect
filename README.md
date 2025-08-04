## Flop Connect python project

Learn python by writing a script that can calculate how a Texas Hold Em hand connects with the flop via percentage

### Rules

1. To connect, at least one card from the hand must be used
2. If the hand is a pair, it does not count by itself as a "connecting" hand
3. Pairs: one card from the hand has a number that matches at least one on the flop
4. Straights: at least three straight cards must be present, with at least one coming from the hand
5. Flushes: at least three flush cards must be present, with at least one coming from the hand

### Cautions

- Aces are high in non-straight value, but both low and high in straights

### Whether to use actual suits in calculation

Currently up in the air. For fewer calculations I am starting with "matching suit" or "s" and "non-matching suit" or "n"

### Other thoughts
- Perhaps overcards should count as "connecting", e.g. you have an ace in your hand, and the flop has none
