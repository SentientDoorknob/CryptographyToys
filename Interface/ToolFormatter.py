import tkinter as tk

def OpenFormatter(loop = None):
    
    if loop:
        loop.destroy()

    root = tk.Tk()
    root.title("Encoder Result")
    root.attributes("-fullscreen", True)
    root.tk.call('tk', 'scaling', root.winfo_fpixels('1i') / 72.0)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    title_font = ("Consolas", 14, "bold")
    plain_font = ("Consolas", 12, "normal")
    bold_font = ("Consolas", 12, "bold")

    num_rows = 20
    num_columns = 14

    frame_color = root.cget("bg")
    info_color = "#d6d6d6"

    for i in range(num_rows):
        root.grid_rowconfigure(i, weight=1, minsize=screen_height // num_rows)

    for i in range(num_columns):
        root.grid_columnconfigure(i, weight=1, minsize=screen_width // num_columns)

    # Adjusting the 'info' frame size and position
    info = tk.Frame(root, width=screen_width, height=screen_height // 10, bg=info_color, borderwidth=0.5, relief="solid")
    info.grid(row=0, column=0, columnspan=14, rowspan=1, sticky="NESW")

    title = tk.Label(info, text="Formatter", font=title_font, bg=info_color)
    title.grid(row=0, padx=7, pady=(5, 0), columnspan=2, sticky="w")
    
    input_frame = tk.Frame(root, bg=frame_color, borderwidth=0.5, relief="solid")
    input_frame.grid(row=1, rowspan=18, column=0, columnspan=num_columns//2, sticky="news")
    
    input_text = tk.Text(input_frame, wrap="word", font=plain_font, state="normal", relief="flat")
    input_text.pack(expand=True, fill="both", padx=10, pady=10)

    output_frame = tk.Frame(root, bg=frame_color, borderwidth=0.5, relief="solid")
    output_frame.grid(row=1, rowspan=18, column=num_columns//2, columnspan=num_columns // 2, sticky="news")
    
    output_text = tk.Text(output_frame, wrap="word", font=plain_font, state="disabled", relief="flat")
    output_text.pack(expand=True, fill="both", padx=10, pady=10)
    
    def set_text(text, area):
        area.config(state="normal")
        area.delete("1.0", "end")
        area.insert("1.0", text)
        area.config(state="disabled")
    

    buttons = tk.Frame(root, bg=info_color, borderwidth=0.5, relief="solid")
    buttons.grid(row=19, column=0, columnspan=14, rowspan=1, sticky="NESW")

    button_columns = 14
    for i in range(button_columns):
        buttons.grid_columnconfigure(i, weight=1, minsize=screen_width // button_columns)
    buttons.grid_rowconfigure(0, weight=1)
    
    def Exit():
        import MainFile
        MainFile.OpenInput(root)

    exit_button = tk.Button(buttons, text="Back", font=bold_font, relief="flat", borderwidth=1, command=Exit)
    exit_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")

    from Tools.Formatter import formats
    
    def UpdateText(*args):
        format_function = formats[placeholder.get()]
        text = format_function(input_text.get("1.0", "end"))
        set_text(text, output_text)

    input_text.bind("<KeyRelease>", UpdateText)
    
    placeholder = tk.StringVar(value="String Format")
    format_selection = tk.OptionMenu(buttons, placeholder, *formats.keys())
    format_selection.grid(row=0, column=11, columnspan=2, padx=3, pady=3, sticky="nsew")
    
    placeholder.trace("w", UpdateText)

    format_selection.config(
        font=bold_font,
        relief="flat",
        fg="black",  # text color
        activebackground="#c0c0c0",  # hover background
        activeforeground="black",  # hover text
        highlightthickness=0,
        bd=0
    )

    menu = format_selection["menu"]
    menu.config(
        bg=info_color,  # Dropdown background color
        fg="black",  # Dropdown text color
        font=bold_font,  # Font for all dropdown items
        activebackground="#c0c0c0",  # Hover background for items
        activeforeground="black",  # Hover text color
        relief="flat",  # Flat border
        bd=0  # Border width
    )
    
    tk.mainloop()