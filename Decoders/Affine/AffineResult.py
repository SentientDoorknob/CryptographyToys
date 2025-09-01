import tkinter as tk

from Utility.Tools import *


class AffineResult:
    keyword = ""
    predicted_et = ""
    ciphertext = ""
    plaintext = ""
    et = []

    is_exiting = False

    def __str__(self):
        return "Affine Cipher"

    def __init__(self, keyword, plaintext, ciphertext, et):
        self.keyword = keyword
        self.predicted_et = et
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.et = et

    def Display(self, loop):

        if self.is_exiting:
            return

        loop.destroy()

        root = tk.Tk()
        root.title("Affine Result")
        root.attributes("-fullscreen", True)
        root.tk.call('tk', 'scaling', root.winfo_fpixels('1i') / 72.0)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        title_font = ("Consolas", 14, "bold")
        plain_font = ("Consolas", 12, "normal")
        bold_font = ("Consolas", 12, "bold")
        input_font = ("Consolas", 20, "normal")

        num_rows = 20
        num_columns = 14

        info_color = "#d6d6d6"

        for i in range(num_rows):
            root.grid_rowconfigure(i, weight=1, minsize=screen_height // num_rows)

        for i in range(num_columns):
            root.grid_columnconfigure(i, weight=1, minsize=screen_width // num_columns)

        # Adjusting the 'info' frame size and position
        info = tk.Frame(root, width=screen_width, height=screen_height // 10, bg=info_color, borderwidth=1,
                        relief="solid")
        info.grid(row=0, column=0, columnspan=14, rowspan=2, sticky="NESW")

        title = tk.Label(info, text="Practice Problem", font=title_font, bg=info_color)
        title.grid(row=0, padx=7, pady=(5, 0), columnspan=2, sticky="w")

        used_label = tk.Label(info, text="Used Keyword: ", font=bold_font, bg=info_color)
        used_label.grid(row=1, padx=(50, 0), column=3, sticky="w")
        used = tk.Label(info, text=str(self.keyword), font=plain_font, bg=info_color)
        used.grid(row=1, padx=0, column=4, sticky="w")

        predicted_et = tk.Label(info, text="Predicted ET: ", font=bold_font, bg=info_color)
        predicted_et.grid(row=1, padx=(6, 0), column=0, sticky="w")
        predicted = tk.Label(info, text=self.predicted_et, font=plain_font, bg=info_color)
        predicted.grid(row=1, column=1, sticky="w")

        et_label = tk.Label(info, text="Used ET: ", font=bold_font, bg=info_color)
        et_label.grid(row=2, padx=(6, 0), column=0, sticky="w")
        et = tk.Label(info, text=self.et, font=plain_font, bg=info_color)
        et.grid(row=2, column=1, sticky="w")

        IoC_label = tk.Label(info, text="Index of Coincidence: ", font=bold_font, bg=info_color)
        IoC_label.grid(row=2, padx=(50, 0), column=3, sticky="w")
        IoC = tk.Label(info, text=IndexOfCoincidence(self.plaintext), font=plain_font, bg=info_color)
        IoC.grid(row=2, column=4, sticky="w")

        text_area = tk.Text(root, wrap="word", font=plain_font, state="disabled")
        text_area.grid(row=2, column=0, columnspan=14, rowspan=17, sticky="nesw")

        def set_text(text, area):
            area.config(state="normal")
            area.delete("1.0", "end")
            area.insert("1.0", text)
            area.config(state="disabled")

        set_text(self.plaintext, text_area)

        buttons = tk.Frame(root, bg=info_color, borderwidth=1, relief="solid")
        buttons.grid(row=19, column=0, columnspan=14, rowspan=1, sticky="NESW")

        button_columns = 14
        for i in range(button_columns):
            buttons.grid_columnconfigure(i, weight=1, minsize=screen_width // button_columns)
        buttons.grid_rowconfigure(0, weight=1)

        def exit_function():
            from Tools import Decoder
            Decoder.OpenCipherInput(Decoder, root, gen_new=True)

        def retry_function():
            self.et = keyword_input.get().split(" ")
            from Tools import Decoder
            dec = Decoder.ciphers[str(self)]
            dec.ReEvaluate(self, root)

        def swap_function():
            self.et = [self.et[1], self.et[0]]
            from Tools import Decoder
            dec = Decoder.ciphers[str(self)]
            dec.ReEvaluate(self, root)

        exit_button = tk.Button(buttons, text="Back", font=bold_font, relief="flat", borderwidth=1,
                                command=exit_function)
        exit_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")

        retry_button = tk.Button(buttons, text="Retry", font=bold_font, relief="flat", borderwidth=1,
                                 command=retry_function)
        retry_button.grid(row=0, column=12, padx=3, pady=3, sticky="nsew")

        swap_button = tk.Button(buttons, text="Swap", font=bold_font, relief="flat", borderwidth=1,
                                 command=swap_function)
        swap_button.grid(row=0, column=11, padx=3, pady=3, sticky="nsew")

        # keyword_input = tk.Text(buttons, wrap="none", font=input_font, relief="flat", borderwidth=1, height=1)
        param = tk.StringVar(value=self.et)
        keyword_input = tk.Entry(root, font=input_font, relief="flat", borderwidth=1, textvariable=param)
        keyword_input.grid(row=19, column=0, columnspan=5, ipadx=3, ipady=3, padx=3, pady=3, sticky="nsew")
        keyword_input.lift()

        root.mainloop()
