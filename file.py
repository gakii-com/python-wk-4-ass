import os

def modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes to a new file with error handling.
    """
    try:
        # Read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (example: convert to uppercase and add line numbers)
        modified_lines = []
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            modified_line = f"{i}: {line.upper()}"
            modified_lines.append(modified_line)
        
        modified_content = '\n'.join(modified_lines)
        
        # Write to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"\nSuccessfully processed {input_filename} and wrote to {output_filename}")
        print(f"Created file size: {os.path.getsize(output_filename)} bytes")
    
    except FileNotFoundError:
        print(f"\nError: The file {input_filename} was not found.")
    except PermissionError:
        print(f"\nError: Permission denied when accessing {input_filename} or creating {output_filename}")
    except IOError as e:
        print(f"\nError: An IO error occurred - {e}")
    except Exception as e:
        print(f"\nError: An unexpected error occurred - {e}")

def read_file_safely():
    """
    Asks user for a filename and handles potential errors when trying to read it.
    """
    while True:
        filename = input("\nPlease enter the filename you want to read: ")
        
        try:
            # Try to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
            
            # If successful, display first 200 characters and exit loop
            print("\nFile content (first 200 characters):")
            print(content[:200] + ("..." if len(content) > 200 else ""))
            print(f"\nFile size: {os.path.getsize(filename)} bytes")
            break
            
        except FileNotFoundError:
            print(f"\nError: The file '{filename}' doesn't exist.")
        except PermissionError:
            print(f"\nError: You don't have permission to read '{filename}'.")
        except IsADirectoryError:
            print(f"\nError: '{filename}' is a directory, not a file.")
        except UnicodeDecodeError:
            print(f"\nError: Couldn't decode '{filename}' as a text file.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
        
        # Ask if user wants to try again
        choice = input("\nWould you like to try another file? (y/n): ").lower()
        if choice != 'y':
            print("Returning to main menu.")
            break

def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        print("\n=== File Operations Menu ===")
        print("1. Read a file (with error handling)")
        print("2. Modify a file (read, process, and write)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            read_file_safely()
        elif choice == '2':
            print("\n=== File Modification ===")
            input_file = input("Enter input filename: ")
            output_file = input("Enter output filename: ")
            modify_file(input_file, output_file)
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    print("=== File Operations Program ===")
    print("Combined file reader/writer with error handling")
    main_menu()
