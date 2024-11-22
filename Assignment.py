def read_and_modify_file():
    import os

    # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")

    try:
        # Attempt to open the input file
        with open(input_file, "r") as file:
            content = file.read()  # Read the entire content
            print("Original Content:")
            print(content)

            # Modify the content (convert to uppercase as an example)
            modified_content = content.upper()

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return
    except IOError:
        print(f"Error: Unable to read the file '{input_file}'.")
        return

    # Ask the user for the output filename
    output_file = input("Enter the name of the file to write the modified content: ")

    try:
        # Attempt to write the modified content to a new file
        with open(output_file, "w") as file:
            file.write(modified_content)
            print(f"Modified content successfully written to '{output_file}'.")
    except IOError:
        print(f"Error: Unable to write to the file '{output_file}'.")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
