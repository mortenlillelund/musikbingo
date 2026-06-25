from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Song:
    title: str
    artist: str
    year: int
    decade: str
    origin: str


@dataclass(slots=True)
class BingoCard:
    number: int
    songs: list[Song]
