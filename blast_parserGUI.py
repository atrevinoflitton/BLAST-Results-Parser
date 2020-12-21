from tkinter import *
from tkinter import ttk as ttk
from tkinter import filedialog
from tkinter import scrolledtext


## Blast Parser
def blast_parser(file):
    # Regex for query
    import re

    ## Open & Read
    with open(file, 'r') as f:
        file = f.read()

    re_query = r"Query=\s(\w+)"
    query = re.findall(re_query, file)

    # Regex for BestHit
    re_best = r"(>\w+.+\w+.+\s+\w+.+\w.+)"
    best = re.findall(re_best, file)
    best_list = []

    # Trim over shoot
    for i in range(len(best)):
        list_item = re.sub(r"(\n\s+Length.+\d)", "", (best[i]))
        best_list.append(list_item)

    # Regex for E-val
    re_eval = r"(\d[e].\d+)"
    e_val = re.findall(re_eval, file)
    # Only keep the 1st of 4 returned
    e_val = (e_val[0::4])

    # Regex for IDs
    re_id = r"Identities\s.\s(\d+.\d+\s.\d+..)"
    iden = re.findall(re_id, file)

    for i in (range(0, (len(query)))):
        formatting = query[i] + "\nBest Hit: " + best_list[i] + "\nE-Value: " + e_val[
            i] + "\nIdentities: " + iden[i] + "\n\n\n\n"
        textbox.insert(INSERT, formatting)




## Button Functions
def blast_file():
    root.filename = filedialog.askopenfilename(title="Please select the file with the BLAST results")
    file_path = (str(root.filename))
    blast_parser(file_path)


def save_file():
    write_file = filedialog.asksaveasfilename(initialdir = "/",title = "Name file")
    open_file = open(write_file, 'w')
    open_file.write(textbox.get(1.0, END))
    open_file.close()


def clear_text():
    textbox.delete(1.0, END)



## GUI Setup
root = Tk()

## Title the window, set size and background color
root.title("Blast Results Parser")
root.geometry('750x800')
root.configure(bg="lavender")


## Add drame to break up the window
frame = LabelFrame(root, height=550, width=715, bg="MistyRose2", bd=2)
frame.place(x=18,y=130)



## Labels
lTitle = Label(root, text="Blast Results Parser", compound=CENTER, font=("Verdana", 18), bg="lavender").place(x=245, y=55)


lDescript = Label(root,
                  text="This tools will retrieve the title line, Best Hit, E-Value and Identity Percentage from your BLAST results."
                       "\nYou can save the results or add your own notes and save them with the output.", font=("Verdana", 10), bg="MistyRose2").place(x=25, y=150)


lAuthor = Label(root, text="Created by Analia Treviño-Flitton", font=("Verdana", 10), bg="lavender").place(x=280, y=720)





## Buttons
select_button = ttk.Button(root, text="Select File", command=blast_file)
select_button.place(x=200, y=215)


save_button = ttk.Button(root, text="Save Results", command=save_file)
save_button.place(x=500, y=215)


clear_button = ttk.Button(root, text="Clear", width=92, command=clear_text)
clear_button.place(x=50, y=595)



## Textbox
textbox = scrolledtext.ScrolledText(root, width=70, height=20, font=("Courier", 11))
textbox.place(x=50, y=250)






if __name__ == '__main__':
    root.mainloop()

