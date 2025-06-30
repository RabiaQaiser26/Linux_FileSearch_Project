import subprocess
import tkinter as tk
from tkinter import messagebox, ttk  # Import ttk for themed widgets

def search_file():
    directory = dir_entry.get().strip()
    filename = file_entry.get().strip()

    if not directory or not filename:
        messagebox.showerror("Error", "Both fields are required.")
        return

    try:
        result = subprocess.run(
            ["./searchfile", directory, filename],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                output_text.config(state='normal')
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, output)
                output_text.config(state='disabled')
                messagebox.showinfo("Search Result", "File found!")
            else:
                messagebox.showinfo("Search Result", "File not found.")
        else:
            messagebox.showerror("Error", result.stderr.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "C++ executable './searchfile' not found.\nMake sure it's compiled and in the same directory.")
    except Exception as e:
        messagebox.showerror("Exception", str(e))

# --- GUI setup ---
root = tk.Tk()
root.title("Advanced File Search")
root.geometry("600x500")
root.resizable(False, False)

# Apply a modern theme
style = ttk.Style()
style.theme_use("clam")

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Input section
input_frame = ttk.LabelFrame(main_frame, text="Search Parameters", padding="15 15 15 15")
input_frame.pack(pady=10, fill=tk.X)

tk.Label(input_frame, text="Start Directory (e.g., /home):", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(0, 2))
dir_entry = ttk.Entry(input_frame, width=70)
dir_entry.pack(fill=tk.X, expand=True)

tk.Label(input_frame, text="File Name to Search (e.g., file.txt):", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 2))
file_entry = ttk.Entry(input_frame, width=70)
file_entry.pack(fill=tk.X, expand=True)

# Search button
search_button = ttk.Button(main_frame, text="Search File", command=search_file, style="Accent.TButton")
search_button.pack(pady=15)

# Customize button style
style.map("Accent.TButton",
    foreground=[('pressed', 'white'), ('active', 'white')],
    background=[('pressed', '!focus', '#0056b3'), ('active', '#007bff')],
    relief=[('pressed', 'groove'), ('!pressed', 'ridge')]
)
style.configure("Accent.TButton",
    font=("Arial", 11, "bold"),
    background="#007bff",
    foreground="white",
    padding=10,
    relief="raised"
)

# Output section
output_frame = ttk.LabelFrame(main_frame, text="Search Results", padding="15 15 15 15")
output_frame.pack(pady=10, fill=tk.BOTH, expand=True)

output_text = tk.Text(output_frame, height=10, wrap="word", state='disabled',
                      font=("Consolas", 10), bg="#f0f0f0", fg="#333",
                      relief="sunken", borderwidth=2)
output_text.pack(fill=tk.BOTH, expand=True)

# Add a scrollbar to the output text area
scrollbar = ttk.Scrollbar(output_frame, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
