# The list of dictionaries that you're using to store the notes is a good data structure for searching by tags, because it allows you to
# associate a set of tags with each note. To search for notes with a specific tag or combination of tags, you can iterate over the list of
# dictionaries and check if the "tags" key for each dictionary contains the desired tags.
#
# For example, if you want to search for all notes with the "advice" tag, you can use a list comprehension to filter the notes list:
#
# css
#
notes_with_advice = [note for note in notes if "advice" in note["tags"]]
#
# This will create a new list called notes_with_advice that contains all the dictionaries in notes that have the "advice" tag.
#
# You can also search for notes that have multiple tags by using set operations. For example, if you want to find all notes that have
# both the "advice" and "anxiety" tags, you can use the set and intersection methods to check if the "tags" set for each dictionary contains both tags:
#
# makefile
#
tags = {"advice", "anxiety"}
notes_with_tags = [note for note in notes if set(note["tags"]).intersection(tags) == tags]
#
# This will create a new list called notes_with_tags that contains all the dictionaries in notes that have both the "advice" and "anxiety" tags.
#
# Overall, the list of dictionaries data structure should be sufficient for searching by tags, especially if the number of notes is relatively small.
# If you have a large number of notes and want to optimize search performance, you might consider using a database or other data storage solution that
# supports efficient searching and indexing.

def show_next(self):
    # Update the tags for the current note
    tags = [self.tags[i] for i, var in enumerate(self.tag_vars) if var.get()]
    if not tags:
        # Don't save the note if no tags are selected
        return

    # Create a new dictionary for the current note and its tags
    note_dict = {"note": self.items[self.current_index], "tags": tags}
    self.notes.append(note_dict)

    # Save the updated notes to the file
    if self.save_file:
        try:
            with open(self.save_file, "r") as f:
                notes = json.load(f)
        except FileNotFoundError:
            notes = []
        notes.extend(self.notes)
        with open(self.save_file, "w") as f:
            json.dump(notes, f)
    else:
        self.label.config(text=self.items[self.current_index])
        # Reset the checkboxes
        for var in self.tag_vars:
            var.set(False)
    # Show the next note
    self.current_index += 1
    if self.current_index >= len(self.items):
        self.current_index = 0
    self.label.config(text=self.items[self.current_index])

