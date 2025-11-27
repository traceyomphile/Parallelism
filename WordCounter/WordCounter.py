"""
Count the total number of words in a file or in a directory.
Author: Tracey Letlape
Date: 27 November 2025
"""

import os
import multiprocessing
from typing import LiteralString

def _form_file_path(path: list[str]) -> LiteralString:
    """
    Form a file path from the given list.
    Parameters:
        path: A list representing each section of the file path.
    Returns:
        A LiteralString representing a file path.
    """
    file_path = path[0]

    for i in range(1, len(path)):
        file_path = os.path.join(file_path, path[i])
    
    return file_path

def _get_file_paths(directory_path: str) -> list:
    """
    Get all file_paths within a given directory.
    Parameters:
        directory_path: A string representing a directory path.
    Returns:
        A list of of all file paths within the given directory.
    """
    # Get all entries (files and directories)
    entries = os.listdir(directory_path)

    file_paths = []

    for entry in entries:
        # Construct the full path to check if it's a file
        full_path = os.path.join(directory_path, entry)

        # Check if the full path points to a file
        if os.path.isfile(full_path):
            file_paths.append(full_path)
        elif os.path.isdir(full_path):
            sub_file_paths = _get_file_paths(full_path)
            file_paths = file_paths + sub_file_paths
    
    return file_paths

def _is_binary(file_path: str, bytes_to_check: int = 1024) -> bool:
    """
    Checks if a given file is a binary file or not.
    Parameters:
        file_path: A string representing the file path of the file we want to check.
        bytes_to_check: An int representing the number of bytes to check. Default is set to 1024.
    Returns:
        A bool value.
    """
    with open(file_path, 'rb') as f:
        # Read a chunk of the file in binary mode
        chunk = f.read(bytes_to_check)

    if not chunk: return False

    # Count the number of null bytes (b'\x00')
    null_byte_count = chunk.count(b'\x00')
    # Binary if more than 0 null bytes
    return null_byte_count > 0

def _read_and_count(file_path: str) -> int:
    """
    Read and count the number of words in a file.
    Parameters:
        file_path: A string representing the file path of a file.
    Returns:
        A int representing the number of words in that file.
    """
    word_count = 0
    # Skip binary files
    if _is_binary(file_path):
        return word_count
    with open(file_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    return _count_words(lines)

def _count_words(file_lines: list[str]) -> int:
    """
    Count the number of words in a list.
    Parameters:
        file_lines: A list of strings representing lines of a file.
    Returns:
        An int representing the number of words in a file.
    """
    word_count = 0
    for line in file_lines:
        temp = line.split()
        word_count += len(temp)
    return word_count

def word_counter(path: str) -> int:
    """
    Count the number of words in the given path.
    Parameters:
        path: A string representing a file path (or directory path)
    Returns:
        An int representing the number of words in the given path.
    """
    if os.path.isfile(path):
        return _read_and_count(path)
    
    total_words = 0
    file_paths = _get_file_paths(path)
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        counts = pool.map(_read_and_count, file_paths)
        total_words = sum(counts)

    return total_words

def main():
    path = input("Enter the path for the file or directory you want:\n")
    
    if path.__contains__("/"):
        temp = path.split("/")
    else:
        temp = path.split("\\")

    file_path = _form_file_path(temp)

    if not os.path.exists(file_path):
        print(f"File path {file_path} doesn't exist.\nTotal number of words: 0")

    words = word_counter(file_path)
    print(f"Total number of words in {file_path}: {words}")
