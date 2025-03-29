from gamestate2 import GameState
from gajiena_izpilde2 import gajiena_izpilde2
from best_move import best_move
from TreeNode import TreeNode
import random
from tkinter import *

# def uzvara():
#     global cilveka_rez, datora_rez
#     if (cilveka_rez > datora_rez):
#           print(f"Cilvece uzvar ar rezultatu {cilveka_rez}!")
#     elif (cilveka_rez == datora_rez):
#           print(f"cilveces intelekts ir vienads ar datoru, abi iegust {cilveka_rez} punktus")
#     else:
#           print(f"Dators uzvar ar {datora_rez} punktiem")
#
def virknes_izveide(garums: int):
      #izveido random virnki
      return [random.choice([1, 2, 3, 4]) for num in range(garums)]

def spele(isHumanChoise: bool, virknes_garums: int):

      main_window = Tk()
      main_window.title("Game")
      main_window.geometry("700x200")

      start_state = GameState(
            virkne = virknes_izveide(virknes_garums),
            cilveka_rez = 0,
            datora_rez = 0,
            ir_cilveka_gajiens = isHumanChoise,
            h_vertiba = 0
      )

      global current_state, root
      current_state = start_state
      root = TreeNode(start_state)

      # TODO: Create separate window in def initApp() to choose algorithm
      #datora_algo = input("izvelies datora algoritmu: ")

      infoLabel = Label(main_window, text=current_state)
      infoLabel.pack()

      Label(main_window, text="ievadi indeksu:", justify="left").pack()
      indexEntry = Entry(main_window, justify="left")
      indexEntry.pack()

      Label(
            main_window, text="izvelies 1(pieskaitīt savam punktu skaitam), 2 (sadalīt divos skaitļos «1» un «1»  un pieskaitīt vienu punktu pretiniekam), vai 3(sadalīt divos skaitļos “2” un “2” un atņemt no pretinieka punktu skaita 1 punktu)", 
            wraplength=400,
            justify="left",
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
            
      Button(main_window, text="Make a move", command=lambda: take_action(current_state)).pack()

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
            result_window.title("Result")
            result_window.geometry("200x200")

            Label(result_window, text=winner_text).pack()
            result_window.mainloop()

      def computer_move():
            global current_state, root

            if not current_state.ir_cilveka_gajiens:
                  root = TreeNode(current_state)
                  best_node = best_move(root, 3)
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
            number_window.title("Enter a Number")
            number_window.geometry("300x150")
            
            Label(number_window, text="Enter a number (15-20):").pack()
            entry = Entry(number_window)
            entry.pack()
            
            def validate_number():
                  garums = int(entry.get())
                  if 15 <= garums <= 20:
                        number_window.destroy()
                        open_pirmais_gajiens_window(garums)
            
            Button(number_window, text="Submit", command=validate_number).pack()
            number_window.mainloop()

      def open_pirmais_gajiens_window(virknes_garums: int):
            choice_window = Tk()
            choice_window.title("Choose an Option")
            choice_window.geometry("300x150")
            
            Label(choice_window, text="Select one:").pack(pady=5)
            choice = StringVar(value="Dators")
            
            Radiobutton(choice_window, text="Dators", variable=choice, value="Desktop").pack()
            Radiobutton(choice_window, text="Cilvēks", variable=choice, value="User").pack()

            
            def submit_choice():
                  choice_window.destroy()
                  spele(choice.get() == "User", virknes_garums)
            
            Button(choice_window, text="Confirm", command=submit_choice).pack(pady=10)
            choice_window.mainloop()

      welcome_window = Tk()
      welcome_window.title("Spele")
      welcome_window.geometry("200x100")

      Label(welcome_window, text="Welcome to the game").pack()
      Button(welcome_window, text="Sakt", command=open_number_input).pack()

      welcome_window.mainloop()

if __name__ == "__main__":
      initApp()