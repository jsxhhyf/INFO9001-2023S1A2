'''
Write your solution for 6. PIAT: Check Setup here.

Author:
SID:
Unikey:
'''
import os.path
from datetime import datetime
from shutil import copy

ROOT_DIR = "/Users/philliphu/Documents/TUTOR/INFO9001/2023S1/Assignment2/"


# you can make more functions or global read-only variables here if you please!

def log(message: str) -> None:
    """
    log message with required timestamp
    Parameters
    ----------
    message : the message to display
    """
    pass


def is_valid_dirpath(path: str) -> bool:
    """
    Determine if a string is a valid absolute directory path.
    Rules for a valid absolute path:
    1. start with '/'
    2. end with '/'
    3. no '.' in the middle
    Parameters
    ----------
    path : str, the string to check

    Returns
    -------
    bool: True if the string is a valid absolute path, otherwise False
    """
    if not path.startswith('/') or not path.endswith('/'):
        return False

    i = 0
    while i < len(path):
        if path[i] == '.':
            return False
        i += 1

    return True


def is_valid_filepath(name: str) -> bool:
    """
    Determine if a string is a valid file name.
    Rules for a valid file name:
    1. start with './'
    2. preceding row is a valid directory (will be checked before this function is called)
    Parameters
    ----------
    name : the file name to check

    Returns
    -------
    bool: True if the string is a valid file name, otherwise False
    """
    return name.startswith('./')


def logging(logs: list, date: str, time: str) -> None:
    '''
    Logging function uses a list of strings to write previous output into a
    log file.
    Parameters:
        logs: list, output from verification/installation in the form of list of 
                    strings to write to logging file.
        date: str,  a string representing the date to generate the necessary 
                    directory date must be in the format YYYY-MM-DD as seen in 
                    the specs (ex: 2023-Mar-03 for March 3rd, 2023).
        time: str,  a string representing the time to generate the log file
                    time must be in the format HH_MM_SS as seen in the specs
                    (ex: 14_31_27 for 14:31:27).
    '''
    pass


def verification(master: str, timestamp: str) -> list:
    '''
    Verification makes sure all files and directories listed in the config file
    are present and match the contents of the master files. 
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the verification process.
    '''

    print(f"{timestamp} Start verification process.")

    # 1. Extract absolute paths to directories from given configuration file
    print(f"{timestamp} Extracting paths in configuration file.")
    total = 0
    dirs = []
    with open(master + "config.txt", "r") as f:
        line = f.readline()[:-1]
        while line:
            if is_valid_dirpath(line):
                total += 1
                dirs.append(line)
            line = f.readline()[:-1]
    print(f"Total directories to check: {total}")

    # 2. Check if directories exist
    print(f"{timestamp} Checking if directories exists.")
    i = 0
    while i < len(dirs):
        if os.path.exists(dirs[i]):
            print(f"{dirs[i]} found!")
        else:
            print(f"{dirs[i]} NOT found!")
        i += 1

    # 3. Extract all absolute paths of all files form given configuration file
    print(f"{timestamp} Extracting files in configuration file.")
    i = 0
    total = 0
    current_folder = ""
    abs_files_list = []
    with open(master + "config.txt", "r") as f:
        line = f.readline()[:-1]
        while line:
            if is_valid_dirpath(line):
                current_folder = line
                total += 1
            elif is_valid_filepath(line):
                abs_path = f"{current_folder}{line[2:]}"
                abs_files_list.append(abs_path)
                print(f"File to check: {abs_path}")
            line = f.readline()[:-1]
        print(f"Total files to check: {total}")

    # 4. Check if files exists
    print(f"{timestamp} Check if files exists.")
    i = 0
    while i < len(abs_files_list):
        if os.path.exists(abs_files_list[i]):
            print(f"{abs_files_list[i]} found!")
        else:
            print(f"{abs_files_list[i]} NOT found!")
        i += 1

    # 5. check contents of each file with those in the master folder
    print(f"{timestamp} Checking contents with master copy.")
    i = 0
    while i < len(abs_files_list):
        subfolder, filename = abs_files_list[i].split('/')[-2:]
        target_file = f"{master}{subfolder}/{filename}"
        src_file = abs_files_list[i]
        try:
            with open(target_file, 'r') as f:
                target = f.read()
            with open(src_file, 'r') as f:
                src = f.read()
        except:
            print("abnormalities detected...")
            return []
        if target == src:
            print(f"{target_file} is same as {src_file}: True")
        else:
            print(f"{target_file} is same as {src_file}: False")
            return []
        i += 1


def installation(master: str, timestamp: str) -> list:
    '''
    Installation copies all required master files into the addresses listed by
    the config file.
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the installation process.
    '''

    print(f"{timestamp} Start installation process.")

    # 1. Extract absolute paths to directories from given configuration file.
    print(f"{timestamp} Extracting paths in configuration file.")
    total = 0
    dirs = []
    with open(master + "config.txt", "r") as f:
        line = f.readline()[:-1]
        while line:
            if is_valid_dirpath(line):
                total += 1
                dirs.append(line)
            line = f.readline()[:-1]
    print(f"Total directories to create: {total}")

    # 2. Create new directories
    print(f"{timestamp} Creat new directories.")
    i = 0
    while i < len(dirs):
        if not os.path.exists(dirs[i]):
            os.makedirs(dirs[i])
            print(f"{dirs[i]} is created successfully.")
        else:
            print(f"{dirs[i]} exists. Skip directory creation.")
        i += 1

    # 3. Extract all absolute paths of files found in the 'master' directory
    print(f"{timestamp} Extracting path of all files in {master}.")
    current_folder = ""
    abs_files = []
    with open(master + "config.txt", "r") as f:
        line = f.readline()[:-1]
        while line:
            if is_valid_dirpath(line):
                current_folder = line
            elif is_valid_filepath(line) and current_folder:
                print(f"Found: {current_folder + line[2:]}")
                abs_files.append(current_folder + line[2:])
            line = f.readline()[:-1]

    # 4. Create new files
    print(f"{timestamp} Create new files.")
    i = 0
    while i < len(abs_files):
        if not os.path.exists(abs_files[i]):
            print(f"Creating file: {abs_files[i]}")
            f = open(abs_files[i], 'w')
            f.close()
        i += 1

    # 5. Copy files from 'master' directory accordingly
    print(f"{timestamp} Copying new files.")
    i = 0
    while i < len(abs_files):
        subfolder, filename = abs_files[i].split('/')[-2:]
        origin = f"{master}{subfolder}/{filename}"
        print(f"Locating: {filename}")
        try:
            copy(origin, abs_files[i])
            print(f"Original path: {origin}")
        except FileNotFoundError:
            print(f"Original path: {origin} is not found.")
            return []
        print(f"Destination path: {abs_files[i]}")
        i += 1

    print(f"{timestamp} Installation complete.")
    return []


def main(master: str, flags: str, timestamp: str):
    '''
    Ideally, all your print statements would be in this function. However, this is
    not a requirement.
    Parameters:
        master:    str, a string representing the absolute path to the master directory.
        flags:     str, a string representing the specified flags, if no flag is given
                        through the command line, flags will be an empty string.
        timestamp: str, a string representing the time to insert into the output.
                    in the format: DD MMM YYYY HH:MM:DD , ex: 10 Apr 2023 12:44:17
    '''
    pass


if __name__ == "__main__":
    # you will need to pass in some arguments here
    # we will leave this empty for you to handle the implementation

    # define the timestamp
    timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S ")
    # main()
    # installation(ROOT_DIR + "master/", timestamp)
    verification(ROOT_DIR + "master/", timestamp)
