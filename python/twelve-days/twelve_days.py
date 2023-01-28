VERSES: dict[int, dict[str, str]] = {
    1: {
        "verse": "a Partridge in a Pear Tree.",
        "day": "first"
    },
    2: {
        "verse": "two Turtle Doves,",
        "day": "second"
    },
    3: {
        "verse": "three French Hens,",
        "day": "third"
    },
    4: {
        "verse": "four Calling Birds,",
        "day": "fourth"
    },
    5: {
        "verse": "five Gold Rings,",
        "day": "fifth"
    },
    6: {
        "verse": "six Geese-a-Laying,",
        "day": "sixth"
    },
    7: {
        "verse": "seven Swans-a-Swimming,",
        "day": "seventh"
    },
    8: {
        "verse": "eight Maids-a-Milking,",
        "day": "eighth"
    },
    9: {
        "verse": "nine Ladies Dancing,",
        "day": "ninth"
    },
    10: {
        "verse": "ten Lords-a-Leaping,",
        "day": "tenth"
    },
    11: {
        "verse": "eleven Pipers Piping,",
        "day": "eleventh"
    },
    12: {
        "verse": "twelve Drummers Drumming,",
        "day": "twelfth"
    }
}

def first_line(day: str):
    return f"On the {day} day of Christmas my true love gave to me:"

def create_lines(verse_number: int):
    verse_lines: list[str] = [first_line(VERSES[verse_number]["day"])]
    for line in range(verse_number, 0, -1):
        verse = VERSES[line]["verse"]
        if line == 1 and verse_number > 1:
            verse = f"and {verse}"
        verse_lines.append(verse)
    return " ".join(verse_lines)

def recite(start_verse: int, end_verse: int) -> list[str]:
    return [
        create_lines(verse_number)
        for verse_number in range(start_verse, end_verse+1)
    ]
