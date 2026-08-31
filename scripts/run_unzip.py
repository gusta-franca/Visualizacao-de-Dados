import argparse
import pathlib

from src.unzip import unzip_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage = "run_unzip.py [--src PATH] [--dst PATH]",
        description = "Unzip all .zip files found in a directory"
    )

    parser.add_argument("--src", type = pathlib.Path, default = pathlib.Path("data/raw"))
    parser.add_argument("--dst", type = pathlib.Path, default = pathlib.Path("data/raw"))

    args = parser.parse_args()

    unzip_files(src = args.src, dst = args.dst)
