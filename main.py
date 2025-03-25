from gamestate2 import GameState
from gajiena_izpilde2 import gajiena_izpilde2
import random

# def uzvara():
#     global cilveka_rez, datora_rez
#     if (cilveka_rez > datora_rez):
#           print(f"Cilvece uzvar ar rezultatu {cilveka_rez}!")
#     elif (cilveka_rez == datora_rez):
#           print(f"cilveces intelekts ir vienads ar datoru, abi iegust {cilveka_rez} punktus")
#     else:
#           print(f"Dators uzvar ar {datora_rez} punktiem")
*
def virknes_izveide(garums):
      return [random.choice([1, 2, 3, 4]) for num in range(garums)]


start_state = GameState(
      virkne = virknes_izveide(15),
      cilveka_rez = 0,
      datora_rez = 0,
      ir_cilveka_gajiens = True,
      h_vertiba = 0
)

current_state = start_state

datora_algo = input("izvelies datora algoritmu: ")

while (not current_state.tuksa_virkne()):
      print(current_state)

      if (current_state.ir_cilveka_gajiens):
            index = int(input("ievadi indeksu: "))
            if (index == 9): exit()
            darbiba = int(input("izvelies 1, 2, vai 3: "))
            current_state = gajiena_izpilde2(current_state, index, darbiba)
      else:
            current_state.generate_children()
            current_state = current_state.children[0] 

