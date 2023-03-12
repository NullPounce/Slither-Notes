from tkinter import *
from tkinter import filedialog

class Notepad:
    def __init__(self, **kwargs):
        self.root = Tk()
        self.filename = None
        self.textarea = Text(self.root, bg='#111111', fg='#FFFFFF', insertbackground='white', wrap=WORD)
        self.textarea.pack(expand=True, fill=BOTH)

        # Set transparency
        self.root.attributes("-alpha", 0.75)

        # Menu bar
        self.menubar = Menu(self.root, bg='#111111', fg='#FFFFFF', activebackground='#333333', activeforeground='#FFFFFF')
        self.filemenu = Menu(self.menubar, tearoff=0, bg='#111111', fg='#FFFFFF', activebackground='#333333',
                             activeforeground='#FFFFFF')
        self.editmenu = Menu(self.menubar, tearoff=0, bg='#111111', fg='#FFFFFF', activebackground='#333333',
                             activeforeground='#FFFFFF')
        self.helpmenu = Menu(self.menubar, tearoff=0, bg='#111111', fg='#FFFFFF', activebackground='#333333',
                             activeforeground='#FFFFFF')

        # File menu options
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Edit menu options
        self.editmenu.add_command(label="Cut", command=self.cut_text)
        self.editmenu.add_command(label="Copy", command=self.copy_text)
        self.editmenu.add_command(label="Paste", command=self.paste_text)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        # Help menu options
        self.helpmenu.add_command(label="About", command=self.show_about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar, bg='#111111')
        self.root.mainloop()

    def new_file(self):
        self.filename = None
        self.textarea.delete(1.0, END)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            self.textarea.delete(1.0, END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.textarea.get(1.0, END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.textarea.get(1.0, END))

    def cut_text(self):
        self.textarea.event_generate("<<Cut>>")

    def copy_text(self):
        self.textarea.event_generate("<<Copy>>")

    def paste_text(self):
        self.textarea.event_generate("<<Paste>>")

    def show_about(self):
        messagebox.showinfo("About", "Simple Notepad\nCreated by Your Name")

if __name__ == '__main__':
    notepad = Notepad()