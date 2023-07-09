"""Waveshare Electronics.

:Website: https://www.waveshare.com/
"""

from pathlib import Path

from .utilities import CqImport, Metadata


class Ddsm115(CqImport):
    """Waveshare DDSM115 hub motor."""

    def __init__(self) -> None:
        """Initialise Waveshare DDSM115."""

        metadata = Metadata(
            resource_path=Path("waveshare/ddsm115.step"),
            supplier="Waveshare",
            part_no="DDSM115",
            doc_url="https://www.waveshare.com/wiki/DDSM115",
            retrieved_url="https://www.waveshare.com/w/upload/c/c9/DDSM115_STEP.zip",
        )

        super().__init__(metadata)
