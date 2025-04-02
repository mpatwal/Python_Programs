def compare_files(file1, file2):
    try:
        # Open the first file and read lines
        with open(file1, 'r') as fil1:
            lines1 = fil1.readlines()

        # Open the second file and read lines
        with open(file2, 'r') as fil2:
            lines2 = fil2.readlines()

        # Compare the files
        if lines1 == lines2:
            print("Both files are identical.")
        else:
            print("The files are different.")

        # Display the total number of lines in each file
        print(f"Total number of lines in {file1}: {len(lines1)}")
        print(f"Total number of lines in {file2}: {len(lines2)}")

    except FileNotFoundError as e:
        print(f"Error: {e}")


# Taking input from the user for file names
file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")

compare_files(file1, file2)
