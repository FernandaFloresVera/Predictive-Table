import tkinter as tk
from AnalizadorSintactico import analize

def run():
    window = tk.Tk()
    window.title("Analizador de sintaxis")
    window.geometry("700x500")

    input_label = tk.Label(window, text="Entrada", fg="#8a2be2")
    input_label.pack()

    input_text = tk.Text(window, height=10, width=70)
    input_text.insert(tk.END, "")
    input_text.pack()

    def analize_input():
        input_text_content = input_text.get("1.0", "end-1c")
        result, history = analize(input_text_content)

        if result:
            result_label.config(text="Cadena válida", fg="#008000")
        else:
            result_label.config(text="Cadena inválida", fg="#ff4500")
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, history)

    analize_button = tk.Button(window, text="Analizar", command=analize_input, bg="#8a2be2", fg="#fff")
    analize_button.pack(pady=10)

    result_label = tk.Label(window, text="", fg="#8a2be2")
    result_label.pack()

    output_area = tk.Text(window, height=15, width=70)
    output_area.pack()

    window.mainloop()
