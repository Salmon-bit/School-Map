"""Drawer Module"""
import json
from PySide6.QtGui import QPaintEvent, QPainter #pylint: disable=no-name-in-module
from PySide6.QtWidgets import QWidget #pylint: disable=no-name-in-module
from PySide6.QtCore import QPoint #pylint: disable=no-name-in-module
from web import get_school_floor


class Drawer(QWidget):
    """Class that draws school maps from files"""
    def __init__(self, school: str, floor: int, parent: QWidget | None = None):
        super().__init__(parent)
        self.do_paint = False
        self.school = school
        self.floor = floor

        o = ""
        for i in self.school:
            if i.isdigit():
                o += i
        self.school = o
        get_school_floor(self.school, self.floor)

    def trigger_paint(self):
        """Triggers to paint widget manually"""
        self.do_paint = True
        self.update()

    def paintEvent(self, _event: QPaintEvent) -> None: #pylint: disable=invalid-name
        """Draws school map"""
        if not self.do_paint:
            return

        with QPainter(self) as qp:
            self.draw(qp)

    def draw(self, qp: QPainter):
        """Draw method"""
        with open(f'assets/school_{self.school}_floor_{self.floor}.json', 'r', newline='', encoding='UTF-8') as f: #pylint: disable=line-too-long
            data = json.load(f)
        points = [QPoint(p[0], p[1]) for p in data["points"]]
        qp.drawPolygon(points)
