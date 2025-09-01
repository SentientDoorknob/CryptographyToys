import tkinter as tk
from Utility.Tools import MakeCosets

num_cosets = 4
texts = []

def OpenSplitter(text, loop):
    global texts
    global num_cosets
    if loop:
        loop.destroy()
    texts = []

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
    info = tk.Frame(root, width=screen_width, height=screen_height // 10, bg=info_color, borderwidth=0.5,
                    relief="solid")
    info.grid(row=0, column=0, columnspan=14, rowspan=1, sticky="NESW")

    title = tk.Label(info, text="Splitter", font=title_font, bg=info_color)
    title.grid(row=0, padx=7, pady=(5, 0), columnspan=2, sticky="w")
    
    cosets_frame = tk.Frame(root, bg=frame_color)
    cosets_frame.grid(row=1, column=0, rowspan=18, columnspan=20, sticky="NEWS")
    
    def set_text(text, area):
        area.config(state="normal")
        area.delete("1.0", "end")
        area.insert("1.0", text)
        area.config(state="disabled")
    
    def UpdateCosets(num_box):
        global num_cosets, texts
        num_cosets = int(num_box.get())
        
        for textbox in texts:
            textbox.destroy()
        texts = []
        
        cosets = MakeCosets(text, num_cosets)

        for j in range(num_cosets):
            cosets_frame.grid_rowconfigure(j, weight=1)
        cosets_frame.grid_columnconfigure(0, weight=1)
        
        for j in range(num_cosets):
            textbox = tk.Text(cosets_frame, wrap="word", font=plain_font, state="disabled", relief="flat")
            textbox.grid(row=j, padx=1, pady=1, sticky="news")
            set_text(cosets[j], textbox)
            texts.append(textbox)

    buttons = tk.Frame(root, bg=info_color, borderwidth=0.5, relief="solid")
    buttons.grid(row=19, column=0, columnspan=14, rowspan=1, sticky="NESW")

    button_columns = 14
    for i in range(button_columns):
        buttons.grid_columnconfigure(i, weight=1, minsize=screen_width // button_columns)
    buttons.grid_rowconfigure(0, weight=1)
    
    
    number_selection = tk.Spinbox(buttons, from_=1, to=30, state="normal",
                                  relief="flat", command=lambda: UpdateCosets(number_selection), font=bold_font)
    number_selection.grid(row=0, column=11, columnspan=2, sticky="news", padx=3, pady=3)
    number_selection.delete(0, "end")
    number_selection.insert(0, str(num_cosets))
    number_selection.config(state="readonly")
    UpdateCosets(number_selection)

    def Exit():
        import Tools.Splitter
        Tools.Splitter.OpenCosetInterface(Tools.Splitter, root, gen_new=True)

    exit_button = tk.Button(buttons, text="Back", font=bold_font, relief="flat", borderwidth=1, command=Exit)
    exit_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")
    
    root.mainloop()