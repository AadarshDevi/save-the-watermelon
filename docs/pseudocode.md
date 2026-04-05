
# Pseudocode

## game.py

This is the game loop where the game will run forever till the user asks to exit the game.

```
FUNCTION game_loop

    create constant WordLoader object
    create constant GameLogic object
    
    running is true
    restart_game is true
    
    WHILE game is runnng
    
        IF restart_game
            reset method in GameLogic object
        ENDIF
        
        print_slices(get slice count from GameLogic)
        print visual_word
        
        get input from user
        
        get is_valid_user_input from valid_user_input in GameLogic
        
        IF is not a valid user input
            print the error message in is_valid_user_input
        ENDIF
        
        get is_valid_letter from check_letter in GameLogic
        IF word does not have letter
            print saying letter does not exist
            reduce slice count in GameLogic obj
            print that the letter is not there
            continue to next iteration of loop
        ENDIF
        print that the letter was found in the word
        update the visual_word in GameLogic
        
        get game_over from check_game_over, GameLogic
        IF game_over
            ask user if they want to continue guessing words
            IF they say yes
                restart_game is true
            ELSE
                running is false
        ENDIF

    ENDWHILE
ENDFUNCTION

FUNCTION print_slices(slice count)
    COMMENT
        each line of the art is a seperate print so * num can be used to print the same text on same line
    ENDCOMMENT
    
    ascii art or watermelon slice visual line 0 * slice count
    ascii art or watermelon slice visual line 1 * slice count
    ...
    ascii art or watermelon slice visual line n * slice count
ENDFUNCTION

```

## logic.py

```
CLASS GameLogic

    FUNCTION __init__(self, slices, word)
        set self.__slices to have 6
        set the __word to word
        set the __visual_word to have the correct amount of "_"
        set visible_letters to length of word
        set a list of letters entered __letters_entered
    ENDFUNCTION
    
    FUNCTION reset_game_logic
        set self.__slices to have 6
        set the __word to empty
        set the __visual_word to have the correct amount of "_"
        set visible_letters to length of word
        set a list of letters entered __letters_entered
    ENDFUNCTION
    
    FUNCTION set_new_word(word)
        set the __word to word
    ENDFUNCTION
    
    FUNCTION get_hint
        IF visible_letters length == length of word
            return false with word is already found
        ENDIF
        
        validHint is false
        WHILE not validHint
            get randon num between 0 and length
            IF char in __visual_word is "_"
                replace "_" at index
                validHint is true
                continue to next iteratation of loop
            ENDIF
        ENDWHILE
        return true and tell that a hint was given
    ENDFUNCTION
    
    FUNCTION check_letter
        IF letter is in __letters_entered
            return false with error message saying letter already shown
        ENDIF
        
        contains_letter is false
        FOR letter in word
            IF word has letter
                replace "_" with letter
                increment visible_letters
                contains_letter is true
                IF letter is not in __letters_enterd
                    add letter to __letters_enterd
                ENDIF 
            ENDIF
        ENDFOR
        return contains_letter
    ENDFUNCTION
    
    FUNCTION check_game_over
        IF visible_letters length == length of word
            return true
        ENDIF
        return false
    ENDFUNCTION
    
    FUNCTION update_visual_word
        FOR letter in word
            IF guess_letter is same as letter 
                get word_letter at letter_index of the list word
                IF word_letter is "_"
                    replace "_" with the guess letter
                    increment visible letters
                ENDIF
            ENDIF
        ENDFOR
    ENDFUNCTION
    
    FUNCTION valid_user_input
        IF user_input string length is not 1
            return false and an error text saying input is not a string with a single letter
        ENDIF
            
        IF user_input is not a letter
            return false and an error text saying character can only be a letter
        ENDIF
        return true with text saying input is valid (debugging purpose only)
    ENDFUNCTION
    
ENDCLASS
```

## words.py

```
__words_in_file, list of words from file
__word_index is 0

CLASS WordLoader
    
    FUNCTION __init__(self, slices)
        set __words_list as empty list
    ENDFUNCTION
    
    FUNCTION read_words(filepath)
        reset __words_list by making it empty
        get file and read it line by line
            IF word is not empty
                add it to a list
            ENDIF
            
        close file
        give the words_in_file list
    ENDFUNCTION
    
    FUNCTION get_new_word
        get a psuedo random int in range of 0 to length of __words_list 
        get a word from __words_list at the index of the pseudo random int
        increment the __word_index
        IF word is empty
            give None
        ENDIF
        give the word
    ENDFUNCTION
ENDCLASS
```

# Sources
1. [How to write Pseudo Code (Geeks for Geeks)](https://www.geeksforgeeks.org/dsa/what-is-pseudocode-a-complete-tutorial/)
2. [Reading a file line by line is Python STDLIB (Geeks for Geeks)](https://www.geeksforgeeks.org/python/how-to-read-from-a-file-in-python/)
3. [How to check if a string is empty (Geeks for Geeks)](https://www.geeksforgeeks.org/python/python-program-to-check-if-string-is-empty-or-not/)
4. [How to write private variables (Course Lecture: Properties)](https://github.com/d-khan/python/blob/main/OOP/3%20Properties.md)