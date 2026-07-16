import validators


def validate_url(url: str) -> bool:
    """
    Validate whether the input is a proper URL.
    """

    return validators.url(url)