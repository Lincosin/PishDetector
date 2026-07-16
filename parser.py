import tldextract
import idna


def decode_punycode(domain: str) -> str:
    """
    Decode punycode if present.
    """

    try:
        return idna.decode(domain)
    except Exception:
        return domain


def extract_domain(url: str) -> str:
    """
    Extract only the domain.
    """

    extracted = tldextract.extract(url)

    domain = f"{extracted.domain}.{extracted.suffix}"

    return decode_punycode(domain)