class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre:", self.nombre, ". Edad:", self.edad, ". Residencia:", self.residencia)

    
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)

        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, ". Antiguedad:", self.antiguedad)

Manuel = Empleado(1500, 55, "Manuel", 55, "Colombia")

Manuel.descripcion()

print(isinstance(Manuel, Persona))#isinstance() devuelve True o False si un objeto pertenece o no a la clase pedida


