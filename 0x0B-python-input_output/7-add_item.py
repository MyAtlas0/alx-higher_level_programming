#!/usr/bin/python3
"""Add command-line arguments to a Python list and save them to a JSON file."""


import sys
import argparse
import json
import importlib

def main():
    """
    Main function of the script.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Add items to a list and save them to a JSON file.")
    parser.add_argument("items", nargs='*', help="Items to add to the list.")
    args = parser.parse_args()

    # Dynamically import save_to_json_file function from 5-save_to_json_file.py
    save_to_json_file_module = importlib.import_module("5-save_to_json_file")
    save_to_json_file = save_to_json_file_module.save_to_json_file

    # Dynamically import load_from_json_file function from 6-load_from_json_file.py
    load_from_json_file_module = importlib.import_module("6-load_from_json_file")
    load_from_json_file = load_from_json_file_module.load_from_json_file

    # Load existing items from JSON file or create an empty list
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add command-line arguments to the list
    items.extend(args.items)

    # Save the updated list to the JSON file
    save_to_json_file(items, "add_item.json")

    print("Items added successfully.")

if __name__ == "__main__":
    main()
