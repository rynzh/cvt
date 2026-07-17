from pathlib import Path

from torch.utils.data import Dataset


class ImageDataset(Dataset):
    def __init__(self, data_dir: str | Path) -> None:
        self.data_dir = Path(data_dir)
        self.samples: list[Path] = []

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, index: int):
        raise NotImplementedError
