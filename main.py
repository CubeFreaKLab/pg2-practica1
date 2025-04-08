from calculadora_poo import Calculadora
from factorial_poo import CalculadoraFactorial

print("Calculadora Estandar")
calculadora_1 = Calculadora()

print(calculadora_1.sumar(2, 5))
print(calculadora_1.restar(10, 9))
print(calculadora_1.multiplicar(5, 9))
print(calculadora_1.dividir(150, 6))

print("Calculadora Factorial")
calculadora_factorial = CalculadoraFactorial(numero=5)
print(calculadora_factorial.calcular())
