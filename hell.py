import sys

def greet():
    print("Hello! How can I assist you?")

def bye():
    print("Goodbye! Have a great day!")

def help_command():
    print("Available commands:")
    print("  greet: Greets the user.")
    print("  bye: Says goodbye.")
    print("  help: Displays this help message. from python")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "-":
        print("Usage: hell - [command]")
        return

    command = sys.argv[2]

    if command == 'greet':
        greet()
    elif command == 'bye':
        bye()
    elif command == 'help':
        help_command()
    else:
        print("Unknown command. Type 'hell - help' for a list of commands.")

if __name__ == "__main__":
    main()
