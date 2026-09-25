# Don't Remove Credit
# Made by @MrYKTG https://github.com/MrYKTG
# @mrxeontg @xeonbotz
# Ask Doubt on telegram @Mrxeontg
# Copyright (c) 2026 XeonBotz
# All Rights Reserved.

import humanize
from config import ENABLE_PRO_CAPTION, PRO_CUSTOM_CAPTION


def _fmt_duration(seconds: int) -> str:
    if not seconds:
        return ""
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}h {m}m"
    if m:
        return f"{m}m {s}s"
    return f"{s}s"


def _extract(message):
    """Return (original_caption, filename, filesize, duration) from a Pyrogram Message."""
    original = ""
    filename = ""
    filesize = ""
    duration = ""

    if message is None:
        return original, filename, filesize, duration

    # original caption (HTML)
    if getattr(message, "caption", None):
        try:
            original = message.caption.html
        except Exception:
            original = str(message.caption)

    media = (
        getattr(message, "document", None)
        or getattr(message, "video", None)
        or getattr(message, "audio", None)
    )

    if media is not None:
        filename = (
            getattr(media, "file_name", None)
            or getattr(media, "title", None)
            or ""
        )
        size = getattr(media, "file_size", 0) or 0
        if size:
            filesize = humanize.naturalsize(size, binary=True)
        dur = getattr(media, "duration", 0) or 0
        if dur:
            duration = _fmt_duration(dur)

    # if no caption but we do have a filename, use that as the fallback
    if not original and filename:
        original = filename

    return original, filename, filesize, duration


def build_pro_caption(message, client=None) -> str:
    """
    Build the caption used when copying a DB message to the user.

    - If PRO caption is enabled → formats PRO_CUSTOM_CAPTION with rich placeholders.
    - Otherwise → falls back to client.messages['CAPTION'] (legacy) or the raw caption.
    """
    original, filename, filesize, duration = _extract(message)

    if not original:
        return ""

    # ---------- PRO caption ----------
    if ENABLE_PRO_CAPTION and PRO_CUSTOM_CAPTION:
        fields = {
            "previouscaption": original,
            "caption":         original,
            "filename":        filename,
            "file_name":       filename,
            "filesize":        filesize,
            "file_size":       filesize,
            "duration":        duration,
            "bot_username":    getattr(client, "username", "") or "",
            "bot":             getattr(client, "username", "") or "",
        }
        try:
            return PRO_CUSTOM_CAPTION.format(**fields)
        except (KeyError, IndexError):
            # template referenced an unknown placeholder — safe fallback
            return original

    # ---------- Legacy fallback ----------
    if client is not None:
        tmpl = client.messages.get("CAPTION", "")
        if tmpl and getattr(message, "document", None):
            try:
                return tmpl.format(
                    previouscaption=f"<blockquote>{original}</blockquote>"
                )
            except (KeyError, IndexError):
                pass

    return original
