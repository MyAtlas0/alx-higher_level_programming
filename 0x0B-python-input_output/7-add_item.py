#!/usr/bin/python3
"""Add command-line arguments to a Python list and save them to a JSON file."""


import sys
import argparse
import json
import importlib

# Dynamically import the save_to_json_file and load_from_json_file functions
save_to_json_file_module = importlib.import_module("5-save_to_json_file")
load_from_json_file_module = importlib.import_module("6-load_from_json_file")

save_to_json_file = save_to_json_file_module.save_to_json_file
load_from_json_file = load_from_json_file_module.load_from_json_file

def add_arguments_to_list(items, *arguments):
    """
    Add command-line arguments to the given list.

    Args:
        items (list): The list to which arguments will be added.
        arguments (list): List of arguments to be added.
    """
    items.extend(arguments)

def main():
    """Main function of the script."""
    parser = argparse.ArgumentParser(description="Add items to a list and save them to a JSON file.")
    parser.add_argument("filename", help="The JSON file to save the items to.", default="add_item.json", nargs='?')
    parser.add_argument("items", nargs=argparse.REMAINDER, help="Items to add to the list.")
    args = parser.parse_args()

    try:
        items = load_from_json_file(args.filename)
    except FileNotFoundError:
        items = []

    add_arguments_to_list(items, *args.items)

    save_to_json_file(items, args.filename)
    print("Items added successfully.")

if __name__ == "__main__":
    main()
