

import os
import shutil

def view_all_files(path):
    files = os.listdir(path)
    if not files:
        print("files not found")
    else:
        print("All files are listed here: ")
        for file in files:
            print(file)

def create_directory(path):
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"directory {path} exists already.")
    except Exception  as e:
        print(f"An Error occurred : {e}")

def create_file(path):
    try:
        with open(path,'x') as file:
            print(f"file{path} created successfully .")
    except FileExistsError:
        print(f"directory {path} exists already.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(path):
    try:
        with open(path,'r') as file:
            content = file.read()
            print(f"content of {path}: {content}")
    except FileNotFoundError:
        print(f"file {path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(path):
    try:
        with open(path, 'a') as file:
            input_ = input("Enter the content you want to add: ")
            file.write(input_)
            print(f"{path} has been modified successfully.")
    except FileNotFoundError:
        print(f"file {path} not found.")
    except Exception as e:
        print(f"An error occurred")

def delete_file(path):
    try:
        os.remove(path)
        print("file {path} has been removed successfully.")
    except FileNotFoundError:
        print(f"file {path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_directory(path):
    try:
        shutil.rmtree(path)
        print(f"Directory '{path}' and its contents deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def exit_app():
    print("Exiting.....")     

def main():
  while True:
    print("\n--- File Management app ---")
    print("1. View all files")
    print("2. create directory")
    print("3. create a new file ")
    print("4. read a file")
    print("5. edit a file")
    print("6. delete a file")
    print("7. delete a directory")
    print("8. Exit the app")

    choice = input("Enter the choice (1 to 8): ")
    print(f"you chose {choice}")
    if choice == "1":
        path = input("Enter directory path to list files: ")
        view_all_files(path)
    elif choice == "2":
        path = input("Enter directory path to create: ")
        create_directory(path)
    elif choice == "3":
        path = input("Enter file path to create: ")
        create_file(path)
    elif choice == "4":
        path = input("Enter file path to read: ")
        read_file(path)
    elif choice == "5":
        path = input("Enter file path to edit: ")
        edit_file(path)
    elif choice == "6":
        path = input("Enter file path to delete: ")
        delete_file(path)
    elif choice == "7":
       path = input("Enter directory path to delete: ")
       delete_directory(path)
    elif choice  ==  "8":
      break
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
    




