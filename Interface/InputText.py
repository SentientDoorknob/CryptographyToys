import tkinter as tk


def OpenInput(module, loop=None):

    if loop:
        loop.destroy()

    info_color = "#d6d6d6"

    # Initialising root
    root = tk.Tk()
    root.title("Input")
    root.attributes("-fullscreen", True)
    root.tk.call('tk', 'scaling', root.winfo_fpixels('1i') / 72.0)

    # Getting screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

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

    info = tk.Frame(root, width=screen_width, height=screen_height // 10, bg=info_color, borderwidth=1, relief="solid")
    info.grid(row=0, column=0, columnspan=14, rowspan=1, sticky="NESW")

    title = tk.Label(info, text="Input", font=title_font, bg=info_color)
    title.grid(row=0, padx=7, pady=(5, 0), columnspan=2, sticky="w")

    text_area = tk.Text(root, wrap="word", font=plain_font, state="normal")
    text_area.grid(row=1, column=0, columnspan=14, rowspan=18, sticky="nesw")

    buttons = tk.Frame(root, bg=info_color, borderwidth=1, relief="solid")
    buttons.grid(row=19, column=0, columnspan=14, rowspan=1, sticky="NESW")

    button_columns = 14
    for i in range(button_columns):
        buttons.grid_columnconfigure(i, weight=1, minsize=screen_width // button_columns)
    buttons.grid_rowconfigure(0, weight=1)

    exit_button = tk.Button(buttons, text="Back", font=bold_font, relief="flat", borderwidth=1, command=lambda: Exit(False))
    exit_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")

    confirm_button = tk.Button(buttons, text="Confirm", font=bold_font, relief="flat", borderwidth=1, command=lambda: Exit(True))
    confirm_button.grid(row=0, column=12, padx=3, pady=3, sticky="nsew")

    def Exit(success):
        module.OnTextInput(success, text_area.get("1.0", "end"), root)

    root.bind("<Return>", lambda x: Exit(True))

    tk.mainloop()
