import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == "+":
            result.set(f"Result: {num1 + num2}")
        elif op == "-":
            result.set(f"Result: {num1 - num2}")
        elif op == "*":
            result.set(f"Result: {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                result.set("Cannot divide by 0")
            else:
                result.set(f"Result: {num1 / num2}")
    except ValueError:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

operator = tk.StringVar(value="+")

tk.OptionMenu(root, operator, "+", "-", "*", "/").pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()

root.mainloop()