# Starts with "MyClippings" and ends with "Notes"
# Removes "- Your Highlight"
with open("MyClippings.txt", "rb") as input_file:
    lines = input_file.readlines()
    with open("Clippings.txt", "wb") as output_file:
        for line in lines:
            if not line.startswith(b"- Your Highlight"):
                output_file.write(line)

with open("Clippings.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

notes_by_title = {}
current_title = None
for i, line in enumerate(lines):
    if line.startswith("=========="):
        try:
            current_title = lines[i+1].strip()
            if current_title not in notes_by_title:
                notes_by_title[current_title] = []
        except IndexError:
            # Ignore the last separator if there is no note following it
            pass
    elif current_title is not None:
        note = line.strip()
        if note not in notes_by_title[current_title]:
            notes_by_title[current_title].append(note)

with open("Notes.txt", "w", encoding="utf-8") as output_file:
    for title, notes in notes_by_title.items():
        output_file.write(title + "\n")
        for note in notes:
            output_file.write(note + "\n")
        output_file.write("\n")

with open("Notes.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

output_lines = []
seen_lines = set()
for line in lines:
    if line.strip() == "":
        output_lines.append(line)
    elif line not in seen_lines:
        output_lines.append(line)
        seen_lines.add(line)

with open("Notes.txt", "w", encoding="utf-8") as output_file:
    for line in output_lines:
        output_file.write(line)
