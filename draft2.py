import tkinter as tk
from tkinter import filedialog
import datetime

# Next job create a program to add tags to notes

filepath = "favourite_quotes.txt"
filepath2 = "fav-quotes.txt"

quote_dict = {}
# Open the file and read its contents
with open(filepath2, 'r') as file:
    lines = file.readlines()
    print(lines)

def format_and_tag_note(array):
    quotelist = []
    placeholder = ""
    for q in array:
        placeholder += q
        if (q == "\n"):
            print(placeholder)
            tags = input(f"Note: {placeholder} - Type tags starting with a hash with a space between them: ")
            if tags == q:
                break
            newString = placeholder.replace("\n\n", f"\n{tags}\n\n")
            quotelist.append(newString)
            placeholder = ""
    return quotelist

formattedList = format_and_tag_note(lines)
print(formattedList)

with open(f"newfile-{filepath}", 'w') as file:
    for q in formattedList:
        file.write(q)

# def add_notes_and_tags(notes_list):
#     dict = {}
#     for n in notes_list:
#
#     return dict


# def add_meta_data(dictionary, location="Frinton", tags=[], file="unknown"):
#     #     Turn array of notes into a dictionary with meta-data input by user or automatically added
#     # const object = [{note : "The note would live here", tags : ["#FavouriteQoutes", "#OriginalQuote", "#Advice"],
#     # metaData: {date : "07/07/23", timeAdded : "12:00", location : "England", fromFile : "ForMyKids", number : 7}]
#     # return an array of dictionaries
#     array = []
#     current_time = datetime.datetime.now()
#     date = current_time.date()
#     time = current_time.time()
#     dictionary = {}
#     meta = {}
#     tags = []
#     title_question = "y" #input(f"Is this the file the notes are from? {arr[0]} input: Y/N? : ").lower()
#     if title_question == "y":
#         meta["fileFrom"] = arr[0]
#         tags.append(f"#{arr[0]}")
#     else:
#         print("Please add file information when importing file")
#         meta["fileFrom"] = file
#     meta["time"] = f"{time}"
#     meta["date"] = f"{date}"
#     dict["note"] = n
#
#     dict["meta"] = meta
#     array.append(dict)
#     return array


# for q in formatFileRead(lines):
#     print(q)

# dictionary_notes = add_meta_data(formattedList)
# print(dictionary_notes)



# def select_file():
#     filepath = filedialog.askopenfilename()
#     parse_file(filepath)

# def parse_file(filepath):
#     # Create a new frame to hold the labels
#     frame = tk.Frame(root)
#     frame.pack()



    # Iterate through the lines and create a label for each one
    # for line in lines:
    #     label = tk.Label(frame, text=line)
    #     label.pack()

# root = tk.Tk()
# select_button = tk.Button(root, text="Select file", command=select_file)
# select_button.pack()
# root.mainloop()

