# File System Analyzer

## A command-line tool that analyzes and reports on the file system structure and usage on a Linux system.

The tool is able to traverse through a specified directory recursively and classify files into categories (executable, image, text, archives, sound, video, other) based on their extensions. It can calculate and display the total size for each file type category. Also the tool is able to generate a report of files with unusual permission settings (world-writable files) and identify and list files above a certain size threshold.

The tool has a simple command-line interface where users can specify the directory to be analyzed and set parameters like size threshold.

Open in [Google Colab](https://colab.research.google.com/drive/1YDudONznX1BpkEsl2Qfo2lOwiExTBPLT?usp=drive_link).

### Prerequisites
Linux or Windows OS. Python3.x

### Install

Clone this repository: 
```
git clone https://github.com/Devareee/FileSystemAnalyzer.git
```
CD into this repository: 
```
cd FileSystemAnalyzer
```
Run the tool:
```
python3 main.py
```

### Command description
- **_dir <your/path/to/dir>_** (_string_): Changes the directory to be analyzed. Default: `current directory`.

- **_size_**: Displays current size threshold (MB).

- **_size <new_size>_** (_int or float_): Changes the current size threshold (MB). Default: `100`.

- **_ftc_**: File Type Categorization. Classifies files into categories (executable, image, text, archives, sound, video, other) based on their extensions. Shows amount of files in each category. `--full` Displays all files in each category.

- **_sa_**: Size Analysis. Calculates and displays the total size for each file type category. `--full` Displays all files in each category.

- **_fpr_**: File Permissions Report. Generates a report of files with unusual permission settings (world-writable files). Displays all the unusual files and their permissions.

- **_lfi_**: Large Files Identification. Identifies and lists files above a `size` threshold. Displays all the large files and their sizes.

- **_exit_**: Exit the program.

- **_help_**: Help command to display other commands.

### Test Cases
test.py consists of 4 unit tests for the main functions.
Run the unit tests:
```
python3 test.py
```