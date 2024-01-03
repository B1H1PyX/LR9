def create_text_file(filename, line_length, num_lines):
    try:
        with open(filename, 'w') as file:
            for _ in range(num_lines):
                line = "1A" * line_length
                file.write(line + '\n')
        print(f"File '{filename}' successfully created.")
    except Exception as e:
        print(f"Error: {e}")
def main():
    filename = "TF11_1.txt"
    line_length = int(input("Enter the length of each line: "))
    num_lines = int(input("Enter the number of lines: "))
    create_text_file(filename, line_length, num_lines)
if __name__ == "__main__":
    main()