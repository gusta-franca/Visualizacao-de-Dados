import pathlib
import zipfile


def unzip_files(src = pathlib.Path("data/raw"), dst = pathlib.Path("data/raw")):
    print(f"Extraíndo arquivos para {dst}...")

    for file_path in src.glob("*.zip"):
        with zipfile.ZipFile(file_path, mode="r") as archive:
            archive.extractall(path = dst)
