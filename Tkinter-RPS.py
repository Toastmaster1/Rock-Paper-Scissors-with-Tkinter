import tkinter as tk
from random import randint
z = 0
compWin = 0
playerWin = 0
draw = 0

root = tk.Tk()
root.geometry("640x480")
root.config(bg='#333333')

def rps(choice):
    global compWin
    global playerWin
    global draw
    compChoice = randint(0, 2)
    winner = (3 + choice - compChoice) % 3
    # we love the rps equation ^^
    if winner == 0:
        output = "It was a draw."
        draw += 1
    elif winner == 1:
        output = "You won."
        playerWin += 1
    else:
        output = "Computer won."
        compWin += 1
    
    # overwriting the labels with appropriate replacements
    d.config(text=f"{output}")
    e.config(text=f"Draw: {draw} \n Computer Win: {compWin} \n Player Win: {playerWin}", bg="#333333")

# what happens goes below (still little to no idea how tkinter works)

a = tk.Button(root, text="Rock", font=("courier", 25), command=lambda:rps(0), bg="#48A57D", activebackground="#377B5D", fg="#FFFFFF")
a.pack()
b = tk.Button(root, text="Paper", font=("courier", 25), command=lambda:rps(1), bg="#48A57D", activebackground="#377B5D", fg="#FFFFFF")
b.pack()
c = tk.Button(root, text="Scissors", font=("courier", 25), command=lambda:rps(2), bg="#48A57D", activebackground="#377B5D", fg="#FFFFFF")
c.pack()
d = tk.Label(root, text=f"Awaiting choice.", bg="#333333", font=("courier", 25), fg="#FFFFFF")
d.pack()
e = tk.Label(root, text=f"Draw: {draw} \n Computer Win: {compWin} \n Player Win: {playerWin}", bg="#333333", font=("courier", 25), fg="#FFFFFF")
e.pack()
# do not put stuff after this line
root.mainloop()