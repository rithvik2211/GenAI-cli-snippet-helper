@echo off
if "%1" == "-" (
    set "command=%2"
    if "%command%" == "greet" (
        echo Hello! How can I assist you?
    ) else if "%command%" == "bye" (
        echo Goodbye! Have a great day!
    ) else if "%command%" == "help" (
        echo Available commands:
        echo   greet: Greets the user.
        echo   bye: Says goodbye.
        echo   help: Displays this help message.
    ) else (
        echo Unknown command. Type 'hell - help' for a list of commands.
    )
) else (
    echo Usage: hell - [command]
)
