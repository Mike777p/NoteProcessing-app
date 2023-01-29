TAGS = ["#favouriteQuotes", "#originalQuotes", "#love", "#4MyChildren", "#advice", "#anxiety", "#apocalypse", "#biography",
        "#blog", "#book", "#control", "#corruption", "#delusion", "#discipline", "#educuation", "#equality", "#film",
        "#fitness", "#food", "#gender", "#getItDone", "#governance", "#illusion", "#inspire", "#intelligence", "#journal",
        "#kelly", "#law", "#life", "#morality", "#motivate", "#produce", "#sleep", "#statusAnxiety",
        "#struggle", "#travel", "#truth", "#work"]
TAGS.sort()

import tkinter.filedialog

import tkinter as tk

class MyGUI:

        def __init__(self, root, tags):
                self.tags = tags
                self.root = root
                self.current_index = -1
                self.items = []
                self.root.geometry("3000x2000")
                self.root.title("My Note App")

                # Set up label
                self.label_frame = tk.Frame(self.root)
                self.label_frame.pack()
                self.label = tk.Label(self.label_frame, text="Select text file to process and choose relevant tags", font=('Arial', 18))
                self.label.pack(padx=100, pady=100)

                # Create select file button
                self.read_button = tk.Button(root, text="Select File", font=('Arial', 18), command=self.read_file).pack(padx=50, pady=50)

                self.button_frame = tk.Frame(self.root)
                for config in range(3):
                        self.button_frame.columnconfigure(config, weight=1)
                self.rows = 3
                self.row = 0
                self.column = 0
                for tag in self.tags:
                        self.button1 = tk.Button(self.button_frame, text=f"{tag}", font=('Arial', 18), command=None)
                        self.button1.grid(row=self.row, column=self.column, sticky=tk.W + tk.E)
                        if self.column < 2:
                                self.column += 1
                        else:
                                self.column = 0
                        if self.column % 3 == 0:
                                self.row += 1

                self.button_frame.pack(fill="x")

                self.next_button = tk.Button(root, text="Next", font=('Arial', 18), command=self.show_next).pack(padx=50, pady=50)



        def read_file(self):
                # Read the file and save its contents to the 'items' list
                self.filepath = tk.filedialog.askopenfilename()
                with open(self.filepath, 'r') as file:
                        self.lines = file.readlines()
                        placeholder = ""
                        for q in self.lines:
                                placeholder += q
                                if (q == "\n"):
                                        self.items.append(placeholder)
                                        placeholder = ""

        def show_next(self):
                self.current_index += 1
                if self.current_index >= len(self.items):
                        self.current_index = 0
                self.label.config(text=self.items[self.current_index])


root = tk.Tk()
my_gui = MyGUI(root, TAGS)
root.mainloop()


