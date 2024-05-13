x = input("Digite o valor correspondente ao número de segundos que deseja converter: ")
x = int(x)
dias = x // 86400
horas = (x % 86400) // 3600
minutos = ((x % 86400) % 3600) // 60
segundos = ((x % 86400) % 3600) % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")