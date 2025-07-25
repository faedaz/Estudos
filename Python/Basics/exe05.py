'''Descrição: Crie um script que gere um pequeno relatório sobre um funcionário. O script deve:
Pedir o nome do funcionário 
Pedir a quantidade de horas trabalhadas no mês 
Pedir o valor que ele recebe por hora 
Calcular o salário bruto do funcionário 
Exibir um relatório formatado com o nome do funcionário e o salário bruto calculado.'''

# Asks for the employee's data
employee_name = input("Type your name: ")
hours_worked = int(input("Hours worked this month: "))
hourly_rate = float(input("Type your payment per hour: $"))

gross_salary = hours_worked * hourly_rate

print(f"""
--- Monthly Report ---
Employee Name: {employee_name}
Gross Salary: ${gross_salary:.2f}
----------------------
Calculation Details:
- Hours Worked: {hours_worked}
- Hourly Rate: ${hourly_rate:.2f}
""")