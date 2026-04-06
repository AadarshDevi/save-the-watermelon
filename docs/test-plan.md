# Test Plans

## User Input

Steps:
1. I started the game and entered various user inputs: "", ax, !, !@, 1, 194, -n, -x, a, a then a (giving same letter), x
2. I check the result (actual result) with the supposed to be result
3. I then checked if both the results were the intended and same

|            Input Type             |                 Theoretical Result                  |                          Actual Result                          | Result |
|:---------------------------------:|:---------------------------------------------------:|:---------------------------------------------------------------:|:------:|
|               empty               |        tell player that text cannot be empty        |        ![img.png](test_imgs/user_input/empty_input.png)         |   ✅    |
|         not single letter         |        tell player to enter a single letter         |      ![img.png](test_imgs/user_input/too_many_letters.png)      |   ✅    |
|           single symbol           |        tell player to enter a single letter         |       ![img.png](test_imgs/user_input/single_symbol.png)        |   ✅    |
|         multiple symbols          |        tell player to enter a single letter         |     ![img_1.png](test_imgs/user_input/multiple_symbols.png)     |   ✅    |
|           single number           |        tell player to enter a single letter         |      ![img_2.png](test_imgs/user_input/single_number.png)       |   ✅    |
|         multiple numbers          |        tell player to enter a single letter         |     ![img_3.png](test_imgs/user_input/multiple_numbers.png)     |   ✅    |
|           valid option            |          process the option and execute it          |     ![img.png](test_imgs/user_input/valid_game_option.png)      |   ✅    |
|          invalid option           |        tell user that the option is invalid         |    ![img.png](test_imgs/user_input/invalid_game_option.png)     |   ✅    |
|          letter in word           |           tell user if it is in the word            |      ![img_4.png](test_imgs/user_input/letter_in_word.png)      |   ✅    |
| entering a letter already entered | the word already has been entered. try a new letter | ![img_4.png](test_imgs/user_input/duplicate_letter_entered.png) |   ✅    |
|        letter not in word         |         tell user if it is not in the word          |    ![img_5.png](test_imgs/user_input/letter_not_in_word.png)    |   ✅    |


## Slices Count

|            Input Type             |       Theoretical Result       |                          Actual Result                           | Result |
|:---------------------------------:|:------------------------------:|:----------------------------------------------------------------:|:------:|
|               empty               |  player does not lose slices   |        ![img.png](test_imgs/slice_count/empty_input.png)         |   ✅    |
|         not single letter         |  player does not lose slices   |     ![img_2.png](test_imgs/slice_count/multiple_letters.png)     |   ✅    |
|           single symbol           |  player does not lose slices   |      ![img_3.png](test_imgs/slice_count/single_symbol.png)       |   ✅    |
|         multiple symbols          |  player does not lose slices   |     ![img_4.png](test_imgs/slice_count/multiple_symbols.png)     |   ✅    |
|           single number           |  player does not lose slices   |      ![img_5.png](test_imgs/slice_count/single_number.png)       |   ✅    |
|         multiple numbers          |  player does not lose slices   |         ![img_6.png](test_imgs/slice_count/multiple.png)         |   ✅    |
|           valid option            |  player does not lose slices   |       ![img_7.png](test_imgs/slice_count/valid_option.png)       |   ✅    |
|          invalid option           |  player does not lose slices   |      ![img_8.png](test_imgs/slice_count/invalid_option.png)      |   ✅    |
|          letter in word           |  player does not lose slices   |      ![img_1.png](test_imgs/slice_count/letter_in_word.png)      |   ✅    |
| entering a letter already entered | tell user if it is in the word | ![img_4.png](test_imgs/slice_count/duplicate_letter_entered.png) |   ✅    |
|        letter not in word         |      player loses slices       |    ![img_9.png](test_imgs/slice_count/letter_not_in_word.png)    |   ✅    |

## Game Features

|            Feature Name             |                                         Trigger                                          |                Theoretical Result                 |                          Actual result                          |
|:-----------------------------------:|:----------------------------------------------------------------------------------------:|:-------------------------------------------------:|:---------------------------------------------------------------:|
|           New Game Option           |                           Using game option [-n] as user input                           |       a new word will be used to be guessed       |  ![img.png](test_imgs/game_features/new_game_game_option.png)   |
|           End Game Option           |                           Using game option [-e] as user input                           |  the game will thank the player before quitting   | ![img_1.png](test_imgs/game_features/exit_game_game_option.png) |
| New Game (After completing a round) | A question will ask if player wants to play again if they win or lose, enter [Y] for yes | a new round of the game will bein with a new word | ![img_2.png](test_imgs/game_features/new_game_after_round.png)  |
| New Game (After completing a round) | A question will ask if player wants to play again if they win or lose, enter [n] for no  | a new round of the game will bein with a new word | ![img_3.png](test_imgs/game_features/exit_game_after_round.png) |