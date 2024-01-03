def print_file_content(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Error: {e}")
def main():
    input_filename = "TF11_2.txt"
    print("Contents of TF11_2 file:")
    print_file_content(input_filename)
if __name__ == "__main__":
    main()