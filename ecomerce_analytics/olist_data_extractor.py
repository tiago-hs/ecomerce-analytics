import os
from pathlib import Path
from zipfile import ZipFile


class OlistDataExtractor:
    """Procedimento para descompactação dos arquivos de dados."""

    def __init__(
        self, zip_file: str | Path, data_dir: str | Path, output_path: str | Path
    ) -> None:
        self.zip_file = zip_file
        self.data_dir = data_dir
        self.output_path = output_path

    def extract_data(self) -> None:
        print("Extraíndo dados zipados...")
        with ZipFile(os.path.join(self.data_dir, self.zip_file), "r") as data_raw:
            data_raw.extractall(path=os.path.join(self.data_dir, self.output_path))
