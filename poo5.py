#Polimorfismo

class Arma:

    def __init__(self, balas, peso):
        self.balas = balas
        self.peso = peso


    def disparar(self):
        print("EL arma dispara")


class Pistola(Arma):

    def disparar(self):
        return print("El arma dispara lento")


class Ametralladora(Arma):

    def disparar(self):
        print("El arma dispara rapido")

arma = Arma(15,7)
arma.disparar()
pistola = Pistola(12,5)
pistola.disparar()
ametralladora = Ametralladora(50,12)
ametralladora.disparar()
