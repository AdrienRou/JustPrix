import tkinter as tk
from random import randint


def get():
    global tries

    if tries == 5:
        countdown(60)

    number_string = guess.get()

    if number_string.isdigit():
        number = int(number_string)
        if 0 <= number <= 100:
            print("Vous avez rentré le nombre: " + str(number))
            if tries > 1:
                if number < random_number:
                    hint.set("C'est plus!")
                    print("c'est plus\n")
                    print("TENTATIVES :" + str(tries - 1))
                    print("Choisissez un nombre entre 1 et 100")
                elif number > random_number:
                    hint.set("C'est moins!")
                    print("c'est moins\n")
                    print("TENTATIVES :" + str(tries - 1))
                    print("Choisissez un nombre entre 1 et 100")
                else:
                    hint.set("C'est gagné")
                    button1["state"] = "disabled"
                    print("c'est ça")
            else:
                if number != random_number:
                    hint.set("C'est perdu")
                    print("c'est perdu")
                else:
                    hint.set("C'est gagné")
                button1["state"] = "disabled"
            tries -= 1
            value = str(tries)
            nb.set(value)
        else:
            print("rentré un nombre valide svp")
    else:
        print("rentré un nombre valide svp")


def setup():
    global random_number
    random_number = randint(1, 100)
    guess.set(0)
    nb.set("5")
    print(random_number)
    print(
        "Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et "
        "100\n")
    print("TENTATIVES :" + str(tries))
    print("Choisissez un nombre entre 1 et 100")


def countdown(count):
    label["text"] = count

    if count > 0:
        root.after(1000, countdown, count - 1)
    if count == 0 and tries > 0:
        hint.set("Trop tard")
        button1["state"] = "disabled"


root = tk.Tk()
root.title("Le juste prix")
root.config(bg="#72a37c")
root.geometry("640x480")
root.maxsize(640, 480)
root.minsize(300, 400)
hint = tk.StringVar()
guess = tk.StringVar()
nb = tk.StringVar()
label = tk.Label(root)
label.place(x=0, y=0)

random_number = 0
tries = 5
g = tk.Entry(textvariable=guess)
g.grid(column=4, row=0, padx=20, pady=0)
button1 = tk.Button(root, text="Deviner", command=get)
button1.grid(column=5, row=0, padx=1, pady=0)
root.update()
h = tk.Label(root, textvariable=hint)
h.grid(column=4, row=2, padx=0, pady=5)
n = tk.Label(root, textvariable=nb)
n.grid(column=6, row=0, padx=200, pady=0)
setup()
root.mainloop()
