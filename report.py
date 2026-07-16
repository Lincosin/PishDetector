def print_report(result):

    print("\n========== RESULT ==========")

    print(f"Domain : {result['domain']}")
    print(f"Status : {result['status']}")

    print("\nCharacter Analysis")

    for item in result["characters"]:

        print("-" * 40)

        print(f"Character : {item['character']}")
        print(f"Unicode   : {item['unicode']}")
        print(f"Name      : {item['name']}")