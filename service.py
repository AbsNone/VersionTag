from dataclasses import dataclass


FileName = str


@dataclass
class Face:
    x: float
    y: float
    w: float
    h: float


@dataclass
class Photo:
    name: FileName
    faces: list[Face]
