import tkinter as tk

window = tk.Tk()
window.title('window')
window.geometry('800x600')

var = tk.StringVar()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")

I = tk.Label(window,
        textvariable=var,
        text="Input:",
        bg="green",
        font=("Consolas", 12),
        width=15,
        height=2
        )
I.place(x=40, y=80)
# I.geometry("200x200")

b = tk.Button(window,
        text="hit me",
        width=15,
        height=2,
        command=hit_me
        )
b.place(x=380, y=500)



window.mainloop()
