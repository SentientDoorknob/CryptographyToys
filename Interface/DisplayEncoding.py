import tkinter as tk

# Global flag to prevent generating new windows after exit
is_exiting = False
is_ciphertext = True


def OpenResult(result, loop=None):
    global is_exiting
    if is_exiting:  # If we're already in the exit process, don't do anything
        return

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

    info_color = "#d6d6d6"

    for i in range(num_rows):
        root.grid_rowconfigure(i, weight=1, minsize=screen_height // num_rows)

    for i in range(num_columns):
        root.grid_columnconfigure(i, weight=1, minsize=screen_width // num_columns)

    # Adjusting the 'info' frame size and position
    info = tk.Frame(root, width=screen_width, height=screen_height // 10, bg=info_color, borderwidth=1, relief="solid")
    info.grid(row=0, column=0, columnspan=14, rowspan=2, sticky="NESW")

    title = tk.Label(info, text="Encoded Result", font=title_font, bg=info_color)
    title.grid(row=0, padx=7, pady=(5, 0), columnspan=2, sticky="w")

    cipher_label = tk.Label(info, text="Cipher: ", font=bold_font, bg=info_color)
    cipher_label.grid(row=1, padx=(7, 0), column=0, sticky="w")
    cipher = tk.Label(info, text="", font=plain_font, bg=info_color)
    cipher.grid(row=1, padx=0, column=1, sticky="w")

    key_label = tk.Label(info, text="Key: ", font=bold_font, bg=info_color)
    key_label.grid(row=2, padx=(7, 0), column=0, sticky="w")
    key = tk.Label(info, text="", font=plain_font, bg=info_color)
    key.grid(row=2, column=1, sticky="w")

    text_area = tk.Text(root, wrap="word", font=plain_font, state="disabled")
    text_area.grid(row=2, column=0, columnspan=14, rowspan=17, sticky="nesw")

    def set_text(text):
        text_area.config(state="normal")
        text_area.delete("1.0", "end")
        text_area.insert("1.0", text)
        text_area.config(state="disabled")

    set_text(result.ciphertext)

    buttons = tk.Frame(root, bg=info_color, borderwidth=1, relief="solid")
    buttons.grid(row=19, column=0, columnspan=14, rowspan=1, sticky="NESW")

    button_columns = 14
    for i in range(button_columns):
        buttons.grid_columnconfigure(i, weight=1, minsize=screen_width // button_columns)
    buttons.grid_rowconfigure(0, weight=1)

    def exit_function():
        from Tools import Encoder
        Encoder.OpenCipherInput(Encoder, loop=root, gen_new=True)

    def switch_text_type():
        global is_ciphertext
        is_ciphertext = not is_ciphertext
        text = result.ciphertext if is_ciphertext else result.plaintext
        set_text(text)
        switch_button.config(text="Reveal Plaintext" if is_ciphertext else "Show Ciphertext")

    def show_key():
        key.config(text=result.keyword)
        show_cipher()

    def show_cipher():
        cipher.config(text=result.encoder)

    exit_button = tk.Button(buttons, text="Back", font=bold_font, relief="flat", borderwidth=1, command=exit_function)
    exit_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")

    switch_button = tk.Button(buttons, text="Reveal Plaintext", font=bold_font, relief="flat", borderwidth=1, command=switch_text_type)
    switch_button.grid(row=0, column=11, padx=3, pady=3, columnspan=2, sticky="nsew")

    show_key = tk.Button(buttons, text="Show Key", font=bold_font, relief="flat", borderwidth=1, command=show_key)
    show_key.grid(row=0, column=10, padx=3, pady=3, columnspan=1, sticky="nsew")

    show_key = tk.Button(buttons, text="Show Cipher", font=bold_font, relief="flat", borderwidth=1, command=show_cipher)
    show_key.grid(row=0, column=9, padx=3, pady=3, columnspan=1, sticky="nsew")

    root.mainloop()
