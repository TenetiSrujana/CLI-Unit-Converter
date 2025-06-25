# CLI Unit Converter

A simple command-line tool to convert temperatures between Celsius and Fahrenheit using Python. Built with argparse for easy and user-friendly command-line options.

## Features

- Convert Celsius to Fahrenheit  
- Convert Fahrenheit to Celsius  
- Clear, helpful command-line interface  

## How to Run in VS Code

1. Open VS Code and open your project folder (for example, `~/projects`).

2. Open the terminal in VS Code (`Ctrl + \`` or go to `View > Terminal`).

3. Create your project folder and navigate into it:

   ```bash
   mkdir -p ~/projects
   cd ~/projects
   ```
4. 4. Create your Python script with nano editor:
   ```bash
   nano converter.py
   
Paste your Python code, then save and exit nano by pressing:

. Ctrl + X
. Then Y to confirm save
. Then Enter to exit

6. Usage Examples:
```bash
python converter.py --celsius 25
# Output: 25.0°C is 77.00°F

python converter.py --fahrenheit 77
# Output: 77.0°F is 25.00°C

   
