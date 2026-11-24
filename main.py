"""The 3 AM Commit Message.

One commit message, written at 3 AM, printed to stdout.
Deterministic, standard library only, writes no files.
"""

LINE = (
    "3:04 AM: fixed the bug by deleting the feature, the tests, "
    "and my will to deploy — shipping it anyway."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
