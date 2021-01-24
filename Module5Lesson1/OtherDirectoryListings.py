import os
from pathlib import Path


entries = os.listdir("\\Users\Justine\PycharmProjects")
for entry in entries:
    print(entry)
print()

entries = os.scandir("\\Users\Justine\PycharmProjects")
for entry in entries:
    print(entry)
print()

entries = Path("\\Users\Justine\PycharmProjects")
for entry in entries.iterdir():
    print(entry)
