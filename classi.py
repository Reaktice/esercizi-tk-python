class Persona:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni
    def stampanome(self):
        print("Ciao, il mio nome è " + self.nome)

p1 = Persona("Marco", 25)
p1.stampanome()


class Persona:
    specie = "Homo sapiens"  # Attributo di classe
    
    def __init__(self, nome, eta):
        self.nome = nome  # Attributo di istanza
        self.eta = eta

persona1 = Persona("Mario", 30)
print(persona1.specie)  # Output: Homo sapiens
print(persona1.nome)    # Output: Mario