from Salario import Salario, Empregado
salario = Salario(10000, 700)
emp = Empregado("gabriel", 23, salario)
print(emp.salario_total())