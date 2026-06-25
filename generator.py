from musicbingo.config import (
    DEFAULT_RANDOM_SEED,
    SONG_DATABASE,
)

from musicbingo.database import load_database


def main() -> None:

    songs = load_database(SONG_DATABASE)

    print(f"{len(songs)} songs loaded.")

    print(f"Seed: {DEFAULT_RANDOM_SEED}")


if __name__ == "__main__":
    main()
