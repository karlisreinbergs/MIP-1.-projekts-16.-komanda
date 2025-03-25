def gajiena_izpilde2(current_state, index, darbiba):     #seit padod cilveka izveletas darbibas lai veiktu gajienus
    num = current_state.virkne[index]

    if (darbiba == 1):
        return current_state.pieskaita_sev(index)
    elif (darbiba == 2 and current_state.virkne[index] == 2):
        return current_state.sadala_2(index)
    elif (darbiba == 3 and current_state.virkne[index] == 4):
        return current_state.sadala_4(index)