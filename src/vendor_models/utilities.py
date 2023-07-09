"""Utilities."""

import importlib
from dataclasses import dataclass
from importlib.resources import files as resources_files
from pathlib import Path

from cadquery import Workplane
from cadquery.occ_impl.importers import importStep

from . import resource
from .exceptions import StepImportError


@dataclass
class Metadata:
    """STEP file metadata."""

    resource_path: Path
    doc_url: str
    supplier: str
    part_no: str
    retrieved_url: str


class CqImport:
    """Base class for importing STEP files."""

    path_relative: Path
    doc_url: str
    supplier: str
    part_no: str

    def __init__(self, metadata: Metadata):
        """Initialise metadata."""

        self.path_relative = metadata.resource_path
        self.doc_url = metadata.doc_url
        self.supplier = metadata.supplier
        self.part_no = metadata.part_no
        self.retrieved_url = metadata.retrieved_url

        with importlib.resources.as_file(resources_files(resource)) as root_path:
            self.path = root_path / metadata.resource_path

    def workplane(self) -> Workplane:
        """Import STEP file.

        Import STEP files as CadQuery Workplane.
        """

        workplane = importStep(self.path.as_posix())  # type: ignore[no-untyped-call]

        if not isinstance(workplane, Workplane):
            raise StepImportError

        return workplane

    def step(self) -> str:
        """Get contents of STEP

        :returns: raw STEP file contents as text
        """

        return self.path.read_text()
