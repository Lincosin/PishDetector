from validator import validate_url
from parser import extract_domain
from detector import analyze_domain
from report import print_report


def main():
    print("=" * 50)
    print("Homograph Detector v1")
    print("=" * 50)

    url = input("\nInput URL : ")

    if not validate_url(url):
        print("\nInvalid URL!")
        return

    domain = extract_domain(url)

    result = analyze_domain(domain)

    print_report(result)


if __name__ == "__main__":
    main()