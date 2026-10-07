#import tkinter as tk

#root = tk.Tk()
#root is the window 

#below are the widgets
#label = tk.Label(root, text="Bob is here say hi (*/ω＼*)")
#label.pack()
# tk.Label creates the label
# root in line 6 is putting the label in its window
#button=tk.Button(root, text="say hi", width=25, height=5, command=label.destroy)
#button.pack()
#button=tk.Button(root, text="ignore it", width=25, height=5, command=root.destroy)
#button.pack()
# tk.Button creates the button
# root in line 11 and 13 is putting the button in its window
# the width and height controls the size of the widget
# "command = root.destroy" in line 13 is when the widget is clicked it will instantly close the window
# "command = label.destroy" in line 11 is when the widget is clicked it will instantly delete the label

# 7 okt
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="favorite food").grid(row=0, column=0)
tk.Label(root, text="favorite color").grid(row=1, column=0)

entry1 = tk.Entry (root)
entry2 = tk.Entry (root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(root, text="Male", variable=var1).grid(row=0, sticky=tk.W)
tk.Checkbutton(root, text="Female", variable=var2).grid(row=1, sticky=tk.W)

v= tk.IntVar()#it is not working

tk.Radiobutton(root, text="A", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="B", variable=v, value=2).pack(anchor=tk.W)
root.mainloop()


