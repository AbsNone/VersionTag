from dataclasses import dataclass
from enum import Enum


FileName = str


class FR(str, Enum):
    CV2 = 'cv2'
    MEDIA_PIPE = 'mediapipe'

@dataclass
class Face:
    method: FR
    label: str
    x: float
    y: float
    w: float
    h: float


@dataclass
class Photo:
    name: FileName
    faces: list[Face]
