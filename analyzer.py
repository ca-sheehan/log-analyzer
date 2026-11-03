
import argparse

THRESHOLD = 3


def count_failed_logins(filename):
    failed_counts = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if "FAILED" in line:
                parts = line.split()
                ip = parts[-1]
                failed_counts[ip] = failed_counts.get(ip, 0) + 1

    return failed_counts


def print_report(failed_counts):
    print("\nFailed Logins Report")
    print("--------------------")

    for ip, count in failed_counts.items():
        if count >= THRESHOLD:
            print(f"{ip}: {count} failed attempts <--- SUSPICIOUS!")
        else:
            print(f"{ip}: {count} failed attempts")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze server logs for suspicious login activity."
    )

    parser.add_argument(
        "filename",
        help="Path to the log file you want to analyze"
    )

    args = parser.parse_args()

    try:
        counts = count_failed_logins(args.filename)
        print_report(counts)

    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

