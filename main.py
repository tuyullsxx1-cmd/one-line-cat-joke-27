import os

# Shape D: the punchline picks a branch, then the line is assembled.
CAT_DID_IT = True
if CAT_DID_IT:
    deed = "knocked my laptop off the table, sat in its warm spot,"
    look = "looked at me like I was the one who didn't understand how computers work"
else:
    deed = "slept through the whole afternoon,"
    look = "woke up only to demand dinner an hour early"
LINE = "My cat " + deed + " and " + look + "."

# The cat's crime is only funny because it takes the warm spot afterwards.
assert "warm spot" in LINE
# The entry is one line: no newline inside, one trailing newline in the file.
assert "\n" not in LINE
# Brief cap for this bounty: the line must stay under 200 characters.
assert len(LINE) < 200
# The joke must be about a cat, obviously.
assert LINE.startswith("My cat")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
