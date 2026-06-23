class KalorienRechner:
    def berechne_kalorienbedarf(self, alter):
        if alter <= 0:
            raise ValueError("Das Alter muss größer als 0 sein.")

        if alter < 30:
            return 2500

        return 2200