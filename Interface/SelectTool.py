import tkinter as tk


def OpenInput(loop=None):
    if loop:
        loop.destroy()

    info_color = "#d6d6d6"

    # Initialising root
    root = tk.Tk()
    root.title("Tool Selection")
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

    title = tk.Label(info, text="Tool Selection", font=title_font, bg=info_color)
    title.grid(row=0, padx=7, pady=(5, 0), columnspan=2, sticky="w")

    tool_selection = tk.Frame(root, relief="flat")
    tool_selection.grid(row=1, column=0, columnspan=14, rowspan=18, sticky="NESW")

    tool_columns = 6
    tool_rows = 3
    for i in range(tool_columns):
        tool_selection.grid_columnconfigure(i, weight=1, minsize=screen_width // tool_columns)
    for i in range(tool_rows):
        tool_selection.grid_rowconfigure(i, weight=1, minsize=18/20*screen_height//tool_rows)

    def OpenTool(func, loop):
        func(loop)
        return

    import MainFile
    buttons = []; images = []; functions = []
    for i, (text, func, image_path) in enumerate(MainFile.main_functions):
        x, y = i % tool_columns, i // tool_columns
        image = tk.PhotoImage(file=fr"Icons\{image_path}").subsample(3, 3)
        images.append(image)
        tool_button = tk.Button(tool_selection, text=text, relief="flat", font=bold_font, image=image, compound="top", command=lambda f=func: OpenTool(f, root))
        tool_button.grid(row=y, column=x, sticky="NESW")
        buttons.append(tool_button)

    buttons = tk.Frame(root, bg=info_color, borderwidth=1, relief="solid")
    buttons.grid(row=19, column=0, columnspan=14, rowspan=1, sticky="NESW")

    button_columns = 14
    for i in range(button_columns):
        buttons.grid_columnconfigure(i, weight=1, minsize=screen_width // button_columns)
    buttons.grid_rowconfigure(0, weight=1)

    exit_button = tk.Button(buttons, text="Exit", font=bold_font, relief="flat", borderwidth=1,
                            command=lambda: Exit(False))
    exit_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")

    clear_button = tk.Button(buttons, text="Clear Globals", font=bold_font, relief="flat", borderwidth=1,
                            command=lambda: Clear())
    clear_button.grid(row=0, column=11, padx=3, pady=3, columnspan=2, sticky="nsew")

    def Exit(success):
        root.destroy()
        
    def Clear():
        MainFile.ClearGlobals()

    root.bind("<Return>", lambda x: Exit(True))

    tk.mainloop()
