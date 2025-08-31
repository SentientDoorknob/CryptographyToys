import tkinter as tk
from Utility.Tools import *

class SubstitutionResult:
    keyword = ""
    predicted_keyword = ""
    ciphertext = ""
    plaintext = ""
    iterations = 0
    encryption = ""

    def __str__(self):
        return "Substitution Cipher"

    def __init__(self, keyword, plaintext, ciphertext, iterations, encoding):
        self.keyword = keyword
        self.predicted_keyword = keyword
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.iterations = iterations
        self.encryption = encoding
        
    def Display(self, loop):
        if loop:
            loop.destroy()

        root = tk.Tk()
        root.title("Substitution Result")
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

        iterations_label = tk.Label(info, text="# Iterations: ", font=bold_font, bg=info_color)
        iterations_label.grid(row=1, padx=(50, 0), column=3, sticky="w")
        iterations = tk.Label(info, text=str(self.iterations), font=plain_font, bg=info_color)
        iterations.grid(row=1, padx=0, column=4, sticky="w")

        predicted_label = tk.Label(info, text="Predicted Keyword: ", font=bold_font, bg=info_color)
        predicted_label.grid(row=1, padx=(6, 0), column=0, sticky="w")
        predicted = tk.Label(info, text=self.predicted_keyword, font=plain_font, bg=info_color)
        predicted.grid(row=1, column=1, sticky="w")

        key_label = tk.Label(info, text="Used Keyword: ", font=bold_font, bg=info_color)
        key_label.grid(row=2, padx=(6, 0), column=0, sticky="w")
        key = tk.Label(info, text=self.keyword, font=plain_font, bg=info_color)
        key.grid(row=2, column=1, sticky="w")

        IoC_label = tk.Label(info, text="Fitness: ", font=bold_font, bg=info_color)
        IoC_label.grid(row=2, padx=(50, 0), column=3, sticky="w")
        IoC = tk.Label(info, text=round(SubstitutionFitness(self.plaintext), 6), font=plain_font, bg=info_color)
        IoC.grid(row=2, column=4, sticky="w")

        predicted_encryption_label = tk.Label(info, text="Predicted Encryption Key: ", font=bold_font, bg=info_color)
        predicted_encryption_label.grid(row=1, padx=(50, 0), column=5, sticky="w")
        predicted_encryption = tk.Label(info, text=InvertKey(self.predicted_keyword), font=plain_font, bg=info_color)
        predicted_encryption.grid(row=1, column=6, sticky="w")

        encryption_label = tk.Label(info, text="Used Encryption Key: ", font=bold_font, bg=info_color)
        encryption_label.grid(row=2, padx=(50, 0), column=5, sticky="w")
        encryption = tk.Label(info, text=self.encryption, font=plain_font, bg=info_color)
        encryption.grid(row=2, column=6, sticky="w")

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
            from Tools import HillClimber
            HillClimber.OpenCipherInput(root, gen_new=True)

        def retry_function():
            from Decoders.Substitution.SubstitutionDecoder import SubstitutionDecoder
            from Encoders.Ciphers.SubstitutionEncoder import SubstitutionEncoder
            self.keyword = SubstitutionEncoder(0).ParseKey(keyword_input.get())
            SubstitutionDecoder().ReEvaluate(self, root)

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