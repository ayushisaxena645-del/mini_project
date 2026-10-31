
from urllib.parse import urlparse

def analyze_url(url):

    parsed_url = urlparse(url)

    if parsed_url.scheme not in ["http", "https"]:
        return {
            "valid": False,
            "message": "Invalid URL protocol"
        }

    if not parsed_url.netloc or "." not in parsed_url.netloc:
        return {
            "valid": False,
            "message": "Invalid URL"
        }

    return {
        "valid": True,
        "message": "URL format is valid",
        "domain": parsed_url.netloc
    }
