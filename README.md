
## Overview

This Python program provides a menu-driven interface for performing file operations with comprehensive error handling. It combines two main functionalities:
1. Safe file reading with error handling
2. File modification (read, process, and write) capabilities

## Features

- **Menu-driven interface** with clear options
- **Robust error handling** for common file operations
- **File reader** that safely handles various error conditions
- **File modifier** that processes content and writes to new files
- **Cross-platform** compatibility (works on Windows, macOS, Linux)

## Requirements

- Python 3.x
- No additional dependencies required

## Installation

1. Clone or download the repository
2. No installation required - just run the Python file directly

## Usage

Run the program by executing:
```bash
python file_operations.py
```

### Menu Options

1. **Read a file (with error handling)**
   - Safely attempts to read any text file
   - Displays the first 200 characters
   - Shows file size
   - Handles various error conditions gracefully

2. **Modify a file (read, process, and write)**
   - Takes an input file and output file name
   - Processes the content (adds line numbers and converts to uppercase)
   - Creates a new file with modified content
   - Shows success message and output file size

3. **Exit**
   - Cleanly exits the program

## Error Handling

The program handles these common error scenarios:

- File not found
- Permission errors
- Directory specified instead of file
- Unicode decode errors (binary files)
- General I/O errors
- Unexpected errors

## Example Usage

```
=== File Operations Program ===
Combined file reader/writer with error handling

=== File Operations Menu ===
1. Read a file (with error handling)
2. Modify a file (read, process, and write)
3. Exit

Enter your choice (1-3): 1

Please enter the filename you want to read: example.txt

File content (first 200 characters):
1: THIS IS LINE ONE
2: THIS IS LINE TWO
3: THIS IS LINE THREE

File size: 45 bytes
```

## Customization

You can modify the file processing logic in the `modify_file()` function to implement different transformations:

- Change text case (upper/lower/title)
- Search and replace text
- Add different formatting
- Process specific data patterns

