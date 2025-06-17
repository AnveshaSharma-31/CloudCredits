def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File '{filename}' opened successfully.\n")
        return content
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting a new file.\n")
        return ""

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' saved successfully.\n")

def edit_content(current_content):
    print("Enter your text below. Type ':wq' on a new line to save and quit editing.")
    lines = []
    if current_content:
        print("Current content:")
        print(current_content)
        print("---- Start editing ----")
    while True:
        line = input()
        if line == ':wq':
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    filename = input("Enter the filename to open/edit: ").strip()
    content = open_file(filename)
    
    while True:
        print("\nMenu:")
        print("1. Edit")
        print("2. Save")
        print("3. Close")
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == '1':
            content = edit_content(content)
        elif choice == '2':
            save_file(filename, content)
        elif choice == '3':
            print("Closing editor. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
