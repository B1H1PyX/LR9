def process_and_write_to_file(input_filename, output_filename, target_length):
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            for line in input_file:
                digits_only = ''.join(char for char in line if char.isdigit())
                padded_line = digits_only.ljust(target_length)
                output_file.write(padded_line + '\n')
        print(f"File '{output_filename}' successfully created.")
    except Exception as e:
        print(f"Error: {e}")
def main():
    input_filename = "TF11_1.txt"
    output_filename = "TF11_2.txt"
    target_length = int(input("Enter the target length for each line: "))

    process_and_write_to_file(input_filename, output_filename, target_length)
if __name__ == "__main__":
    main()