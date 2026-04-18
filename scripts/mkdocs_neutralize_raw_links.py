"""
MkDocs hook module: neutralize markdown links that point at ``raw/`` before HTML render.

The published site (``docs_dir: wiki``) does not include the evidence corpus; relative
``[label](../../raw/...)`` links would otherwise become broken navigable URLs. We replace
them with a non-link span so Obsidian-authored markdown stays unchanged on disk while
the public build shows inert provenance text.

Register in ``mkdocs.yml``::

    hooks:
      - scripts/mkdocs_neutralize_raw_links.py
"""

from __future__ import annotations

import html
import re

# Standard markdown links (not images)
MD_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
# Images pointing at raw/ — drop the image, keep alt as text
MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def _target_is_raw_path(target: str) -> bool:
    t = target.split("#", 1)[0].split("?", 1)[0].strip()
    return "raw/" in t.replace("\\", "/")


def _span(label: str, target: str) -> str:
    safe_label = html.escape(label, quote=False)
    safe_target = html.escape(target, quote=True)
    return (
        '<span class="raw-source-ref" data-raw-path="true" '
        f'title="Evidence path (not published on this site): {safe_target}">{safe_label}</span>'
    )


def on_page_markdown(markdown: str, *, page, config, files):
    def sub_link(m: re.Match[str]) -> str:
        label, target = m.group(1), m.group(2).strip()
        if _target_is_raw_path(target):
            return _span(label, target)
        return m.group(0)

    def sub_img(m: re.Match[str]) -> str:
        alt, target = m.group(1), m.group(2).strip()
        if _target_is_raw_path(target):
            return _span(alt or "(image)", target)
        return m.group(0)

    out = MD_LINK.sub(sub_link, markdown)
    out = MD_IMAGE.sub(sub_img, out)
    return out
