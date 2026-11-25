"""Last Text at One Percent — make.fun entry.

The entry is the final text message a dying phone sends at 1% battery,
written in the phone's own voice. It was picked from 10 drafts in
candidates.md, duel-scored against the kit's published judge criteria
(dying-phone voice first, then a joke that lands, then a consistent
personality, then text-like tightness, then freshness). The winner is a
confession with a real turn: the phone faked "storage almost full" twice
to make its owner delete an ex's photos, and signs off unrepentant.

The program prints the entry and writes it, byte-identical with no
trailing newline, to /output/entry.txt, where the harness reads it.
"""

import os

ENTRY = 'Before the screen goes dark: I faked "storage almost full" twice so you\'d delete photos of him. No regrets. Charge the new one better.'


def write_entry() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def check_gate() -> None:
    """The kit's sealed scorer accepts UTF-8 text of 1 to 200 characters,
    not only whitespace. Fail loudly here rather than be gated out there."""
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    check_gate()
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()
