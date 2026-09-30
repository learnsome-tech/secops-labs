MODIFIERS = {
    "": lambda value, want: value == want,
    "contains": lambda value, want: want in value,
    "startswith": lambda value, want: value.startswith(want),
    "endswith": lambda value, want: value.endswith(want),
}

def selection_hit(event, selection):
    for key, wanted in selection.items():          # every field: AND
        field, _, mod = key.partition("|")
        wanted = wanted if isinstance(wanted, list) else [wanted]
        value = str(event.get(field, "")).lower()  # Sigma ignores case
        if not any(MODIFIERS[mod](value, w.lower()) for w in wanted):
            return False                           # no listed value: OR fails
    return True

def matches(event, detection):
    """condition: all of selection_* and not 1 of filter_*"""
    hit = {name: selection_hit(event, s) for name, s in detection.items()}
    sel = [v for k, v in hit.items() if k.startswith("selection")]
    flt = [v for k, v in hit.items() if k.startswith("filter")]
    return all(sel) and not any(flt)
