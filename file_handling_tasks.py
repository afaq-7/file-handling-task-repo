# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

import csv
import json

# Task 1: Create a new text file and write "Hello, world!" to it.
def task1_create_file():
    with open("hello.txt", "w") as file:
        file.write("Hello, world!")

# Task 2: Read the contents of a file and print them to the console.
def task2_read_file():
    with open("hello.txt", "r") as file:
        content = file.read()
        print(content)

# Task 3: Append a new line of text to an existing file.
def task3_append_file():
    with open("hello.txt", "a") as file:
        file.write("\nThis is a new line.")

# Task 4: Count and print the number of lines in a file.
def task4_count_lines():
    with open("hello.txt", "r") as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))

# Task 5: Find whether a specific word exists in the file and how many times.
def task5_find_word():
    word_to_find = "Hello"
    with open("hello.txt", "r") as file:
        content = file.read()
        count = content.count(word_to_find)
        print(f"The word '{word_to_find}' appears {count} times.")

# Task 6: Copy the contents of one file to another.
def task6_copy_file():
    with open("hello.txt", "r") as original_file:
        content = original_file.read()
    with open("copy.txt", "w") as copy_file:
        copy_file.write(content)

# Task 7: Replace a specific word in the file with another word.
def task7_replace_word():
    with open("hello.txt", "r") as file:
        content = file.read()
    new_content = content.replace("Hello", "Hi")
    with open("hello.txt", "w") as file:
        file.write(new_content)

# Task 8: Read a CSV file and print each row.
def task8_read_csv():
    with open("data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Task 9: Write a list of dictionaries to a CSV file.
def task9_write_csv():
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
    with open("people.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "age"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Task 10: Create a JSON file from a Python dictionary and read it back.
def task10_json_file():
    data = {"name": "Alice", "age": 25}
    
    # Write to JSON file
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
    
    # Read from JSON file
    with open("data.json", "r") as json_file:
        loaded_data = json.load(json_file)
        print(loaded_data)
