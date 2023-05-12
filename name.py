'''
Answer for Question 5. Kids' Friendly.

Author:
SID:
Unikey:
'''

import os

# you can make more functions or global read-only variables here if you please!

'''
This part should be your solution from Assignment 1, 3. Functions.
'''


def player_name():
    # Name input
    player_input = input("What's ye name, Hunter?\n")
    return player_input


def is_valid_length(name: str) -> bool:
    return len(name) >= 1 and len(name) <= 9


def is_valid_start(name: str) -> bool:
    return len(name) == 0 or name[0].isalpha()


def is_one_word(name: str) -> bool:
    i = 0
    while i < len(name):
        if name[i] == ' ':
            return False
        i += 1
    return True


def is_valid_name(name: str) -> bool:
    return is_valid_length(name) and is_valid_start(name) and is_one_word(name) and not is_profanity(name)


def is_profanity(word: str, database='files/list.txt', records='files/history.txt') -> bool:
    """
    Checks if `word` is listed in the blacklist `database`.
    Parameters:
        word:     str,  word to check against database.
        database: str,  absolute directory to file containing list of bad words.
        records:  str,  absolute directory to file to record past offenses by player.
    Returns:
        result:   bool, status of check.
    """

    # check if the name is found in database
    if not os.path.exists(database):
        print("Check directory of database!")
        return False

    with open(database, 'r') as f:
        bad_names = f.read().split('\n')

    i = 0
    while i < len(bad_names):
        if word.strip().lower() == bad_names[i]:
            with open(records, 'a') as f:
                f.write(bad_names[i] + '\n')
            return True
        i += 1


def count_occurrence(word: str, file_records="/home/files/history.txt", start_flag=True) -> int:
    """
    Count the occurrences of `word` contained in file_records.
    Parameters:
        word:         str,  target word to count number of occurences.
        file_records: str,  absolute directory to file that contains past records.
        start_flag:   bool, set to False to count whole words. True to count words
                            that start with.
    Returns:
        count:        int, total number of times `word` is found in the file.
    """
    if not isinstance(word, str) or not word[0].isalpha():
        print("First argument must be a string object!")
        return 0

    if len(word) == 0:
        print("Must have at least one character in the string!")
        return 0

    if not os.path.exists(file_records):
        print("File records not found!")
        return 0

    with open(file_records, 'r') as f:
        word_list = f.read().split('\n')[:-1]

    count = 0
    i = 0
    while i < len(word_list):
        if start_flag:
            if word_list[i].strip().lower().startswith(word[0].strip().lower()):
                count += 1
        else:
            if word_list[i].strip().lower() == word.strip().lower():
                count += 1
        i += 1

    return count


def generate_name(word: str, src="files/animals.txt", past="files/names.txt") -> str:
    """
    Select a word from file `src` in sequence depending on the number of times word occurs.
    Parameters:
        word:     str, word to swap
        src:      str, absolute directory to file that contains safe in-game names
        past:     str, absolute directory to file that contains past names
                       auto-generated
    Returns:
        new_name: str, the generated name to replace word
    """

    # some validations
    if not isinstance(word, str) or not word[0].isalpha():
        print("First argument must be a string object!")
        return "Bob"

    if len(word) == 0:
        print("Must have at least one character in the string!")
        return "Bob"

    if not os.path.exists(src):
        print("Source file not found!")
        return "Bob"

    new_name = ""
    last_replaced_word = ""
    found_last_word = False

    with open(src, 'r') as f:
        replace_names = f.read().split('\n')[:-1]

    if os.path.exists(past):
        with open(past, 'r') as f:
            past_names = f.read().split('\n')[:-1]

        # get the last replaced word with the same initial
        idx = len(past_names) - 1
        while idx >= 0:
            if past_names[idx].startswith(word.strip().lower()[0]):
                last_replaced_word = past_names[idx]
                break
            idx -= 1

    if len(last_replaced_word) == 0:
        found_last_word = True
    i = 0
    while i < len(replace_names):
        if replace_names[i].strip().lower().startswith(word.strip().lower()[0]):
            if found_last_word:
                new_name = replace_names[i]
                with open(past, 'a') as f:
                    f.write(new_name + '\n')
                break
            if replace_names[i].strip().lower() == last_replaced_word:
                found_last_word = True
        i += 1

    # if still not found a proper name within the first round of loop
    # it means the first replacement name with the same initial should be used
    if len(new_name) == 0 and found_last_word:
        i = 0
        while i < len(replace_names):
            if replace_names[i].strip().lower().startswith(word.strip().lower()[0]):
                new_name = replace_names[i]
                with open(past, 'a') as f:
                    f.write(new_name + '\n')
                break
            i += 1
    return new_name


def main():
    while True:
        user_input = input("Check name: ")
        if user_input == "s":
            break
        if is_valid_name(user_input):
            print(f"{user_input} is a valid name!")
        else:
            print(f"Your new name is: {generate_name(user_input)}")


if __name__ == "__main__":
    main()
