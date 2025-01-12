from pathlib import Path

path = Path("/").iterdir()

for p in path:
    if p.is_dir():
        print(p)