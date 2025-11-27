"""
Count the total number of real words in a file or in a directory.
Author: Tracey Letlape
Date: 27 November 2025
"""

import os
import re
import multiprocessing
from typing import LiteralString
from PyPDF2 import PdfReader
import docx
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract


def _read_pdf(file_path: str) -> str:
    text = []
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            extracted = page.extract_text() or ""
            text.append(extracted)
    except Exception:
        pass
    return "\n".join(text)

def _read_docx(file_path: str) -> str:
    try:
        document = docx.Document(file_path)
        return "\n".join([p.text for p in document.paragraphs])
    except Exception:
        return ""
    
def _read_html(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            return soup.get_text(separator=" ")
    except Exception:
        return ""
    
def _read_image(file_path: str) -> str:
    try:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
    except Exception:
        return ""
    
def _read_plain(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""
    
def _extract_text(file_path: str) -> str:
    lower = file_path.lower()

    if lower.endswith(".pdf"):
        return _read_pdf(file_path)
    if lower.endswith(".docx"):
        return _read_docx(file_path)
    if lower.endswith((".html", ".htm")):
        return _read_html(file_path)
    if lower.endswith((".png", ".jpg", ".jpeg")):
        return _read_image(file_path)
    if lower.endswith((".txt", ".md")):
        return _read_plain(file_path)
    
    # For anything readable
    if not _is_binary(file_path):
        return _read_plain(file_path)
    
    return ""

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
    text = _extract_text(file_path)
    tokens = text.split()

    clean_words = [t for t in tokens if re.search(f"[A-Za-z]", t)]

    return len(clean_words)

def word_counter(path: str) -> int:
    """
    Count the number of words in the given path.
    Parameters:
        path: A string representing a file path (or directory path)
    Returns:
        An int representing the number of words in the given path.
    """
    if os.path.isfile(path):
        print("here")
        return _read_and_count(path)
    
    total_words = 0
    print("\nGetting files....")
    file_paths = _get_file_paths(path)
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        counts = pool.map(_read_and_count, file_paths)
        total_words = sum(counts)
    print("\nDone! Counting words...")
    return total_words

def main():
    """Example usage!"""
    file_path = input("Enter the path for the file or directory you want:\n")

    if not os.path.exists(file_path):
        print()
        print(f"File path {file_path} doesn't exist.\nTotal number of words: 0")

    words = word_counter(file_path)
    print()
    print(f"Total number of words in {file_path}: {words}")

if __name__ == '__main__':
    main()
