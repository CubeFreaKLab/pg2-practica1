# PG2: PRÁCTICA 1

## Descripción General de la Práctica

Esta práctica implementa una calculadora utilizando Programación Orientada a Objetos (POO) en Python. El objetivo es demostrar los principios fundamentales: abstracción, encapsulamiento, herencia y polimorfismo.

Se ha desarrollado una calculadora estándar que realiza operaciones básicas (suma, resta, multiplicación y división), y una calculadora factorial que hereda de la primera, añadiendo la capacidad de calcular el factorial de un número.

## Configuración del Entorno y Ejecución

Para configurar y ejecutar este proyecto:

1. Clone el repositorio:

   ```bash
   git clone https://github.com/CubeFreaKLab/pg2-practica1.git
   cd pg2-practica1
   ```

2. Cree un entorno virtual

   - En Windows:

   ```
   python -m venv env
   env\Scripts\activate
   ```

   - En Linux:

   ```
   python3 -m venv env
   source env/bin/activate
   ```

   Para desactivar el entorno virtual cuando termine:

   ```
   deactivate
   ```

3. Ejecute el archivo principal:
   ```
   python main.py
   ```

## Calculadora Estándar

### Descripción y Forma de Uso

La clase `Calculadora` implementa las operaciones aritméticas básicas: suma, resta, multiplicación y división. Cada método devuelve directamente el resultado formateado.

Ejemplo de uso (como se ve en main.py):

```python
from calculadora_poo import Calculadora

# Crear una instancia de la calculadora
calculadora_1 = Calculadora()

# Realizar operaciones y mostrar resultados directamente
print(calculadora_1.sumar(2, 5))
print(calculadora_1.restar(10, 9))
print(calculadora_1.multiplicar(5, 9))
print(calculadora_1.dividir(150, 6))
```

### Principios de POO Aplicados

1. **Abstracción**: La clase `Calculadora` abstrae las operaciones matemáticas en métodos específicos (`sumar()`, `restar()`, etc.), ocultando la complejidad de su implementación.

2. **Encapsulamiento**: El atributo `__resultado` está encapsulado (privado) y solo es accesible mediante métodos de la clase, protegiendo los datos y manteniendo la integridad del objeto.

3. **Polimorfismo**: Los métodos de la clase `Calculadora` tienen una interfaz consistente, todos reciben dos parámetros y devuelven un resultado formateado.

## Calculadora Factorial

### Descripción y Forma de Uso

La clase `CalculadoraFactorial` extiende la funcionalidad de `Calculadora` para calcular el factorial de un número.

Ejemplo de uso (como se ve en main.py):

```python
from factorial_poo import CalculadoraFactorial

# Crear una instancia de la calculadora factorial con un número
calculadora_factorial = CalculadoraFactorial(numero=5)

# Calcular el factorial y mostrar el resultado
print(calculadora_factorial.calcular())
```

### Principios de POO Aplicados

1. **Herencia**: `CalculadoraFactorial` hereda de la clase base `Calculadora`, reutilizando sus atributos y métodos, particularmente el método `_multiplicar()`.

2. **Polimorfismo**: La clase sobrescribe el método `_mostrar_operacion()` para adaptarlo a la visualización específica del cálculo factorial.

3. **Encapsulamiento**: Mantiene el encapsulamiento heredado de la clase padre y utiliza apropiadamente los métodos protegidos.

4. **Abstracción**: Proporciona una interfaz simple (`calcular()`) que oculta la complejidad del algoritmo factorial.

## Diferencia entre Implementación Procedimental y Orientada a Objetos

| Aspecto         | Programación Procedimental                            | Programación Orientada a Objetos                                    |
| --------------- | ----------------------------------------------------- | ------------------------------------------------------------------- |
| Organización    | Se centra en funciones y procedimientos               | Se centra en objetos y clases                                       |
| Datos           | Los datos y las funciones están separados             | Los datos y los métodos están unidos en objetos                     |
| Reutilización   | Reutilización de código más difícil                   | Facilita la reutilización mediante herencia                         |
| Mantenimiento   | Puede ser más difícil de mantener en sistemas grandes | Más fácil de mantener y extender                                    |
| Encapsulamiento | No existe formalmente                                 | Los datos pueden encapsularse para proteger su integridad           |
| Modularidad     | Menor modularidad                                     | Mayor modularidad y organización                                    |
| Extensibilidad  | Requiere modificar código existente                   | Permite extender mediante herencia sin modificar el código original |

## Licencia de Publicación

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo LICENSE para más detalles.
