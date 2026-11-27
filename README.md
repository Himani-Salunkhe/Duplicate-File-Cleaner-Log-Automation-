# Automated Process Logger and Scheduling System

An automated Python utility that recursively scans a directory every minute and creates a timestamped log containing the names of all files found.

## Features

- Recursively scans the selected directory and all subdirectories
- Creates a unique log file for every scheduled scan
- Records file names and the log creation timestamp
- Runs continuously until stopped
- Includes command-line help and usage options

## Requirements

- Python 3
- `schedule` Python package

## Installation

1. Clone or download this repository.

2. Open a terminal in the project directory.

3. Create and activate a virtual environment (recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the required package:

   ```powershell
   python -m pip install -r Requirement.txt
   ```

## Usage

Run the script with the directory that should be scanned:

```powershell
python DirectoryScannerLogUniqueScheduler.py "C:\path\to\directory"
```

The script schedules a scan once every minute. It writes each log file to the current working directory.

### Command-Line Help

Display a short description:

```powershell
python DirectoryScannerLogUniqueScheduler.py --h
```

Display usage instructions:

```powershell
python DirectoryScannerLogUniqueScheduler.py --u
```

Stop the running scheduler with `Ctrl+C`.

## Log File Format

Each log file uses the following naming pattern:

```text
Marvellous<weekday>_<month>_<day>_<time>_<year>.log
```

For example:

```text
MarvellousFri_Nov_27_19_29_23_2026.log
```

The log includes:

- A title and separator lines
- File names found during the recursive directory scan
- The timestamp at which the log was created

## How It Works

The `DirectoryScanner` function uses `os.walk()` to traverse the target directory and write discovered file names to a log file. The `main` function validates command-line arguments and uses the `schedule` package to execute `DirectoryScanner` every minute.

## Project File

- `DirectoryScannerLogUniqueScheduler.py` - Main directory scanning and scheduling script
- `Requirement.txt` - Project requirements file
- `README.md` - Project documentation

## Author

Himani Ramesh Salunkhe