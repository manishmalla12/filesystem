import os
import tkinter as tk
import tkinter.simpledialog
from tkinter import filedialog, messagebox

class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Simple File System")
        self.root.geometry("600x300") 
        self.root.configure(bg="#34495e")  

        welcome_label = tk.Label(root, text="Welcome to the File System application!", bg="#34495e", fg="#ecf0f1", font=("Helvetica", 16))
        welcome_label.pack(padx=20, pady=40)

        enter_button = tk.Button(root, text="Enter", command=self.enter_file_manager, bg="#2ecc71", fg="white", width=15)
        enter_button.pack(pady=10)

        exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#e74c3c", fg="white", width=15)
        exit_button.pack()

    def enter_file_manager(self):
        self.root.destroy() 
        main_root = tk.Tk()
        app = FileManager(main_root)
        main_root.mainloop()

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File System")
        self.root.geometry("600x400")  
        self.root.configure(bg="#34495e")  

        button_color = "#3498db" 
        text_color = "white"  

        self.create_file_button = tk.Button(root, text="Create File", command=self.create_file, bg=button_color, fg=text_color, height=2, width=20)
        self.read_file_button = tk.Button(root, text="Read File", command=self.read_file, bg=button_color, fg=text_color, height=2, width=20)
        self.update_file_button = tk.Button(root, text="Update File", command=self.update_file, bg=button_color, fg=text_color, height=2, width=20)
        self.delete_file_button = tk.Button(root, text="Delete File", command=self.delete_file, bg=button_color, fg=text_color, height=2, width=20)

        self.create_dir_button = tk.Button(root, text="Create Directory", command=self.create_directory, bg=button_color, fg=text_color, height=2, width=20)
        self.delete_dir_button = tk.Button(root, text="Delete Directory", command=self.delete_directory, bg=button_color, fg=text_color, height=2, width=20)

        self.create_file_button.pack(pady=10)
        self.read_file_button.pack(pady=10)
        self.update_file_button.pack(pady=10)
        self.delete_file_button.pack(pady=10)
        self.create_dir_button.pack(pady=10)
        self.delete_dir_button.pack(pady=10)

    def create_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                pass

    def read_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                messagebox.showinfo("File Content", content)

    def update_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r+') as file:
                content = file.read()
                new_content = input("Enter new content: ")
                file.seek(0)
                file.write(new_content + '\n' + content)

    def delete_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            os.remove(file_path)
            messagebox.showinfo("Info", "File deleted successfully.")

    def create_directory(self):
        new_dir_name = tk.simpledialog.askstring("Create Directory", "Enter directory name:")

        if new_dir_name:
            desktop_path = os.path.expanduser("C:\\Users\Lenovo\Desktop")  # Path of the Directory 
            new_dir_path = os.path.join("C:\\Users\Lenovo\Desktop", new_dir_name)
            
            try:
                os.mkdir(new_dir_path)
                if os.path.exists(new_dir_path):
                    messagebox.showinfo("Info", "Directory created successfully.")
                else:
                    messagebox.showerror("Error", "Failed to create directory.")
            except OSError as e:
                messagebox.showerror("Error", f"Failed to create directory: {e}")


    def delete_directory(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            os.rmdir(dir_path)
            messagebox.showinfo("Info", "Directory deleted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    welcome = WelcomeWindow(root)
    root.mainloop()
