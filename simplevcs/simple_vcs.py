# pylint: disable=C0103

"""
simple_vcs.py

A minimalistic version control system.
"""


import os
# import hashlib
# import json
# from datetime import datetime
import argparse


class SimpleVCS:  # pylint: disable=too-few-public-methods
    """
    A simple version control system class.
    """
    def __init__(self, repo_path):
        """
        Initialize the SimpleVCS with a repository path.

        Args:
            repo_path (str): The path to the repository.
        """
        self.repo_path = repo_path
        self.object_path = os.path.join(repo_path, 'objects')
        self.commits = []

    def init(self):
        """
        Initialize a new repository by creating the necessary directories.
        """
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)
        if not os.path.exists(self.object_path):
            os.makedirs(self.object_path)
        print(f"Initialized empty repository at {self.repo_path}")


def main():
    """
    Main function to parse command-line arguments and execute the appropriate commands.
    """
    parser = argparse.ArgumentParser(description='SimpleVCS - A simple version control system')
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Subparser for init command
    parser_init = subparsers.add_parser('init', help='Initialize a new repository')
    parser_init.add_argument('repo_path', type=str, help='Path to the repository')

    args = parser.parse_args()

    if args.command == 'init':
        vcs = SimpleVCS(args.repo_path)
        vcs.init()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
