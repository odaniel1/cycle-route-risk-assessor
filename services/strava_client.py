import re

def extract_route_id(txt: str) -> int:
    """Extract the numeric route ID from a Strava route URL."""
    m = re.search(r"strava\.com/routes/(\d+)", txt)
    if m:
        return int(m.group(1))
    return None