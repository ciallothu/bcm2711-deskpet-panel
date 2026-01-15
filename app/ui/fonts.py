import os
from typing import Iterable, List

from PIL import ImageFont


_CUSTOM_FONT_PATHS: List[str] = []


def set_font_paths(paths: Iterable[str]) -> None:
    _CUSTOM_FONT_PATHS.clear()
    for p in paths:
        if p:
            _CUSTOM_FONT_PATHS.append(os.path.expanduser(str(p)))


def load_font(size: int) -> ImageFont.ImageFont:
    # Prefer the font shipped in the driver zip (arialbd.ttf)
    base = os.path.dirname(__file__)
    candidates = [
        *[p for p in _CUSTOM_FONT_PATHS if p],
        os.path.join(os.path.dirname(base), "drivers", "fonts", "arialbd.ttf"),
        os.path.join(base, "assets", "fonts", "arialbd.ttf"),
        os.path.join(os.path.dirname(base), "fonts", "arialbd.ttf"),
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/arphic/ukai.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        os.path.join(base, "fonts", "NotoSansSC-Regular.otf"),
        os.path.join(base, "fonts", "NotoSansCJK-Regular.ttc"),
        os.path.join(base, "arialbd.ttf"),
    ]
    for p in candidates:
        try:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()
