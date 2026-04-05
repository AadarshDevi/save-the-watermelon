
# Game Design

A hangman like puzzle game for entertainment where the player is guessing the word correctly to be able to eat the
watermelon slices before it runs out. Players older than 15 years who like to challenge themselves in testing their
vocabulary.

### Game Rules

The player will have 6 chances to guess a random word pick by the game. Each chance is represented as a watermelon
slice. When the player guesses the correct word, they win. If there are no watermelon slices left the player loses the game. For each
incorrect letter, the player will lose a watermelon slice but if they guess a letter in the word, the letter is shown
on the spaces where it is.

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

## Progression 2: 