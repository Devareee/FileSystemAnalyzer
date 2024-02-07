import os
import file_system_analyzer as fsa
from test import test_fsa


def prompt():
    # default values of dir and size
    dir = os.getcwd()
    size = 100
    # command receiving cycle
    while True:
        print(f'[{dir}] $ ', end='')
        # split the command by words
        command = input().split()
        if len(command) == 0:
            continue

        # command to change directory for analysis
        elif command[0] == 'dir' and len(command) == 2:
            # check if the path exists
            if os.path.exists(command[1]):
                # check if the path accessible for the current user
                if os.access(command[1], os.R_OK):
                    dir = command[1]
                else:
                    print('Inaccessible directory')
            else:
                print('Directory does not exist')

        # command to get current size threshold
        elif command[0] == 'size' and len(command) == 1:
            print(f'{size} MB')

        # command to change size threshold
        elif command[0] == 'size' and len(command) == 2 and command[1].replace('.', '', 1).isdigit():
            size = float(command[1])

        # command for file type categorization
        elif command[0] == 'ftc' and len(command) == 1:
            fsa.file_type_categorization(dir)

        # command for file type categorization that displays list of files
        elif command[0] == 'ftc' and len(command) == 2 and command[1] == '--full':
            fsa.file_type_categorization(dir, full=True)

        # command for size analysis
        elif command[0] == 'sa' and len(command) == 1:
            fsa.file_type_categorization(dir, calculate_size=True)

        # command for size analysis that displays list of files
        elif command[0] == 'sa' and len(command) == 2 and command[1] == '--full':
            fsa.file_type_categorization(dir, calculate_size=True, full=True)

        # command for file permissions report
        elif command[0] == 'fpr' and len(command) == 1:
            fsa.file_permissions_report(dir)

        # command for large files identification
        elif command[0] == 'lfi' and len(command) == 1:
            fsa.large_files_identification(dir, size)

        # command to finish the program
        elif command[0] == 'exit' and len(command) == 1:
            return

        # help command to display other commands
        elif command[0] == 'help' and len(command) == 1:
            print('dir <your/path/to/dir> - Change directory for analysis\nsize - Current size threshold (MB)\nsize'
                  ' <new_size> - Change size threshold (MB)\nftc - File Type Categorization\n\t--full - print file '
                  'names\nsa - Size Analysis\n\t--full - print file names\nfpr - File Permissions Report\nlfi - '
                  'Large Files Identification\nexit - Exit the program')

        # great error handling :)
        else:
            print('Command not found')


if __name__ == '__main__':
    prompt()
