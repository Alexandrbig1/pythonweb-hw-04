import asyncio
import shutil
import argparse
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def copy_file(file_path: Path, output_folder: Path):
    try:
        ext = file_path.suffix.lstrip('.') or 'unknown'
        target_dir = output_folder / ext
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / file_path.name

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, shutil.copy2, file_path, target_path)
        logging.info(f"File copied: {file_path} -> {target_path}")
    except Exception as e:
        logging.error(f"error while copying {file_path}: {e}")


async def read_folder(source_folder: Path, output_folder: Path):
    tasks = []
    for file_path in source_folder.rglob('*'):
        if file_path.is_file():
            tasks.append(copy_file(file_path, output_folder))

    if tasks:
        await asyncio.gather(*tasks)
    else:
        logging.warning("Files for processing not found.")


def get_folder_path(prompt: str) -> Path:
    while True:
        path = Path(input(prompt).strip())
        if path.exists() and path.is_dir():
            return path
        logging.error("Entered path not exist or it's not a directory. Try again.")

async def main():
    parser = argparse.ArgumentParser(description="Async sorting of files by extensions.")
    parser.add_argument("source", type=str, nargs="?", help="Output folder with files")
    parser.add_argument("output", type=str, nargs="?", help="Source folder for sorted files")

    args = parser.parse_args()

    source_folder = Path(args.source) if args.source else get_folder_path("Enter the path to output folder: ")
    output_folder = Path(args.output) if args.output else get_folder_path("Enter the path to source folder: ")

    if not source_folder.exists() or not source_folder.is_dir():
        logging.error("Source folder doesn't exist or is not a directory.")
        return

    output_folder.mkdir(parents=True, exist_ok=True)
    await read_folder(source_folder, output_folder)


if __name__ == "__main__":
    asyncio.run(main())