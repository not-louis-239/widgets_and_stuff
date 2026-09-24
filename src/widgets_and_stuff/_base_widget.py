# Copyright 2026 Louis Masarei-Boulton

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import annotations
from abc import ABC, abstractmethod

import pygame as pg


class Widget(ABC):
    def __init__(self, *, flex: float = 0.0) -> None:
        self.flex = flex
        self.rect = pg.Rect(0, 0, 0, 0)
        self.children: list[Widget] = []
        self.visible: bool = True
        self.active: bool = False

    @abstractmethod
    def preferred_size(self) -> tuple[int, int]:
        """How big should this UI element be, given no constraints?"""
        raise NotImplementedError

    @abstractmethod
    def layout(self, rect: pg.Rect) -> None:
        """Assign the rect to `self` and divide space between
        any potential children of `self`."""
        raise NotImplementedError
