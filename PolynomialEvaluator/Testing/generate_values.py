"""
@author ChatGPT
"""

import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to values.txt inside that same directory
output_path = os.path.join(script_dir, "values.txt")

with open(output_path, "w") as f:
    for i in range(-50000, 50001):
        f.write(f"{i}\n")
