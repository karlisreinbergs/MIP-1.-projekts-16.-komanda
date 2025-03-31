class GameState:
    def __init__(self, virkne, cilveka_rez, datora_rez, ir_cilveka_gajiens, h_vertiba):
        self.virkne = virkne
        self.cilveka_rez = cilveka_rez
        self.datora_rez = datora_rez
        self.ir_cilveka_gajiens = ir_cilveka_gajiens
        self.h_vertiba = datora_rez - cilveka_rez                  #heiristiska vertiba gajienam
        self.children = []                          #seit glabajas gajieni iespejamiem
    
    def tuksa_virkne(self):
        return len(self.virkne) == 0                #parbauda vai virkne ir tuksa
    
    def generate_children(self):
        self.children = []                          #iztukso listu pirms liek taja nakamos gajienus
        for i, num in enumerate(self.virkne):           #katram ciparam virknei izveido gajiena variantus
            child1 = self.pieskaita_sev(i)
            self.children.append(child1)
            if num == 2:
                child2 = self.sadala_2(i)
                self.children.append(child2)
            if num == 4:
                child3 = self.sadala_4(i)
                self.children.append(child3)
    
    def pieskaita_sev(self, i):
        jauna_virkne = self.virkne[:]
        punkti = jauna_virkne.pop(i)
        
        jauns_gajiens = GameState(
            virkne=jauna_virkne,
            cilveka_rez=self.cilveka_rez,
            datora_rez=self.datora_rez,
            ir_cilveka_gajiens=not self.ir_cilveka_gajiens,
            h_vertiba=0  # Tiks pārrēķināts automātiski
        )

        if self.ir_cilveka_gajiens:
            jauns_gajiens.cilveka_rez += punkti
        else:
            jauns_gajiens.datora_rez += punkti

        jauns_gajiens.h_vertiba = jauns_gajiens.datora_rez - jauns_gajiens.cilveka_rez
        return jauns_gajiens
    
    def sadala_2(self, i):
        jauna_virkne = self.virkne[:]
        jauna_virkne.pop(i)
        jauna_virkne[i:i] = [1, 1]                  #aizvieto ar diviem 1niekiem

        jauns_gajiens = GameState(
            virkne = jauna_virkne,
            cilveka_rez = self.cilveka_rez,
            datora_rez = self.datora_rez,
            ir_cilveka_gajiens = not self.ir_cilveka_gajiens,
            h_vertiba = -1
        )

        if (self.ir_cilveka_gajiens):
            jauns_gajiens.datora_rez += 1
        else:
            jauns_gajiens.cilveka_rez += 1
        
        return jauns_gajiens

    def sadala_4(self, i):
        jauna_virkne = self.virkne[:]
        jauna_virkne.pop(i)
        jauna_virkne[i:i] = [2, 2]

        jauns_gajiens = GameState(
            virkne = jauna_virkne,
            cilveka_rez = self.cilveka_rez,
            datora_rez = self.datora_rez,
            ir_cilveka_gajiens = not self.ir_cilveka_gajiens,
            h_vertiba = 1
        )

        if (self.ir_cilveka_gajiens):
            jauns_gajiens.datora_rez -= 1
        else:
            jauns_gajiens.cilveka_rez -= 1
        
        return jauns_gajiens
    
    
    def __str__(self):
        speletajs = "Cilvēks" if self.ir_cilveka_gajiens else "Dators"
        return f"Virkne: {self.virkne} | Cilvēks: {self.cilveka_rez} | Dators: {self.datora_rez} | Tagad spēlē: {speletajs} | Heiristiskais vērtējums: {self.h_vertiba}"
    