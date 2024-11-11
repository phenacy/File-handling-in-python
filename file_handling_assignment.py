# File Creation
try:
    # Open the file in write mode ('w'), which will create the file
    with open('my_file.txt', 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("Here is the second line with a number: 12345\n")
        file.write("This is the third line, and the number is 67890.\n")
    print("File 'my_file.txt' created and data written successfully.")

except PermissionError:
    print("Error: You do not have permission to write to this file.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")

# File Reading and Display
try:
    # Open the file in read mode ('r') to display its content
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    # Open the file in append mode ('a') to add more content
    with open('my_file.txt', 'a') as file:
        file.write("Appending the fourth line with some more text.\n")
        file.write("This is the fifth line, another number: 24680\n")
        file.write("Here is the sixth line, end of file.\n")
    print("\nThree additional lines appended to 'my_file.txt' successfully.")

except PermissionError:
    print("Error: You do not have permission to append to this file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Final reading to display updated content
try:
    # Read the content of the file after appending
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nUpdated contents of 'my_file.txt':")
        print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file again: {e}")
