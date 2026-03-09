from glob import glob
import shutil
from pathlib import Path

all_files = glob("*_cands/*.csv")

all_seats = set()
for file in all_files:
    with open(file, "r") as f:
        first_line = f.readline()
        n_seats = first_line.strip().split(",")[1]
        all_seats.add(n_seats)

seats_to_files = {n_seats: [] for n_seats in sorted(all_seats)}
for file in all_files:
    with open(file, "r") as f:
        first_line = f.readline()
        n_seats = first_line.strip().split(",")[1]
        seats_to_files[n_seats].append(file)

for n_seats, files in seats_to_files.items():
    out_folder = Path(f"{n_seats}_seats")
    out_folder.mkdir(exist_ok=True)
    for file in files:
        shutil.copy2(file, out_folder / Path(file).name)
