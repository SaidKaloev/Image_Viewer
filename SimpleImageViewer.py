import glob
import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk

# Here we define a counter, the filetypes we look for and the folder name of the images
#######################################################################
count = 0  # DO NOT CHANGE
file_endings = ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG")
abs_path = os.path.abspath("CityPics")  # Folder with images should be in same directory as this file
#######################################################################
root = Tk()
root.title("SimpleImageViewer")


def black():
    """
    This and the following 3 functions return the background color of the ImageViewer.
    :return: Configure/Update Background Color
    """
    root.configure(bg="black")


def blue():
    root.configure(bg="blue")


def gray():
    root.configure(bg="gray")


def white():
    root.configure(bg="white")


def read_and_show(n: int):
    """
    This function receives an index, opens the image with PIL and transforms it into a tkinter image.

    :param n: The index of the current image. (Also defined as count.)
    :return: An image as a tkinter object.
    """

    global tok_list

    read = Image.open(tok_list[n])
    img = ImageTk.PhotoImage(read.resize((700, 700), Image.ANTIALIAS))
    return img


def forward():
    """
    This function represents the "Next"-Button, with which we are able to move to the next image.
    It deletes current image from the label and defines the new label to be the next image.
    If the image is the last picture in the list, the next_button will be disabled.

    :return: Updates the existing buttons and label to point to the next image.
    """

    global btn_next
    global btn_prev
    global btn_exit
    global tok_list
    global count
    global image
    global lbl

    # Remove current image, so we can show next image
    lbl.grid_forget()
    # If the counter is equal to index of last image we disable the next button
    if count == len(tok_list)-1:
        btn_next = Button(root, text='NEXT>>', width=30, bg='white', state=DISABLED, command=forward)
        btn_prev = Button(root, text='<<BACK', width=30, bg='green', command=previous)
        btn_exit = Button(root, text="EXIT", width=30, bg="orange", command=root.quit)

    else:
        count += 1
        # Define the buttons again
        btn_next = Button(root, text='NEXT>>', width=30, bg='green', command=forward)
        btn_prev = Button(root, text='<<BACK', width=30, bg='green', command=previous)
        btn_exit = Button(root, text="EXIT", width=30, bg="orange", command=root.quit)
        # Show the image with updated counter
        image = read_and_show(count)
        lbl = Label(root, image=image)

    # Update status_bar
    status_bar = Label(root, text=f"Image {count+1} of {len(tok_list)}", bd=1, relief=SUNKEN, anchor=E)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)
    #  And last but not least, define in which grid the buttons should be shown
    lbl.grid(column=0, row=0, columnspan=3)
    btn_next.grid(column=2, row=1)
    btn_exit.grid(column=1, row=1)
    btn_prev.grid(column=0, row=1)


def previous():
    """
    This function represents the "Back"-Button, with which we are able to move to the previous image.
    It deletes current image from the label and defines the new label to be the previous image.
    If the image is the first picture in the list, the back_button will be disabled.

    :return: Updates the existing buttons and label to point to the next image.
    """
    global btn_next
    global btn_prev
    global btn_exit
    global tok_list
    global count
    global image
    global lbl
    global status_bar

    # Remove current image, so we can show prev image
    lbl.grid_forget()
    # Check if the counter is equal to zero
    if count == 0:
        # If the counter is equal to 0 we disable the previous button
        btn_next = Button(root, text='NEXT>>', width=30, bg='green', command=forward)
        btn_prev = Button(root, text='<<BACK', width=30, bg='white', state=DISABLED, command=previous)
        btn_exit = Button(root, text="EXIT", width=30, bg="orange", command=root.quit)
    else:
        count -= 1
        # Define the buttons again
        btn_next = Button(root, text='NEXT>>', width=30, bg='green', command=forward)
        btn_prev = Button(root, text='<<BACK', width=30, bg='green', command=previous)
        btn_exit = Button(root, text="EXIT", width=30, bg="orange", command=root.quit)
        # Show the image with updated counter
        image = read_and_show(count)
        lbl = Label(root, image=image)

    # Update status_bar
    status_bar = Label(root, text=f"Image {count+1} of {len(tok_list)}", bd=1, relief=SUNKEN, anchor=E)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)
    # And last but not least, define in which grid the buttons should be shown
    lbl.grid(column=0, row=0, columnspan=3)
    btn_next.grid(column=2, row=1)
    btn_exit.grid(column=1, row=1)
    btn_prev.grid(column=0, row=1)


#  Configure and define the background-color buttons
root.configure(bg="black") # Default background is black
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="black", command=black)
filemenu.add_command(label="blue", command=blue)
filemenu.add_command(label="gray", command=gray)
filemenu.add_command(label="white", command=white)
menubar.add_cascade(label="Background", menu=filemenu)
root.config(menu=menubar)
# Configure rows and columns of buttons when changing size of the GUI-window
root.rowconfigure(0, weight=1)
for i in range(3):
    root.columnconfigure(i, weight=1)
# Define the buttons next, back and exit
btn_next = Button(root, text='NEXT>>', width=30, bg='green', command=forward)
btn_next.grid(column=2, row=1)
btn_prev = Button(root, text='<<BACK', width=30, bg='green', command=previous)
btn_prev.grid(column=0, row=1)
btn_exit = Button(root, text="EXIT", width=30, bg="orange", command=root.quit)
btn_exit.grid(column=1, row=1)
# Get the absolute path of the directory in which the images are stored, then get list of images
tok_list = []
for files in file_endings:
    tok_list.extend(glob.glob(os.path.join(abs_path, files)))
# Implement a statusbar to know at which image we currently are
status_bar = Label(root, text=f"Image {count+1} of {len(tok_list)}", bd=1, relief=SUNKEN, anchor=E, bg="white")
status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)
# Show current picture
image = read_and_show(count)
lbl = Label(root, image=image)
lbl.grid(column=0, row=0, columnspan=3)

root.mainloop()
