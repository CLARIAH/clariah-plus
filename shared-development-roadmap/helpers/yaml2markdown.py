#!/usr/bin/env python3

"""
Reads YAML frontmatter in Markdown and outputs it (as markdown) after the next header
"""

import sys
import yaml

def output(metadata):
    print("| key | value |")
    print("| ---------- | ------- |")
    for key, value in metadata.items():
        if isinstance(value, list):
            value = ", ".join([ str(x) for x in value])
        if isinstance(value, dict):
            value = ", ".join([ f"**{k}**: {v}" for k,v in value.items() ])
        print(f"| **{key}** | {value} |")

parse = False
metadata = []
for line in sys.stdin.readlines():
    if line.strip() == "---":
        if parse:
            parse = False
        else:
            parse = True
            metadata = []
    elif parse:
        metadata.append(line.rstrip("\n"))
    elif line.startswith("> "):
        pass
    elif line.startswith("#") and metadata:
        print(line,end="")
        print()
        output(yaml.safe_load("\n".join(metadata)))
        metadata = []
    else:
        print(line,end="")


