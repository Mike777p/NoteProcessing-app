import tkinter.filedialog
import tkinter as tk
TAGS = ["#favouriteQuotes", "#originalQuotes", "#love", "#4MyChildren", "#advice", "#anxiety", "#apocalypse", "#biography",
        "#blog", "#book", "#control", "#corruption", "#delusion", "#discipline", "#educuation", "#equality", "#film",
        "#fitness", "#food", "#gender", "#getItDone", "#governance", "#illusion", "#inspire", "#intelligence", "#journal",
        "#kelly", "#law", "#life", "#morality", "#motivate", "#produce", "#sleep", "#statusAnxiety",
        "#struggle", "#travel", "#truth", "#work"]
TAGS.sort()
import datetime

class MyGUI:

    def __init__(self, tags, quote_list):

        self.tags = tags
        self.len_of_tags = len(tags)
        self.root = tk.Tk()
        self.root.geometry("3000x2000")
        self.root.title("My Note App")
        self.quote_list = quote_list

        self.select_button = tk.Button(self.root, text="Select file", font=('Arial', 18), command=self.select_file)
        self.select_button.pack(pady=50)

        print(self.quote_list)

        self.label_frame = tk.Frame(self.root)
        self.label_frame.pack()
        self.label = tk.Label(self.label_frame,
                              text='"A man without a vision is a man without a future, \n'
                                'If something is possible for any man it is possible for you too.\n'
                                 'a man without a future will always return to his past."',
                         font=('Arial', 18))
        self.label.pack(padx=50, pady=50)
        self.label = tk.Label(self.label_frame, text="Select the tags you wish to add to this note:",
                              font=('Arial', 18))
        self.label.pack(padx=50, pady=50)

        self.button_frame = tk.Frame(self.root)
        for config in range(3):
            self.button_frame.columnconfigure(config, weight=1)
        self.rows = 3
        self.row = 0
        self.column = 0
        for tag in self.tags:
            self.button1 = tk.Button(self.button_frame, text=f"{tag}", font=('Arial', 18), command=None)
            self.button1.grid(row=self.row, column=self.column, sticky=tk.W+tk.E)
            if self.column < 2:
                self.column += 1
            else:
                self.column = 0
            if self.column % 3 == 0:
                self.row += 1
        # self.button2 = tk.Button(self.button_frame, text="#motivate", font=('Arial', 18), command=None)
        # self.button2.grid(row=0, column=1, sticky=tk.W + tk.E)
        # self.button3 = tk.Button(self.button_frame, text="#belief", font=('Arial', 18), command=None)
        # self.button3.grid(row=0, column=2, sticky=tk.W + tk.E)
        #
        # self.button4 = tk.Button(self.button_frame, text="#inspire", font=('Arial', 18), command=None)
        # self.button4.grid(row=1, column=0, sticky=tk.W + tk.E)
        # self.button5 = tk.Button(self.button_frame, text="#motivate", font=('Arial', 18), command=None)
        # self.button5.grid(row=1, column=1, sticky=tk.W + tk.E)
        # self.button6 = tk.Button(self.button_frame, text="#belief", font=('Arial', 18), command=None)
        # self.button6.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.button_frame.pack(fill="x")

        self.root.mainloop()

    def select_file(self):
        self.filepath = tk.filedialog.askopenfilename()
        self.read_file(self.filepath)
        # self.parse_file(self.filepath)

    def read_file(self, select_file):
        with open(select_file, 'r') as file:
            self.quote_list = file.readlines()
            return self.quote_list
            print("Ran!!")




MyGUI(TAGS, [])

# select_button = tk.Button(root, text="Select file", command=select_file)
# select_button.pack()
