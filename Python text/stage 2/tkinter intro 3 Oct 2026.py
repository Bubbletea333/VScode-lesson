import tkinter as tk

root = tk.Tk()
#root is the window 

#below are the widgets
label = tk.Label(root, text="Bob is here say hi (*/ω＼*)")
label.pack()
# tk.Label creates the label
# root in line 6 is putting the label in its window
button=tk.Button(root, text="say hi", width=25, height=5, command=label.destroy)
button.pack()
button=tk.Button(root, text="ignore it", width=25, height=5, command=root.destroy)
button.pack()
# tk.Button creates the button
# root in line 11 and 13 is putting the button in its window
# the width and height controls the size of the widget
# "command = root.destroy" in line 13 is when the widget is clicked it will instantly close the window
# "command = label.destroy" in line 11 is when the widget is clicked it will instantly delete the label
root.mainloop()


