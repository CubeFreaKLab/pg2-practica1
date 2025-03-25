import math

# Clase base que representa una calculadora simple (Abstraccion)
class Calculadora:
    def __init__(self, a, b):
        self.__resultado = 0
        self.a = a
        self.b = b
        self.operacion = ""

    def sumar(self):
            self.operacion = "Suma"
            self.__resultado = self.a + self.b
            return self._mostrar_operacion()
        
    def restar(self):
            self.operacion = "Resta"
            self.__resultado = self.a - self.b
            return self._mostrar_operacion()
        
    def multiplicar(self):
            self.operacion = "Multiplicar"
            self.__resultado = self.a * self.b
            return self._mostrar_operacion()
        
    def dividir(self):
        self.operacion = "División"
        if self.b != 0:
            self.__resultado = self.a / self.b
        else:
            return "Error: División entre cero"
        return self._mostrar_operacion()
        
    def _mostrar_operacion(self):
            return f"{self.operacion}: {self.a} y {self.b} = {self.__resultado}"

    def calcular_todo(self):
        resultados = []
        resultados.append(self.sumar())
        resultados.append(self.restar())
        resultados.append(self.multiplicar())
        resultados.append(self.dividir())
        return "\n".join(resultados)

calculadora_1 = Calculadora(20, 5)
print(calculadora_1.calcular_todo())
