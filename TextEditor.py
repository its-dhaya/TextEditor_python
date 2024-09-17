from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror
from tkinter import *
from tkinter import ttk  # For better-looking widgets
from tkinter.font import Font, families

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    if filename is None:
        saveAs()  # If no filename, use Save As
    else:
        t = text.get(0.0, END)
        with open(filename, 'w') as f:
            f.write(t.strip())

def saveAs():
    global filename
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:  # If the user cancels save
        return
    filename = f.name
    t = text.get(0.0, END)
    try:
        f.write(t.strip())
    except:
        showerror(title="oops", message="Unable to save file")

def openFile():
    f = askopenfile(mode='r')
    if f is None:  # If the user cancels open
        return
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def maximizeWindow():
    root.state('zoomed')  # Maximized window

def minimizeWindow():
    root.state('iconic')  # Minimize the window

def normalWindow():
    root.state('normal')  # Restore window to normal size

def applyDarkTheme():
    root.config(bg='#2e2e2e')  # Background color for the main window
    menubar.config(bg='#1e1e1e', fg='#ffffff')  # Menubar colors
    filemenu.config(bg='#1e1e1e', fg='#ffffff')  # File menu colors
    viewmenu.config(bg='#1e1e1e', fg='#ffffff')  # View menu colors
    text.config(bg='#1e1e1e', fg='#d4d4d4', insertbackground='white')  # Text widget colors
    scrollbar.config(bg='#1e1e1e', troughcolor='#2e2e2e')
    theme_var.set('Dark')

def applyLightTheme():
    root.config(bg='#ffffff')  # Background color for the main window
    menubar.config(bg='#f0f0f0', fg='#000000')  # Menubar colors
    filemenu.config(bg='#f0f0f0', fg='#000000')  # File menu colors
    viewmenu.config(bg='#f0f0f0', fg='#000000')  # View menu colors
    text.config(bg='#ffffff', fg='#000000', insertbackground='black')  # Text widget colors
    scrollbar.config(bg='#ffffff', troughcolor='#f0f0f0')
    theme_var.set('Light')

def toggleTheme():
    if theme_var.get() == 'Dark':
        applyLightTheme()
    else:
        applyDarkTheme()

def changeFont(font_name):
    text.config(font=(font_name, 12))

def showFontSelector():
    font_selector = Toplevel(root)
    font_selector.title("Select Font")
    font_selector.geometry("300x400")

    # Create a scrollbar
    scrollbar = Scrollbar(font_selector)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create a Listbox
    font_listbox = Listbox(font_selector, yscrollcommand=scrollbar.set)
    font_listbox.pack(fill=BOTH, expand=True)

    scrollbar.config(command=font_listbox.yview)

    # Populate the Listbox with available fonts
    fonts = families(root)
    for font in fonts:
        font_listbox.insert(END, font)

    # Bind the select event
    font_listbox.bind("<Double-1>", lambda event: changeFont(font_listbox.get(font_listbox.curselection())))

# Create the main window
root = Tk()
root.title("D-editor")
root.geometry("800x600")  # Default size, but resizable
root.state('normal')  # Start in normal state (not maximized)

# Set the custom icon
photo = PhotoImage(file="C:\\Users\\dhaya\\Downloads\\code.png")
root.iconphoto(False, photo)

# Add Text widget inside a Frame with Scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(frame, wrap=NONE, yscrollcommand=scrollbar.set, font=("Arial", 12), undo=True)
text.pack(fill=BOTH, expand=True)
scrollbar.config(command=text.yview)

# Create Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Add maximize, minimize, and restore options in View menu
viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Maximize", command=maximizeWindow)
viewmenu.add_command(label="Minimize", command=minimizeWindow)
viewmenu.add_command(label="Restore", command=normalWindow)

# Add theme toggle option
thememenu = Menu(menubar, tearoff=0)
theme_var = StringVar(value='Dark')  # Default theme
thememenu.add_command(label="Toggle Theme", command=toggleTheme)

# Add font selection menu
fontmenu = Menu(menubar, tearoff=0)
fontmenu.add_command(label="Select Font...", command=showFontSelector)

# Add menus to the menubar
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="View", menu=viewmenu)
menubar.add_cascade(label="Theme", menu=thememenu)
menubar.add_cascade(label="Fonts", menu=fontmenu)

root.config(menu=menubar)

# Apply default theme
applyDarkTheme()

# Run the application
root.mainloop()
