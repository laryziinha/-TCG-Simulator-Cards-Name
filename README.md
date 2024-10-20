Pokémon Overhaul for TCG Card Shop Simulator Card Renamer and Renamed Files

This repository contains the corrected files for the Pokémon Overhaul mod for the game TCG Card Shop Simulator version v0.47. All the files have been correctly renamed to ensure the mod works flawlessly. You will find both individual renamed files and a zipped package containing all of them. Additionally, we’ve included a Python script that automates the file renaming process.
Repository Contents

    Individual Files: All the renamed files are available directly in the folder.
    Zipped Package: A zipped file containing all the correctly renamed files.
    Python Script: A script that automates the process of renaming configuration files for the mod using an Excel spreadsheet as input.

Important: Compatibility with More Card Expansions Mod

This script is not limited to the Pokémon Overhaul mod; it works for any card mod that utilizes the More Card Expansions mod. So, you can use this tool to rename files for any card expansion that follows this format, making it a versatile tool for mod creators and users alike.
How the Script Works

The Python script is designed to make the renaming process for mod configuration files easier. Here’s a brief explanation of how it works, aimed at users with no programming experience:
Input

    You need to provide an Excel spreadsheet (.xlsx format) where:
        Column A contains the original names of the files you want to rename.
        Column B contains the new names that you want to assign to the files.

Process

The script reads this spreadsheet and, for each file it finds, it:

    Identifies the original file (using the name from Column A).
    Renames the file to the new name specified (using the name from Column B).
    This process is repeated for all the files listed in the spreadsheet, ensuring that all filenames and their respective mod cards are updated correctly.

Output

    The script automatically updates all the files based on the spreadsheet, generating a new version of each configuration file with the correct card names for the game.

How to Use

    Download the individual files or the zipped package with all the renamed files.
    If you want to rename other files, you can use the Python script:
        Place the files to be renamed and the spreadsheet in the script’s directory.
        Run the script, and it will handle everything for you!

Requirements

    Python 3.x
    Pillow library (for image processing, if needed in future versions)
