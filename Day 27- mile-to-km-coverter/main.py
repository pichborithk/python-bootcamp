import tkinter as tk

window = tk.Tk()
window.title("Miles to Kilometer Converter")
w = 320
h = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)
window.geometry("%dx%d+%d+%d" % (w, h, x, y))
window.config(padx=50, pady=50)

mile_entry = tk.Entry(width=10)
mile_entry.insert(tk.END, string="0")
mile_entry.grid(row=0, column=1)

mile_label = tk.Label(text="Miles")
mile_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = tk.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)


def convert():
    mile = float(mile_entry.get())
    km = round(mile * 1.609, 2)
    result_label.config(text=f"{km}")


convert_button = tk.Button(text="Calculate", command=convert)
convert_button.grid(row=2, column=1)

window.mainloop()
