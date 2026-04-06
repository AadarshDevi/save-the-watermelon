# Test Plans

## User Input

|     Input Type     |          Theoretical Result           |                       Actual Result                       | Result |
|:------------------:|:-------------------------------------:|:---------------------------------------------------------:|:------:|
|       empty        | tell player that text cannot be empty |     ![img.png](test_imgs/user_input/empty_input.png)      |   ✅    |
| not single letter  | tell player to enter a single letter  |   ![img.png](test_imgs/user_input/too_many_letters.png)   |   ✅    |
|   single symbol    | tell player to enter a single letter  |    ![img.png](test_imgs/user_input/single_symbol.png)     |   ✅    |
|  multiple symbols  | tell player to enter a single letter  |  ![img_1.png](test_imgs/user_input/multiple_symbols.png)  |   ✅    |
|   single number    | tell player to enter a single letter  |   ![img_2.png](test_imgs/user_input/single_number.png)    |   ✅    |
|  multiple numbers  | tell player to enter a single letter  |  ![img_3.png](test_imgs/user_input/multiple_numbers.png)  |   ✅    |
|    valid option    |   process the option and execute it   |  ![img.png](test_imgs/user_input/valid_game_option.png)   |   ✅    |
|   invalid option   | tell user that the option is invalid  | ![img.png](test_imgs/user_input/invalid_game_option.png)  |   ✅    |
|   letter in word   |    tell user if it is in the word     |   ![img_4.png](test_imgs/user_input/letter_in_word.png)   |   ✅    |
| letter not in word |  tell user if it is not in the word   | ![img_5.png](test_imgs/user_input/letter_not_in_word.png) |   ✅    |
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
