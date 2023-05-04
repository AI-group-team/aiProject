
import tkinter as tk

roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_decimal():
    roman_numeral = entry.get()
    decimal_num = 0
    prev_num = 0
    
    for i in range(len(roman_numeral)-1, -1, -1):
        current_num = roman_dict[roman_numeral[i]]
        if current_num < prev_num:
            decimal_num -= current_num
        else:
            decimal_num += current_num
        prev_num = current_num
    
    result_label.config(text=f"The decimal equivalent of {roman_numeral} is {decimal_num}")

root = tk.Tk()
root.title("Roman to Decimal Converter")
root.geometry("400x400")
root.configure(bg='#64a1de')

label = tk.Label(root, text="Enter a Roman numeral between 1 and 3999:", bg='#64a1de')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Convert", command=roman_to_decimal)
button.pack()

result_label = tk.Label(root, text="", bg='#f2f2f2')
result_label.pack()

# Animated text at the bottom of the window
text = tk.Label(root, text="NAME Temesgen Debebe ID = 0888/12___", font=("Helvetica", 12), bg='#f2f2f2')
text.pack(side="bottom", pady=10)

def animate():
    text.config(text=text["text"][1:] + text["text"][0])
    text.after(200, animate)

animate()

root.mainloop()
