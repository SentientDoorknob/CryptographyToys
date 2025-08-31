import tkinter as tk

from Tools import Profiler
from Utility.Tools import *


def ShowResult(result, loop=None):
    if loop:
        loop.destroy()

    info_color = "#d6d6d6"
    frequency_color = "#f0f0f0"
    stats_color = "#eaeaea"
    bigram_color = "#e0e0e0"
    monogram_color = "#dfdfdf"

    # Initialising root
    root = tk.Tk()
    root.title("Cipher Profile")
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
    info.grid(row=0, column=0, columnspan=14, rowspan=1, sticky="nsew")

    title = tk.Label(info, text="Cipher Profile", font=title_font, bg=info_color)
    title.grid(row=0, padx=7, pady=(5, 0), columnspan=2, sticky="w")

    buttons = tk.Frame(root, bg=info_color, borderwidth=1, relief="solid")
    buttons.grid(row=19, column=0, columnspan=14, rowspan=1, sticky="nsew")

    fa_width = 3
    frequency_analysis = tk.Frame(root, borderwidth=1, relief="solid", bg=frequency_color)
    frequency_analysis.grid(column=num_columns - fa_width, columnspan=fa_width, row=1, rowspan=18, sticky="nsew")

    for i in range(26):
        frequency_analysis.grid_rowconfigure(i, weight=1, minsize=(screen_height * 9 / 10) // 26)
    for i in range(4):
        frequency_analysis.grid_columnconfigure(i, weight=1)

    labels = []
    for row in range(26):
        letter = chr(row + 65)
        expected = ENGLISH_LETTER_FREQ[row]
        observed = round(result.letterFrequencies[row], 4)
        difference = round(abs(expected - observed), 4)

        letter_label = tk.Label(frequency_analysis, text=letter, font=bold_font, bg=frequency_color)
        letter_label.grid(row=row, column=0, padx=15, sticky="news")
        labels.append(letter_label)

        expected_label = tk.Label(frequency_analysis, text=str(expected), font=plain_font, bg=frequency_color)
        expected_label.grid(row=row, column=1, padx=15, sticky="news")
        labels.append(expected_label)

        observed_label = tk.Label(frequency_analysis, text=str(observed), font=plain_font, bg=frequency_color)
        observed_label.grid(row=row, column=2, padx=15, sticky="news")
        labels.append(observed_label)

        difference_label = tk.Label(frequency_analysis, text=str(difference), font=plain_font, bg=frequency_color)
        difference_label.grid(row=row, column=3, padx=15, sticky="news")
        labels.append(difference_label)

    stats_width, stats_partition = 2, 8

    display_stats = {
        "Index OC": result.indexOC,
        "Chi Squared": result.chiSquared,
        "Friedman Test": result.friedmanTest,
        "Mono Entropy": result.entropy,
        "Tri Entropy": result.triEntropy,
        "Cosine Entropy": result.cosineFitness,
        "Sub. Fitness": result.substitutionFitness,
        "Eng. Fitness": result.englishFitness,
    }

    stats_num = len(display_stats)
    stats = tk.Frame(root, borderwidth=1, relief="solid", bg=stats_color)
    stats.grid(column=num_columns - fa_width - stats_width, columnspan=stats_width, row=1, rowspan=stats_partition,
               sticky="news")

    for i in range(stats_num):
        stats.grid_rowconfigure(i, weight=1)
    for i in range(2):
        stats.grid_columnconfigure(i, weight=1)

    for i, (descriptor, stat) in enumerate(display_stats.items()):
        desc_label = tk.Label(stats, text=descriptor, bg=stats_color, font=bold_font)
        desc_label.grid(row=i, padx=10, sticky="w")
        
        stat_label = tk.Label(stats, text=stat, bg=stats_color, font=plain_font)
        stat_label.grid(row=i, column=1, padx=10, sticky="w")
    
    bigram_span = 5
    bigram_num = len(result.commonBigrams)
    
    bigram_display = tk.Frame(root, borderwidth=1, relief="solid", bg=bigram_color)
    bigram_display.grid(column=num_columns - fa_width - stats_width, columnspan=stats_width, row=stats_partition + 1, rowspan=bigram_span, sticky="news")

    for i in range(bigram_num):
        bigram_display.grid_rowconfigure(i, weight=1)
    for i in range(4):
        bigram_display.grid_columnconfigure(i, weight=1)
    
    for i, (bigram, frequency) in enumerate(result.commonBigrams):
        english_bigram, english_frequency = MOST_COMMON_BIGRAMS[i]
        
        bigram_label = tk.Label(bigram_display, text=bigram, bg=bigram_color, font=bold_font)
        bigram_label.grid(row=i, padx=10, sticky="w")

        frequency_label = tk.Label(bigram_display, text=frequency, bg=bigram_color, font=plain_font)
        frequency_label.grid(row=i, column=1, padx=10, sticky="w")

        sample_bigram_label = tk.Label(bigram_display, text=english_bigram, bg=bigram_color, font=bold_font)
        sample_bigram_label.grid(row=i, column=2, padx=10, sticky="w")
        
        sample_frequency_label = tk.Label(bigram_display, text=english_frequency, bg=bigram_color, font=plain_font)
        sample_frequency_label.grid(row=i, column=3, padx=10, sticky="w")

    monogram_num = len(result.commonMonograms)

    monogram_display = tk.Frame(root, borderwidth=1, relief="solid", bg=monogram_color)
    monogram_display.grid(column=num_columns - fa_width - stats_width, columnspan=stats_width, row=stats_partition + bigram_span + 1,
                        rowspan=num_rows - 2 - bigram_span - stats_partition, sticky="news")

    for i in range(monogram_num):
        monogram_display.grid_rowconfigure(i, weight=1)
    for i in range(4):
        monogram_display.grid_columnconfigure(i, weight=1)

    for i, (monogram, frequency) in enumerate(result.commonMonograms):
        english_monogram, english_frequency = MOST_COMMON_MONOGRAMS[i]

        monogram_label = tk.Label(monogram_display, text=monogram, bg=monogram_color, font=bold_font)
        monogram_label.grid(row=i, padx=10, sticky="w")

        frequency_label = tk.Label(monogram_display, text=frequency, bg=monogram_color, font=plain_font)
        frequency_label.grid(row=i, column=1, padx=10, sticky="w")

        sample_monogram_label = tk.Label(monogram_display, text=english_monogram, bg=monogram_color, font=bold_font)
        sample_monogram_label.grid(row=i, column=2, padx=10, sticky="w")

        sample_frequency_label = tk.Label(monogram_display, text=english_frequency, bg=monogram_color, font=plain_font)
        sample_frequency_label.grid(row=i, column=3, padx=10, sticky="w")

    button_columns = 14
    for i in range(button_columns):
        buttons.grid_columnconfigure(i, weight=1, minsize=screen_width // button_columns)
    buttons.grid_rowconfigure(0, weight=1)
    
    text_area = tk.Text(root, wrap="word", font=plain_font, state="normal", borderwidth=1)
    text_area.grid(row=1, column=0, columnspan=14 - fa_width - stats_width, rowspan=18, sticky="nesw")
    
    def set_text(text):
        text_area.config(state="normal")
        text_area.delete("1.0", "end")
        text_area.insert("1.0", text)
        text_area.config(state="disabled")
        
    set_text(result.text)

    def Back():
        Profiler.OpenTextInput(gen_new=True, loop=root)

    back_button = tk.Button(buttons, text="Back", font=bold_font, command=lambda: Back(), relief="flat")
    back_button.grid(row=0, column=13, padx=3, pady=3, sticky="nsew")

    root.mainloop()
