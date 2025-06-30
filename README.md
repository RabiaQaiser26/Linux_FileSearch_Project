# 📁 File Founder – Recursive File Search Tool for Linux

**File Founder** is a powerful desktop application that allows users to perform **fast, recursive file searches** in any Linux directory using a **C++ backend** and a clean **Python GUI**. It combines the speed of system-level programming with the accessibility of graphical user interfaces.

---

## 🚀 Features

- 🔁 **Recursive Search** through nested directories
- 🖥️ **Python Tkinter GUI** with themed widgets (ttk)
- ⚙️ **C++ Backend** using `dirent.h`, `stat()`, and recursion
- 🔗 Seamless Python ↔ C++ integration via `subprocess`
- 📄 **Live Output Display** in a scrollable textbox
- 🛡️ Error handling for:
  - Missing executable
  - File not found
  - Invalid inputs
  - Directory permissions
- 💡 Educational example of **cross-language integration**

---

## 🧱 Project Structure

File-Founder/
│
├── searchfile.cpp # C++ backend source
├── file_founder_gui.py # Python frontend GUI
├── screenshots/ # (optional) GUI snapshots
│ ├── main_window.png
│ └── file_found.png
├── README.md # This file
└── LICENSE # (optional) License file


---

## 📸 Screenshots



| GUI Interface | File Found |
|---------------|------------|
|![Screenshot (66)](https://github.com/user-attachments/assets/b948e247-c677-466f-b838-eccb463c7dc6) | ![Screenshot 2025-06-09 174503](https://github.com/user-attachments/assets/cceb50e7-8828-4017-9a1d-dbdde94f181e) |

---

## 🛠️ Installation & Setup

### ✅ Step 1: Install Dependencies

sudo apt update
sudo apt install g++ python3-tk
 Step 2: Compile the C++ Backend
Use the following command to compile the C++ source code:


g++ searchfile.cpp -o searchfile
This will create an executable file named searchfile in the current directory.

✅ Step 3: Prepare the Python GUI Script
Make sure your file_founder_gui.py script is in the same directory as the compiled searchfile executable.


ls
# Expected output:
# searchfile  file_founder_gui.py
✅ Step 4: Run the Application
Start the GUI application using:


python3 file_founder_gui.py
⚠️ Optional: Make the Executable Runnable (if needed)
If you get a permission error when running searchfile, run:


chmod +x searchfile ```bash


## ⚙️ How It Works

1. The user enters:
   - A **start directory** (e.g., `/home/user`)
   - A **file name** (e.g., `report.txt`)
2. The **Python GUI** passes these inputs to the compiled `searchfile` C++ executable.
3. The **C++ program** performs a **recursive directory traversal** to find the file.
4. If found, the **full path** is printed and displayed in the GUI's result area.
5. If not found, a user-friendly message is shown.

---

## 🧩 Technologies Used

| Layer         | Technology                       |
|---------------|----------------------------------|
| **Frontend**  | Python `Tkinter`, `ttk` widgets  |
| **Backend**   | C++ (`<dirent.h>`, `<stat.h>`)   |
| **Communication** | Python `subprocess` module   |
| **Platform**  | Linux (Ubuntu / Debian / Fedora) |

---

## 🧪 Troubleshooting

| Problem                  | Solution                                                        |
|--------------------------|-----------------------------------------------------------------|
| ❌ **Executable not found**  | Recompile `searchfile.cpp` and keep it in the same directory   |
| 🔒 **Permission denied**     | Use `sudo` or update directory permissions (`chmod`)           |
| 📭 **No results**            | Double-check spelling, case sensitivity, and file path         |
| 💥 **Segmentation fault**    | Avoid restricted system folders or debug using `gdb`           |



