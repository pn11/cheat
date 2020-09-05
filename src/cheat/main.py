"""Primary application entrypoint.
"""
import argparse
import json
import os
import pathlib
import site
import sys

cheat_dir = str(pathlib.Path.home())+'/.cheatsheet/'
ext_list = ['', '.md', '.txt', '.rst']
aliases = {'dired': 'emacs-dired'}

def _display_cheat_sheet(cheat_name: str):
    cheat_name = aliases.get(cheat_name, cheat_name)
    filenames = [f"{cheat_dir}/{cheat_name}{ext}" for ext in ext_list]

    for name in filenames:
        if os.path.exists(name):
            with open(name) as f:
                print(f.read())
                return 0
    print('Error: No such cheat sheet.', file=sys.stderr)
    return -1


def _list_sheets():
    li = os.listdir(cheat_dir)
    for file in li:
        print(file)
    print('Aliases:')
    for k, v in aliases.items():
        print(f'{k} -> {v}')

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('cheat_name', help='name of a cheat sheet (put list to display cheetsheets)')
    args = parser.parse_args()
    if args.cheat_name == 'list':
        _list_sheets()
    else:
        _display_cheat_sheet(args.cheat_name)

    return None
