# Python Yahtzee Dice

#### [Video Demo](https://youtu.be/qDg3Tu0ujMo)

#### Description:

This is my final project for CS50. It's a traditional game of yahtzee dice, made with Python and playable through command line.

The installation is simple:
```
pip install -i https://test.pypi.org/simple/ pyahtzee==0.4.7
```

**How to Play**
To start the game after installation, type `pyahtzee` command to the command line.

Initially, the game will ask if player wants to play the game or not. With the answer `y`, the game will start.

The first thing player will see, after starting the game, is the dice player have rolled. For example:
```
[⚁ 2] [⚁ 2] [⚂ 3] [⚂ 3] [⚄ 5]
```

The game asks player `Do you want to reroll dice?(y/n)`. If player satisfied with your current combination of dice, types `n`, if not - `y`. Player have up to 2 rerolls.

After all rerolls are exhausted or player agreed with rolled dice, the game will provide a list of available combinations with current dice and how much the combination will score. There are two types of combinations:

- upper section (combination for every type of dice). For example `[⚁ 2] [⚁ 2] [⚂ 2] [⚄ 5] [⚄ 5]` has two of those: `twos` (scores 6) and `fives` (scores 10)

- lower section (various poker-themed combinations). For example `[⚁ 2] [⚁ 2] [⚂ 3] [⚂ 3] [⚄ 5]` has three of those: `one pair` (game will select the higher scoring pair - `3` in this example, returning score of 6) , `two pairs` (`2` and `3`, returning score 10) and `chance`, which adds all numbers, returning score 15.

In the game list looks like this:
```
Upper results are:
1. Twos, Score: 4
2. Threes, Score: 6
3. Fives, Score: 5
Lower results are:
1. One Pair, Score: 6
2. Two Pairs, Score: 10
3. Chance, Score: 15
Select section (u / l):
```

After player selects section with `u` for upper or `l` for lower section, and then combinations from list, typing the number for corresponding combination. For example, if player selected lower results with `l`, the next answer `3` will select `Chance` combination and add a score of 15 to players total.

After combination is selected, the game will show current score and what combinations are left. Every combination can be selected only once. After that, the next round starts. There is 14 rounds in the game. If no combinations can be formed with the current dice, the round finishes with zero score and next round starts. Aim of the game is to get the highest possible score.