# Function to count total lines in a file
def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())


# Get filenames from the user
file1 = input("Enter the first filename: ")
file2 = input("Enter the second filename: ")

# Count lines in both files
lines1 = count_lines(file1)
lines2 = count_lines(file2)

# Display results
print(f"Total lines in '{file1}': {lines1}")
print(f"Total lines in '{file2}': {lines2}")
