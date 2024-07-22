#!/usr/bin/env python3

# export-firefox-extensions Python script
# Copyright (C) 2024 kernaltrap8
# This program comes with ABSOLUTELY NO WARRANTY
# This is free software, and you are welcome to redistribute it
# under certain conditions

import json
import os

def export_firefox_extensions(profile_path, output_file):
    # Path to Firefox profile directory
    extensions_file = os.path.join(profile_path, 'extensions.json')

    # Load the extensions file
    with open(extensions_file, 'r') as file:
        data = json.load(file)

    # Check if 'addons' is present and is a list
    if 'addons' in data and isinstance(data['addons'], list):
        extensions_data = data['addons']
    else:
        raise ValueError("Unexpected data format in extensions.json")

    # Extract extensions info
    extensions_info = []
    for extension in extensions_data:
        if 'id' in extension and 'defaultLocale' in extension:
            extensions_info.append({
                'id': extension['id'],
                'name': extension['defaultLocale'].get('name', 'unknown'),
                'version': extension.get('version', 'unknown')
            })

    # Write to output JSON file
    with open(output_file, 'w') as file:
        json.dump(extensions_info, file, indent=4)

# Example usage
firefox_profile_path = '' # put the path to your profile here (include a leading '/' without quotes)
output_json_file = 'firefox_extensions.json'
export_firefox_extensions(firefox_profile_path, output_json_file)
