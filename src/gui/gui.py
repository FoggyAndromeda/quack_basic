from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
import os
import tokenizer.tokenizer as tokenizer
import interpreter.interpreter as interpreter


class Editor:
    aboutmes = """https://github.com/FoggyAndromeda/quack_basic

Interpreter by Andrey Stoyanovski
GUI by Aleksandr Savinov"""

    file_ = None
    root = Tk()
    root.title("QBASIC code editor - New File")
    root.minsize(500, 500)
    root.option_add('*tearOff', FALSE)
    basefont = font.Font(family='Courier New', size=10)
    mainframe = ttk.Frame(root, padding="4 4 4 4")
    code = Text(mainframe, font=basefont)
    output = Text(mainframe, background="white", font=basefont,
                  height=code['height']/2, state="disabled")
    scr1 = ttk.Scrollbar(mainframe, orient=VERTICAL, command=code.yview)
    code.configure(yscrollcommand=scr1.set)
    scr2 = ttk.Scrollbar(mainframe, orient=VERTICAL, command=output.yview)
    output.configure(yscrollcommand=scr2.set)
    menubar = Menu(root)
    menu_file = Menu(menubar)
    menu_edit = Menu(menubar)
    menu_run = Menu(menubar)
    menu_help = Menu(menubar)
    menu_view = Menu(menubar)
    saved = True

    def __init__(self):

        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(3, weight=1)

        ttk.Label(self.mainframe, text='Code:', justify='left',
                  width=10).grid(row=0, column=0, sticky=(W))
        self.code.grid(row=1, column=0, sticky=(N, W, E, S))
        self.code.bind("<KeyPress-Return>", self.check)
        self.code.bind("<KeyPress>", self.setstate)
        self.root.bind("<KeyPress-F5>", self.run)

        self.output.config(state="normal")
        self.output.config(state="disabled")
        ttk.Label(self.mainframe, text='Output:', justify='left',
                  width=10).grid(row=2, column=0, sticky=(W))
        self.output.grid(row=3, column=0, sticky=(N, W, E, S))

        self.scr2.grid(row=3, column=1, sticky=(N, S))
        self.scr1.grid(row=1, column=1, sticky=(N, S))

        self.menu_file.add_command(label="New file", command=self.newfile)
        self.menu_file.add_command(label="Open file", command=self.openfile)
        self.menu_file.add_command(label="Save file", command=self.savefile)
        self.menu_file.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(menu=self.menu_file, label="File")

        self.menu_edit.add_command(label="Cut", command=self.cut)
        self.menu_edit.add_command(label="Copy", command=self.copy)
        self.menu_edit.add_command(label="Paste", command=self.paste)
        self.menubar.add_cascade(menu=self.menu_edit, label="Edit")

        self.menu_run.add_command(label="Run", command=self.run)
        self.menubar.add_cascade(menu=self.menu_run, label="Run")

        self.menu_help.add_command(label="About", command=self.about)
        self.menubar.add_cascade(menu=self.menu_help, label="Help")

        self.menu_view.add_command(label="Clear output", command=self.clear_output)
        self.menubar.add_cascade(menu=self.menu_view, label="View")

        self.root['menu'] = self.menubar
        self.code.focus_set()

    def newfile(self):
        if self.saved == False:
            val = messagebox.askyesnocancel(
                "File not saved", "The current file has changes, that are not saved. Do you want to save?")
            if val == None:
                return
            if val:
                self.savefile()
                return
        self.file_ = None
        self.root.title("QBASIC code editor - New File")
        self.code.delete(1.0, END)

    def openfile(self):
        if self.saved == False:
            val = messagebox.askyesnocancel(
                "File not saved", "The current file has changes, that are not saved. Do you want to save?")
            if val == None:
                return
            if val:
                self.savefile()
                return
        self.file_ = filedialog.askopenfilename(defaultextension=".BAS", filetypes=[
                                                ("All Files", "*.*"), ("QBASIC code", "*.BAS")])
        self.root.title("QBASIC code editor - "+os.path.basename(self.file_))
        content = open(self.file_, "r")
        self.code.delete(1.0, END)
        self.code.insert(1.0, content.read())
        content.close()
        self.code.focus_set()
        self.code.mark_set(INSERT, 1.0)

    def savefile(self):
        if self.file_ == None:
            self.file_ = filedialog.asksaveasfilename(initialfile='NewCode.BAS', defaultextension=".BAS", filetypes=[
                                                      ("All Files", "*.*"), ("QBASIC code", "*.BAS")])
            if self.file_ != '':
                self.root.title("QBASIC code editor - " +
                                os.path.basename(self.file_))
                dest = open(self.file_, "w")
                dest.write(self.code.get(1.0, END))
                dest.close()
            else:
                self.file_ = None
        else:
            dest = open(self.file_, "w")
            dest.write(self.code.get(1.0, END))
            dest.close()
        self.saved = True

    def cut(self):
        self.code.event_generate('<<Cut>>')

    def copy(self):
        self.code.event_generate('<<Copy>>')

    def paste(self):
        self.code.event_generate('<<Paste>>')

    def run(self, event=None):
        self.savefile()

        try:
            interinstance = interpreter.Interpreter()
            interinstance.run_file(self.file_)
            output = interinstance.get_buffer()
            output = "\n".join(output)
        except Exception as e:
            output = str(e)

        output += "\n--END OF PROGRAMM--\n"
        self.output.config(state="normal")
        self.output.insert(END, output)
        self.output.config(state="disabled")
        self.output.see("end")

    def setstate(self, event):
        self.saved = False

    def check(self, event):
        x, y = map(int, event.widget.index(INSERT).split("."))
        line = event.widget.get("{}.0".format(x), "{}.{}".format(x, y))
        try:
            instoken = tokenizer.Tokenizer(line)
            instoken.to_tokens()
        except:
            messagebox.showerror(
                "Syntax error", "There is a mistake in line {}".format(x))

    def quit(self):
        self.savefile()
        self.root.destroy()

    def launch(self):
        self.root.mainloop()

    def clear_output(self):
        self.output.config(state="normal")
        self.output.delete(1.0, END)
        self.output.config(state="disabled")

    def about(self):
        messagebox.showinfo("QBASIC code editor", self.aboutmes)


if __name__ == "__main__":
    instance = Editor()
    instance.launch()
