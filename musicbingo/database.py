from __future__ import annotations

import csv
from pathlib import Path

from .models import Song


def load_database(path: Path) -> list[Song]:
    songs: list[Song] = []

    with path.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            songs.append(
                Song(
                    title=row["title"].strip(),
                    artist=row["artist"].strip(),
                    year=int(row["year"]),
                    decade=row["decade"].strip(),
                    origin=row["origin"].strip(),
                )
            )

    return songs
