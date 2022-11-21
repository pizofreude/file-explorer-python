"""
Project Structure
1. Install tkinter and easygui
2. Import necessary libraries
3. Save file(s)
4. Open file(s)
5. Rename file(s)
6. Delete file(s)
7. Copy file(s)
8. Delete folder(s)
9. Create folder(s)
10. Move folder(s)
11. Initialize window and create buttons
"""

# 2. Import necessary libraries
import shutil
import os   # Process files & directory from different locations
from tkinter import filedialog   # Filedialog provides a set of dialogs
from tkinter import *   # Graphical User Interface package & event driven
import easygui   # Graphical User Interface module & not event driven
from tkinter import messagebox as mb

# 3. Save file(s)
def Save():
    def SaveAs():
        FileName = filedialog.asksaveasfile(initialdir="/", defaultextension=".txt", filetypes=[("text files", ".txt"), ("all files", ".*")])
        FileText = str(textspace.get(1.0, END))
        FileName.write(FileText)
    def Back():
        SaveWindow.destroy()
        os.startfile("file-explorer.py")
    Screen.destroy()   # Destroy a widget
    SaveWindow = Tk()   # Initialize tkinter module
    SaveWindow.title('Save As')
    SaveWindow.iconbitmap('SaveAs_python_icon_129853.ico')
    buttonSaveAs = Button(text="SaveAs", command=SaveAs)
    buttonSaveAs.pack()   # Organizes widgets in blocks & placed in the parent widget
    buttonBack = Button(text="Back", command=Back)
    buttonBack.pack()
    textspace = Text(SaveWindow)
    textspace.pack()

# 4. Open file(s)
def Open():
    Read = easygui.fileopenbox()   # Display the files where the path matches the default file path
    try:
        os.startfile(Read)   # Opens the file
    except:
        mb.showinfo("File not found!")   # Display the information as a pop up

# 5. Rename file(s)
def Rename():
    Read = easygui.fileopenbox()
    pathnew = os.path.dirname(Read)
    extension = os.path.splitext(Read)[1]   # This widget splits the path into extension and pair root
    print('Enter new name for the file')
    newName = input()
    path1 = os.path.join(pathnew, newName+extension)
    print(path1)
    os.rename(Read, path1)
    mb.showinfo("File renamed!")

# 6. Delete file(s)
def Delete():
    Read = easygui.fileopenbox()
    if os.path.exists(Read):   # Checks path existance
        os.remove(Read)   # Remove given object
    else:
        mb.showinfo("File not found!")

# 7. Copy file(s)
def Copy():
    Read = easygui.fileopenbox()
    destination1 = filedialog.askdirectory()
    shutil.copy(Read, destination1)   # Various operations related to file handling
    mb.showinfo("File copied.")

# 8. Delete folder(s)
def DeleteFolder():
    DelFolder = filedialog.askdirectory()   # Prompting the user to select a directory
    os.rmdir(DelFolder)   # Removal of an empty folder
    mb.showinfo("Folder deleted.")

# 9. Create folder(s)
def CreateFolder():
    Folder = filedialog.askdirectory()
    print("Enter folder name: ")
    NewFolder = input()
    path = os.path.join(Folder, NewFolder)
    os.mkdir(path)
    mb.showinfo(f"Folder {NewFolder} created")

# 10. Move folder(s)
def MoveFile():
    Read = easygui.fileopenbox()
    Destination = filedialog.askdirectory()
    if (Read == Destination):
        mb.showinfo('affirmative!', "Source and Destination are identical.")
    else:
        shutil.move(Read, Destination)   # move() relocate a folder to a designated directory
        mb.showinfo("File move success!")

# 11. Initialize mainloop window and create buttons
Screen = Tk()
Screen.title("Barebone File Explorer by Python 3.11")
Screen.geometry("400x400")
Screen.iconbitmap('folder_type_python_opened_icon_129852.ico')
Screen.resizable(0,0)
Screen.config(bg="grey")   # config() changes the property of the widget
SaveButton = Button(text="Save", command=Save)
SaveButton.place(relx=0.3, rely=0.2)
OpenButton = Button(text="Open", command=Open)
OpenButton.place(relx=0.5, rely=0.2)
RenameButton = Button(text="Rename", command=Rename)
RenameButton.place(relx=0.3, rely=0.4)
CopyButton = Button(text="Copy", command=Copy)
CopyButton.place(relx=0.5, rely=0.4)
DeleteButton = Button(text="Delete File", command=Delete)
DeleteButton.place(relx=0.3, rely=0.6)
DeleteFolderButton = Button(text="Delete Folder", command=DeleteFolder)
DeleteFolderButton.place(relx=0.5, rely=0.6)
CreateFolderButton = Button(text="Create Folder", command=Rename)
CreateFolderButton.place(relx=0.3, rely=0.8)
MoveFileButton = Button(text="Move File", command=MoveFile)
MoveFileButton.place(relx=0.5, rely=0.8)
mainloop()