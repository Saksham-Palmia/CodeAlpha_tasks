import tkinter as tk

def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def generate_fib():
    try:
        n = int(entry.get())
        series = [fibo(i) for i in range(n)]
        result_label.config(text="Fibonacci Series: " + str(series))
    except ValueError:
        result_label.config(text="Please enter a valid integer")

#main window
root = tk.Tk()
root.title("Fibonacci Series Generator")
root.configure(bg="beige")
root.geometry("600x600")

# Create widgets
label = tk.Label(root, text="Enter the number of terms:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Series", command=generate_fib)
generate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the application
root.mainloop()
