import tkinter as tk
from tkinter import ttk


def convert_octal_to_hex():
    octal_num = entry.get() # get captura texto do entry
    if any(digit in octal_num for digit in '89') or not octal_num.isnumeric():
        result_label.config(text="Por favor, insira um numero octal valido.")
    else:
        hex_num = hex(int(octal_num, 8))[2:]
        result_label.config(text=f"Hexadecimal: {hex_num}")
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"Hexadecimal: {hex_num}")
        result_text.tag_add("hex", "1.13", tk.END)
        result_text.tag_configure("hex", foreground="blue")
        result_text.insert(tk.END, f"Hexadecimal: {hex_num}")
        result_text.tag_add("center", "1.0", "end")


window = tk.Tk()
window.title("Conversor de Octal para Hexadecimal")
window.geometry("600x600")

tk.Label(window, text="Insira um numero em formato octal:").pack()
entry = tk.Entry(window)
entry.pack()

convert_button = tk.Button(window, text="Converta para Hexadecimal", command=convert_octal_to_hex)
convert_button.pack()

result_label = ttk.Label(window, text="",background="red",foreground="white",font=("Helvetica", 16))
result_label.pack()

result_text = tk.Text(window, height=1, background="red", font=("Helvetica", 16))
result_text.pack()
result_text.tag_configure("center", justify='center')


ttk.Separator(window, orient="horizontal").pack(fill="x")

window.mainloop()