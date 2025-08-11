import sys
from stats import generate_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    generate_report(sys.argv[1])

    