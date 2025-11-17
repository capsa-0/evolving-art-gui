"""Shared helpers for application screens."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

from src.app.theme import VisualConfig


@dataclass(frozen=True)
class ScreenPalette:
    """Centralized color palette for top-level screens."""

    background: str = "#1a1a1a"
    panel_background: str = "#191919"
    border: str = "#2d2d2d"
    primary_text: str = "#f0f0f0"
    secondary_text: str = "#b0b0b0"
    tertiary_text: str = "#777777"
    accent: str = VisualConfig.color_accent

    def hover(self, lighten_factor: int = 125) -> str:
        """Return a lighter version of the accent suitable for hover states."""
        return QColor(self.accent).lighter(lighten_factor).name()


def build_outline_button_style(
    palette: ScreenPalette,
    *,
    thickness: int = 2,
    padding: str = "9px 20px",
    radius: int = 8,
    font_size: str = "14px",
    font_weight: str = "600",
) -> str:
    """Return a reusable stylesheet for outlined accent buttons."""

    return f"""
    QPushButton {{
        font-size: {font_size};
        font-weight: {font_weight};
        color: {palette.accent};
        background-color: transparent;
        border: {thickness}px solid {palette.accent};
        border-radius: {radius}px;
        padding: {padding};
    }}
    QPushButton:hover {{
        background-color: {palette.hover()};
        color: #111;
    }}
    QPushButton:disabled {{
        border-color: #3a3a3a;
        color: #555555;
    }}
    """


def build_primary_button_style(
    palette: ScreenPalette,
    *,
    padding: str = "10px 26px",
    min_width: int = 200,
    font_size: str = "15px",
    font_weight: str = "700",
) -> str:
    """Return a filled accent button style used for primary actions."""

    return f"""
    QPushButton {{
        font-size: {font_size};
        font-weight: {font_weight};
        color: #111111;
        background-color: {palette.accent};
        border: none;
        border-radius: 10px;
        padding: {padding};
        min-width: {min_width}px;
    }}
    QPushButton:hover {{
        background-color: {palette.hover()};
    }}
    QPushButton:disabled {{
        background-color: #333333;
        color: #666666;
    }}
    """


def build_secondary_button_style(
    palette: ScreenPalette,
    *,
    padding: str = "6px 16px",
    radius: int = 6,
    font_size: str = "13px",
    font_weight: str = "600",
) -> str:
    """Return a thinner outlined button variant used for inline controls."""

    return build_outline_button_style(
        palette,
        thickness=1,
        padding=padding,
        radius=radius,
        font_size=font_size,
        font_weight=font_weight,
    )


class StyledScreen(QWidget):
    """Base QWidget that applies the global palette background automatically."""

    def __init__(self, parent: Optional[QWidget] = None, *, palette: Optional[ScreenPalette] = None):
        super().__init__(parent)
        self.palette = palette or ScreenPalette()
        object_name = self.objectName() or self.__class__.__name__.lower()
        self.setObjectName(object_name)
        self.setStyleSheet(f"#{object_name} {{ background-color: {self.palette.background}; }}")
