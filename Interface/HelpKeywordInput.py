import tkinter as tk


def OpenHelp():
    info_color = "#d6d6d6"

    # Initialising root
    root = tk.Tk()
    root.title("Keyword Input Help")
    root.attributes("-topmost", True)

    # Getting screen dimensions
    screen_width = int(root.winfo_screenwidth() / 16)
    screen_height = int(root.winfo_screenheight() / 3)

    root.minsize(screen_width, screen_height)

    # Initialising fonts
    title_font = ("Consolas", 14, "bold")
    plain_font = ("Consolas", 12, "normal")
    bold_font = ("Consolas", 12, "bold")
    input_font = ("Consolas", 20, "normal")

    # Initialising Grid Layout
    num_rows = 20
    num_columns = 14

    for i in range(num_rows):
        root.grid_rowconfigure(i, weight=1, minsize=screen_height // num_rows)

    for i in range(num_columns):
        root.grid_columnconfigure(i, weight=1, minsize=screen_width // num_columns)

    help_area = tk.Text(root, font=bold_font, wrap="word", state="normal")
    help_area.grid(columnspan=14, rowspan=20, sticky="nsew", padx=10, pady=10)

    text = """Okie here we go
    
CAESAR CIPHER
Note: a = A = 0
Enter 1 number/character; eg.
a .. B .. 19 .. etc.

VIGNERE CIPHER
Note: abc = ABC
Enter string of letters; eg.
favor .. ELIAS

AFFINE CIPHER
Note: 1 2 = [1, 2]
Enter [m, c]; eg.
[13, 14] .. 2, 9

PERMUTATION CIPHER
Note: Ab = a B = 1 2
Enter permutation key, will be simplified according to ascii. If letters are used, spaces are unnecessary; eg.
0 2 1 .. ive ... h i

NIHILIST CIPHER
Note: a = A
Same as vignere, don't use numbers due to difference in polybius square in real puzzles; eg.
hello .. SIMMS

HILL CIPHER
Note: a = 0 = A
Enter matrix a, b, c, d. Will be adjusted if non-invertible; eg.
[[15, 16], [19, 1]] .. 9 8 24 1"""

    help_area.insert("1.0", text)
    help_area.configure(state="disabled")

    root.mainloop()
