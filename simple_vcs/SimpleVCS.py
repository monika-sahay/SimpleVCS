import os
import hashlib
import json
from datetime import datetime
import argparse


class SimpleVCS:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.object_path = os.path.join(repo_path, 'objects')
        self.commits = []

    def init(self):
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)
        if not os.path.exists(self.object_path):
            os.makedirs(self.object_path)
        print(f"Initialized empty repository at {self.repo_path}")


def main():
    parser = argparse.ArgumentParser(description='SimpleVCS - A simple version control system')
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Subparser for init command
    parser_init = subparsers.add_parser('init', help='Initialize a new repository')
    parser_init.add_argument('repo_path', type=str, help='Path to the repository')