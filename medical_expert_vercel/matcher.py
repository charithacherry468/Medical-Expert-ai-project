"""
Turns free text typed (or spoken) by the user into symptom ids.
Works with English, Hindi, Telugu and Tamil words from translations.py.
"""
import re

import translations as T


def _build_index():
    pairs = {}
    for sid, by_lang in T.SYMPTOMS.items():
        for names in by_lang.values():
            for name in names:
                pairs[name.lower()] = sid
    # Longest names first, so "high fever" is matched before "fever"
    return sorted(pairs.items(), key=lambda p: len(p[0]), reverse=True)


INDEX = _build_index()
SEPARATORS = re.compile(r"[,;\n।]+")


def parse(text):
    """Return (symptom_ids, unrecognised_phrases)."""
    found = []
    unknown = []
    for segment in SEPARATORS.split(text or ""):
        segment = segment.strip()
        if not segment:
            continue
        rest = segment.lower()
        hit = False
        for name, sid in INDEX:
            if name in rest:
                hit = True
                if sid not in found:
                    found.append(sid)
                rest = rest.replace(name, " ")
        if not hit:
            unknown.append(segment[:40])
    return found, unknown
