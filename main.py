import time
import HumanDetection as svm
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk


numberPeopleDetected = -1
photoFileName = ""

def submission_click():
    global photoFileName
    photoFileName = entry.get()
    if not photoFileName:
        return

    try:
        with Image.open(photoFileName) as img:
            print("Image opened successfully")
    except IOError:
        print(f"Failed to open the image file: {photoFileName}")
        return

    progress = ttk.Progressbar(startWindow, orient='horizontal', length=200, mode='determinate')
    progress.pack(pady=20)
    for i in range(1, 101):
        progress['value'] = i
        startWindow.update_idletasks()
        time.sleep(0.1)
    startWindow.destroy()

# Initialize the main window
startWindow = tk.Tk()
startWindow.title("Human Detection Algorithm")
startWindow.geometry("800x600")  # Window size
startWindow.configure(bg='black')  # Background color

textDescFrame = tk.Frame(bg='black')

# Create a label
firstLine = tk.Label(master=textDescFrame, text="Enter a file name", font=("Arial", 24), bg='black', fg='white')
firstLine.pack(pady=3)

secondLine = tk.Label(master=textDescFrame, text="for an image", font=("Arial", 24), bg='black', fg='white')
secondLine.pack(pady=3)

thirdLine = tk.Label(master=textDescFrame, text="to be analyzed:", font=("Arial", 24), bg='black', fg='white')
thirdLine.pack(pady=3)

textDescFrame.pack()


entryFrame = tk.Frame(bg = 'black')

# Create an entry box
entry = ttk.Entry(master=entryFrame, font=("Arial", 20))
entry.pack(side= tk.LEFT, padx=15)

# Create a button
button = ttk.Button(master=entryFrame, text="Submit", command=submission_click)
button.pack(side=tk.RIGHT)

entryFrame.pack()
# Start the Tkinter event loop
startWindow.mainloop()

def resize_image(image, max_size=(500, 500)):
    original_size = image.size
    ratio = min(max_size[0] / original_size[0], max_size[1] / original_size[1])
    new_size = (int(original_size[0] * ratio), int(original_size[1] * ratio))
    return image.resize(new_size, Image.Resampling.LANCZOS)

outputWindow = tk.Tk()
outputWindow.title("Human Detection Algorithm Output")
outputWindow.geometry("800x600")  # Window size
outputWindow.configure(bg='black')  # Background color

analyzedText = tk.Label(outputWindow, text="Analyzed Image:", font=("Arial", 44), bg='black', fg='white')
analyzedText.pack(pady=8)

# Load the image and resize it
image = Image.open(photoFileName)

numPeople = svm.image_detection(photoFileName,'output.jpg')

image1 = Image.open('output.jpg')

resized_image = resize_image(image1)
img = ImageTk.PhotoImage(resized_image)

# Create a frame that adjusts to the image size
imageFrame = tk.Frame(outputWindow, width=img.width(), height=img.height(), bg='black')
imageFrame.pack()
imageFrame.place(anchor='center', relx=0.5, rely=0.5)

# Create a Label Widget to display the image
photoLabel = tk.Label(imageFrame, image=img)
photoLabel.pack()

outputText = tk.Label(imageFrame, text="Number of people: " + str(numPeople), font=("Arial", 18), bg='black', fg='white')
outputText.pack(pady=3)

outputWindow.mainloop()
