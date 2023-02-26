import json
import tkinter.filedialog
import tkinter as tk
from tags import TAGS
from tkinter import messagebox


class MyGUI:
    def __init__(self, root, tags):
        self.tags = tags
        self.root = root
        self.current_index = -1
        self.items = []
        self.notes = []
        self.save_file = None
        self.root.geometry("3000x2000")
        self.root.title("My Note App")

        # Set up label
        self.label_frame = tk.Frame(self.root)
        self.label_frame.pack()
        self.label = tk.Label(self.label_frame, text="Choose relevant tags for each note", font=('Arial', 18))
        self.label.pack(padx=100, pady=100)

        # Create a frame of checkboxes
        self.button_frame = tk.Frame(self.root)
        for config in range(3):
            self.button_frame.columnconfigure(config, weight=1)
        self.rows = 3
        self.row = 0
        self.column = 0
        self.tag_vars = []
        for tag in self.tags:
            var = tk.BooleanVar(value=False)
            self.tag_vars.append(var)
            self.button1 = tk.Checkbutton(self.button_frame, text=f"{tag}", font=('Arial', 18), variable=var)
            self.button1.grid(row=self.row, column=self.column, sticky=tk.W + tk.E)
            if self.column < 2:
                self.column += 1
            else:
                self.column = 0
            if self.column % 3 == 0:
                self.row += 1
        self.button_frame.pack(fill="x")

        # Create a "Next" button
        self.next_button = tk.Button(root, text="Next", font=('Arial', 18), command=self.show_next)
        self.next_button.pack(padx=50, pady=50)

        # Create a "Select File" button
        self.read_button = tk.Button(root, text="Select File", font=('Arial', 18), command=self.read_file)
        self.read_button.pack(padx=50, pady=50)

    def read_file(self):
        # Read the file and save its contents to the 'items' list
        self.filepath = tk.filedialog.askopenfilename()
        with open(self.filepath, 'r') as file:
            self.lines = file.readlines()
            current_item = ""
            for q in self.lines:
                if not q.strip():
                    continue
                current_item += q
                if q.endswith("\n"):
                    self.items.append(current_item)
                    current_item = ""
            if current_item:
                self.items.append(current_item)

    def show_next(self):
        if not self.items:
            # If no file has been selected, display an error message
            messagebox.showinfo("Error", "Please select a file.")
            return

        # Get the selected tags and add them to notes
        selected_tags = [self.tags[i] for i, var in enumerate(self.tag_vars) if var.get()]
        self.notes.append({
            "note": self.items[self.current_index],
            "tags": selected_tags
        })

        # Move to the next item in the list
        self.current_index += 1
        if self.current_index >= len(self.items):
            # If we have reached the end of the list, display a "Finished!" message
            self.current_index = 0
            self.label.config(text="Finished!")

            # Save notes to a file if needed
            if self.save_file:
                with open(self.save_file, "a") as f:
                    json.dump(self.notes, f)

            # Clear the notes list
            self.notes = []
            self.items = []
        else:
            # If there are more items, display the next one and reset the checkboxes
            self.label.config(text=self.items[self.current_index])
            for var in self.tag_vars:
                var.set(False)


root = tk.Tk()
my_gui = MyGUI(root, TAGS)
my_gui.save_file = "notes.json"  # set the save_file attribute to the desired file path
root.mainloop()
