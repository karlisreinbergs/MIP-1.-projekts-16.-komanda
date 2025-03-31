from gamestate2 import GameState
from gajiena_izpilde2 import gajiena_izpilde2
from best_move import best_move
from TreeNode import TreeNode
import random
from tkinter import *

def virknes_izveide(garums: int):
    # izveido random virkni
    return [random.choice([1, 2, 3, 4]) for num in range(garums)]

def spele(isHumanChoise: bool, virknes_garums: int, algorithm: str):
    main_window = Tk()
    main_window.title("Spēle")
    main_window.geometry("500x500")

    start_state = GameState(
        virkne=virknes_izveide(virknes_garums),
        cilveka_rez=0,
        datora_rez=0,
        ir_cilveka_gajiens=isHumanChoise,
        h_vertiba=0
    )

    global current_state, root
    current_state = start_state
    root = TreeNode(start_state)

    infoLabel = Label(main_window, text=current_state)
    infoLabel.pack()

    Label(main_window, text="Ievadi indeksu:", justify="left").pack()
    indexEntry = Entry(main_window, justify="left")
    indexEntry.pack()

    Label(
        main_window,
        text="izvēlies 1(pieskaitīt savam punktu skaitam), 2 (sadalīt divos skaitļos '1' un '1'  un pieskaitīt vienu punktu pretiniekam), vai 3(sadalīt divos skaitļos '2' un '2' un atņemt no pretinieka punktu skaita 1 punktu)", 
        wraplength=400,
        justify="left"
    ).pack()
    actionEntry = Entry(main_window, justify="left")
    actionEntry.pack()

    def take_action(state: GameState):
        global current_state, root

        index = int(indexEntry.get())
        action = int(actionEntry.get())

        validIndex = index >= 0 and index < len(state.virkne)

        if validIndex and [1, 2, 3].__contains__(action) and state.ir_cilveka_gajiens:
            # palaiz gajienu funkciju cilvekam
            current_state = gajiena_izpilde2(state, index, action)
            root = TreeNode(current_state)
            infoLabel.config(text=str(current_state))
            main_window.after(500, computer_move)

        if current_state.tuksa_virkne():
            show_winner()
        
    Button(main_window, text="Veikt gājienu", command=lambda: take_action(current_state)).pack()

    def show_winner():
        winner_text = "=== SPĒLE BEIGUSIES ===\n"
        winner_text += f"Cilvēks: {current_state.cilveka_rez}\n"
        winner_text += f"Dators: {current_state.datora_rez}\n"

        if current_state.cilveka_rez > current_state.datora_rez:
            winner_text += "Cilvēks uzvar!"
        elif current_state.datora_rez > current_state.cilveka_rez:
            winner_text += "Dators uzvar!"
        else:
            winner_text += "Neizšķirts!"

        main_window.destroy()

        result_window = Tk()
        result_window.title("Rezultāts")
        result_window.geometry("500x500")

        Label(result_window, text=winner_text).pack()
        result_window.mainloop()

    def computer_move():
        global current_state, root

        if not current_state.ir_cilveka_gajiens:
            root = TreeNode(current_state)
            if algorithm == "minimax":
                best_node = best_move(root, 3, float('-inf'), float('inf'), algorithm)
            else:  # alphabeta
                best_node = best_move(root, 3, float('-inf'), float('inf'), algorithm)
            if best_node:
                current_state = best_node.state
                infoLabel.config(text=str(current_state))
            else:
                show_winner()

    main_window.after(500, computer_move)
    main_window.mainloop()

def initApp():
    def open_number_input():
        welcome_window.destroy()
        number_window = Tk()
        number_window.title("Ievadi skaitli")
        number_window.geometry("500x500")
        
        Label(number_window, text="Ievadi skaitli no 15 līdz 20:").pack()
        entry = Entry(number_window)
        entry.pack()
        
        def validate_number():
            try:
                garums = int(entry.get())
                if 15 <= garums <= 20:
                    number_window.destroy()
                    open_algorithm_window(garums)
                else:
                    Label(number_window, text="Lūdzu ievadi skaitli no 15 līdz 20!", fg="red").pack()
            except ValueError:
                Label(number_window, text="Lūdzu ievadi derīgu skaitli!", fg="red").pack()
        
        Button(number_window, text="Ievadīt", command=validate_number).pack()
        number_window.mainloop()

    def open_algorithm_window(virknes_garums: int):
        algo_window = Tk()
        algo_window.title("Izvēlēties algoritmu")
        algo_window.geometry("500x500")
        
        Label(algo_window, text="Izvēlies algoritmu:").pack(pady=5)
        algorithm = StringVar(value="minimax")
        
        Radiobutton(algo_window, text="Minimax", variable=algorithm, value="minimax").pack(anchor=W)
        Radiobutton(algo_window, text="Alpha-Beta", variable=algorithm, value="alphabeta").pack(anchor=W)
        
        def submit_algorithm():
            algo_window.destroy()
            open_pirmais_gajiens_window(virknes_garums, algorithm.get())
        
        Button(algo_window, text="Apstiprināt", command=submit_algorithm).pack(pady=10)
        algo_window.mainloop()

    def open_pirmais_gajiens_window(virknes_garums: int, algorithm: str):
        choice_window = Tk()
        choice_window.title("Kurš sāks pirmais?")
        choice_window.geometry("500x500")
        
        Label(choice_window, text="Izvēlies, kam pirmais gājiens:").pack(pady=5)
        choice = StringVar(value="Dators")
        
        Radiobutton(choice_window, text="Datoram", variable=choice, value="Desktop").pack(anchor=W)
        Radiobutton(choice_window, text="Cilvēkam", variable=choice, value="User").pack(anchor=W)
        
        def submit_choice():
            choice_window.destroy()
            spele(choice.get() == "User", virknes_garums, algorithm)
        
        Button(choice_window, text="Apstiprināt", command=submit_choice).pack(pady=10)
        choice_window.mainloop()

    welcome_window = Tk()
    welcome_window.title("Spēle")
    welcome_window.geometry("500x500")
    kakis = PhotoImage(file="cat.png")
    image_label = Label(welcome_window, image=kakis)
    image_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    Label(welcome_window, text="Laipni lūgti spēlē!").place(relx=0.5, rely=0.6, anchor=CENTER)
    Button(welcome_window, text="Sākt", command=open_number_input).place(relx=0.5, rely=0.8, anchor=CENTER)

    welcome_window.mainloop()

if __name__ == "__main__":
    initApp()