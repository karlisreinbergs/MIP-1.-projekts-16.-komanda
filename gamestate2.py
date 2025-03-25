class GameState:
    def __init__(self, virkne, cilveka_rez, datora_rez, ir_cilveka_gajiens, h_vertiba):
        self.virkne = virkne
        self.cilveka_rez = cilveka_rez
        self.datora_rez = datora_rez
        self.ir_cilveka_gajiens = ir_cilveka_gajiens
        self.h_vertiba = h_vertiba                  #heiristiska vertiba gajienam
        self.children = []                          #seit glabajas gajieni iespejamiem

    def tuksa_virkne(self):
        return len(self.virkne) == 0                #parbauda vai virkne ir tuksa

    def generate_children(self):
        self.children = []                          #iztukso listu pirms liek taja nakamos gajienus
        for i, num in enumerate(self.virkne):           #katram ciparam virknei izveido gajiena variantus
            self.children.append(self.pieskaita_sev(i)) #izsauc funkcijas, kas genere variantus
        
            if (num == 2):
                self.children.append(self.sadala_2(i))
            
            if (num == 4):
                self.children.append(self.sadala_4(i))

    def pieskaita_sev(self, i):
        jauna_virkne = self.virkne[:]               #nokope virkni
        punkti = jauna_virkne.pop(i)

        jauns_gajiens = GameState(                  #izveido gajienu
            virkne = jauna_virkne,
            cilveka_rez = self.cilveka_rez,
            datora_rez = self.datora_rez,
            ir_cilveka_gajiens = not self.ir_cilveka_gajiens,      #nomaina gajienu uz pretejeo
            h_vertiba = punkti                      #pagaidam heiristisko vertibu pieskir ka skaitla vertibu
        )

        if (self.ir_cilveka_gajiens):               #atskiriba no ta kuram gajiens pieskaita punktus
            jauns_gajiens.cilveka_rez += punkti
        else:
            jauns_gajiens.datora_rez += punkti
        
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
        return f"Virkne: {self.virkne} | Cilvēks: {self.cilveka_rez} | Dators: {self.datora_rez} | Tagad spēlē: {speletajs} | heiristiskais vertejums: {self.h_vertiba}"
    