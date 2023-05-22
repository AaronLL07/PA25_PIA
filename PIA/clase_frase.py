# clase de las frases
class Frase:
    
    def __init__(self, id_frase, frase, autor, stars_calif = []):
        self.id_frase = id_frase
        self.frase = frase
        self.autor = autor
        self.stars_calif = stars_calif
    
    def mostrar_frase(self):
        print(21*"*")
        print(f"ID de la frase: {self.id_frase}\nFrase: {self.frase}\nAutor: {self.autor}\nPorcentaje de estrellas: {self.stars_calif[-5:]}")

    def info_frase(self):
        print(21*"*")
        print(f"Frase: {self.frase}\nAutor: {self.autor}")