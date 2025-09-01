import tkinter as tk

from Utility.Tools import *


class NihilistResult:
    keyword = []
    predicted_keyword = []
    keywords = []
    ciphertext = ""
    plaintext = ""
    keyword_len = 0

    is_exiting = False

    def __str__(self):
        return "Nihilist Cipher"

    def __init__(self, keyword, keywords, plaintext, ciphertext):
        self.keyword = keyword
        self.predicted_keyword = keyword
        self.keywords = keywords
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.keyword_len = len(keyword)

    def Display(self, loop):

        if self.is_exiting:
            return

        loop.destroy()

        root = tk.Tk()
        root.title("Nihilist Result")
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

        keyword_length_label = tk.Label(info, text="Keyword Length: ", font=bold_font, bg=info_color)
        keyword_length_label.grid(row=1, padx=(50, 0), column=3, sticky="w")
        keyword_length = tk.Label(info, text=str(self.keyword_len), font=plain_font, bg=info_color)
        keyword_length.grid(row=1, padx=0, column=4, sticky="w")

        predicted_label = tk.Label(info, text="Predicted Keyword: ", font=bold_font, bg=info_color)
        predicted_label.grid(row=1, padx=(6, 0), column=0, sticky="w")
        predicted = tk.Label(info, text=self.predicted_keyword, font=plain_font, bg=info_color)
        predicted.grid(row=1, column=1, sticky="w")

        key_label = tk.Label(info, text="Used Keyword: ", font=bold_font, bg=info_color)
        key_label.grid(row=2, padx=(6, 0), column=0, sticky="w")
        key = tk.Label(info, text=self.keyword, font=plain_font, bg=info_color)
        key.grid(row=2, column=1, sticky="w")

        IoC_label = tk.Label(info, text="Index of Coincidence: ", font=bold_font, bg=info_color)
        IoC_label.grid(row=2, padx=(50, 0), column=3, sticky="w")
        IoC = tk.Label(info, text=IndexOfCoincidence(StringFormat(self.plaintext)), font=plain_font, bg=info_color)
        IoC.grid(row=2, column=4, sticky="w")

        text_area = tk.Text(root, wrap="word", font=plain_font, state="disabled")
        text_area.grid(row=2, column=0, columnspan=12, rowspan=17, sticky="nesw")

        possibilities_area = tk.Text(root, wrap="word", font=bold_font, state="disabled", bg=info_color)
        possibilities_area.grid(row=2, column=12, columnspan=2, rowspan=17, sticky="nesw")

        def set_text(text, area):
            area.config(state="normal")
            area.delete("1.0", "end")
            area.insert("1.0", text)
            area.config(state="disabled")

        set_text(self.plaintext, text_area)
        possibilities_text = ""
        for key in self.keywords:
            possibilities_text += str(key)
            possibilities_text += "\n"
        set_text(possibilities_text, possibilities_area)

        possibilities_area.tag_configure("justify", justify='center')
        possibilities_area.tag_add("justify", 1.0, "end")

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
            self.keyword = [int(x) for x in keyword_input.get().split(" ")]
            from Tools import Decoder
            dec = Decoder.ciphers[str(self)]
            dec.ReEvaluate(self, root)

        exit_button = tk.Button(buttons, text="Back", font=bold_font, relief="flat", borderwidth=1,
                                command=exit_function)
        exit_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")

        retry_button = tk.Button(buttons, text="Retry", font=bold_font, relief="flat", borderwidth=1,
                                 command=retry_function)
        retry_button.grid(row=0, column=12, padx=3, pady=3, sticky="nsew")

        # keyword_input = tk.Text(buttons, wrap="none", font=input_font, relief="flat", borderwidth=1, height=1)
        key_display = self.keyword
        param = tk.StringVar(value=key_display)
        keyword_input = tk.Entry(root, font=input_font, relief="flat", borderwidth=1, textvariable=param)
        keyword_input.grid(row=19, column=0, columnspan=5, ipadx=3, ipady=3, padx=3, pady=3, sticky="nsew")
        keyword_input.lift()

        root.mainloop()
