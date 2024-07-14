from dataclasses import dataclass


FileName = str


@dataclass
class Photo:
    name: FileName
