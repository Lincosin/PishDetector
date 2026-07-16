import unicodedata


def analyze_domain(domain: str):

    characters = []

    suspicious = False

    for char in domain:

        info = {
            "character": char,
            "unicode": f"U+{ord(char):04X}",
            "name": unicodedata.name(char, "UNKNOWN")
        }

        characters.append(info)

        if ord(char) > 127:
            suspicious = True

    return {
        "domain": domain,
        "status": "Suspicious" if suspicious else "Safe",
        "characters": characters
    }