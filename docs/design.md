
# Game Design

A hangman like puzzle game for entertainment where the player is guessing the word correctly to be able to eat the
watermelon slices before it runs out. Players older than 15 years who like to challenge themselves in testing their
vocabulary.

### Game Rules

1. The player will have 6 chances to guess a random word pick by the game.
2. Each chance the player has (life) to guess the word is represented by a watermelon slice
3. When the player guesses the correct letter, all the "__" where the letter is, is replaced by the letter itself
4. for each wrong letter guessed, the player will lose a slice (life). Additionally, the game will tell you why the letter inputted was wrong.
5. If there are no watermelon slices left the player loses the game.
6. If the player guesses the word before losing all the lives, they win the game
7. Player can start a new game or end a new game while playing a round.
8. Once a round of the game is finished, the player can choose to start a new game or exit the game.

### Core Features

Features that has to be in the game:
1. The ability to start a new game
2. Length of the word
3. Game tells if the letter exists in the word
4. exiting the game while guessing word
5. requesting a new word

### Stretch Goals

Features that would be nice to have:
1. The app talking to an api from the web to get a random word from it.
2. Chance to enter the entire word for a single chance instead of 6
3. Difficulty levels for a more challenging gameplay or easier levels for casual gameplay.

### Flowchart
![Save_The_Watermelon_Flowchart.Export.svg](flowchart_files/Save_The_Watermelon_Flowchart.Export.svg)

### Data Design

All words used to be guessed will be in a list and the word to be guessed will be stored as a list.

Another list wil be used as the base for the guessing game. it will have the same length as the word but
all characters will be "_". the "_" will be replaced by the letters

Duplicate letters when given as user input will throw error saying that the letter has been already been used to guess.

Variables:
1. `word`: holds the word as a list
2. `visualWord`: a list that has the same length as `word` but all characters shown are "_" unless they were found.
3. `visibleLetters` will be used to track the number of letters visible to the player.
4. `watermelonSlices` will hold how many slices remain.

### Sources
1. [Symbols used in Flowchart](https://www.smartdraw.com/flowchart/flowchart-symbols.htm?srsltid=AfmBOopnj8VhAH3pNCdk65Tsgi4LUFEdzxhhFjXCAr6yDnC71mat-Mrq)
2. [Embed a flowchart](https://www.drawio.com/blog/embed-diagrams-github-markdown)
