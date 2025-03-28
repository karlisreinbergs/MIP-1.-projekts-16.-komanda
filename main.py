from gamestate2 import GameState
from gajiena_izpilde2 import gajiena_izpilde2
from best_move import best_move
from TreeNode import TreeNode
import random

# def uzvara():
#     global cilveka_rez, datora_rez
#     if (cilveka_rez > datora_rez):
#           print(f"Cilvece uzvar ar rezultatu {cilveka_rez}!")
#     elif (cilveka_rez == datora_rez):
#           print(f"cilveces intelekts ir vienads ar datoru, abi iegust {cilveka_rez} punktus")
#     else:
#           print(f"Dators uzvar ar {datora_rez} punktiem")
#
def virknes_izveide():
      garums = random.randint(15, 20)
      return [random.choice([1, 2, 3, 4]) for num in range(garums)]           #izveido random virnki

def spele():
      
      start_state = GameState(                                                      #izveido speles gajiena datu strukturu
            virkne = virknes_izveide(),    #uzlabots, lai virknes garumus būtu diapazonā no 15 līdz 20 skaitļiem
            cilveka_rez = 0,
            datora_rez = 0,
            ir_cilveka_gajiens = True,
            h_vertiba = 0
      )

      current_state = start_state

      root = TreeNode(start_state)
      #datora_algo = input("izvelies datora algoritmu: ")

      while (not current_state.tuksa_virkne()):
            print(current_state)

            if (current_state.ir_cilveka_gajiens):                                        #parbauda vai ir cilveka gajiens
                  index = int(input("ievadi indeksu: "))                                  #ievadi indeksu skaitlim kuru gribi izmantot
                  if (index == 9): exit()                                                 #vnk lai izbeigtu kodu
                  darbiba = int(input("izvelies 1, 2, vai 3: "))                          #izvelies kuru ricibu velies veikt ar skaitli, 1 ir pieskaitit sev, 2 ir sadalit vieniniekos, un 3 ir 4 sadalits divniekos
                  current_state = gajiena_izpilde2(current_state, index, darbiba)         #palaiz gajienu funkciju cilvekam
                  root = TreeNode(current_state)
            else:
                  print("Datora gājiens")  
                  root = TreeNode(current_state)
                  best_node = best_move(root, 3)  # Izvēlas labāko gājienu no koka
                  if best_node:
                        current_state = best_node.state
                  else:
                        break
      print("\n=== SPĒLE BEIGUSIES ===")
      print(f"Cilvēks: {current_state.cilveka_rez}")
      print(f"Dators: {current_state.datora_rez}")
      if current_state.cilveka_rez > current_state.datora_rez:
            print("Cilvēks uzvar!")
      elif current_state.datora_rez > current_state.cilveka_rez:
            print("Dators uzvar!")
      else:
            print("Neizšķirts!")

if __name__ == "__main__":
    spele()