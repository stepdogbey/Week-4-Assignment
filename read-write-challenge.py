# Function to read from a file, modify content, and write to a new file
def modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., converting text to uppercase)
        modified_content = content.upper()

        # Open the output file for writing
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_filename}' has been read and modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: An I/O error occurred while reading or writing to files.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
input_filename = "example.txt"
output_filename = "modified_example.txt"
modify_file(input_filename, output_filename)
