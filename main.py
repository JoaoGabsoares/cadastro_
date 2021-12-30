from datetime import datetime
import random
from rich.progress import track
from rich import print
from time import sleep

print("[green][bold]<========================================[/][/]")
print("[bold]Sejam Bem-Vindos[/]")
print("[green][bold]<========================================[/][/]")
print("[red][bold]Abaixo você será direcionado ao cadastro e concorrerá a um cartão pré pago![/][/]")

nome_usuario = input('Digite seu nome: ')  # recebo nome do usuario
idade_usuario = int(input('Digite sua idade: '))  # recebe a idade do usuario
aniversario_usuario = datetime.strptime(
    input('Digite sua data de nascimento no formato dd/mm/aaaa: '), '%d/%m/%Y')
###################################################
for i in track(range(10), 'Processando...'):
    sleep(1)

print('[bold]Usuário cadastrado com sucesso![/]')

data_registro = datetime.now()  # data do dia de cadastro
cartoes = ['R$50', 'R$100', 'R$250']  # valor dos cartões a serem sorteados
cartoes = random.choice(cartoes)

print(f'Olá [green][bold]{nome_usuario}[/][/], seu registro foi concluido com sucesso no dia {data_registro.day}/{data_registro.month}/{data_registro.year} . \n [bold]Parabéns[/], houve um sorteio e você foi [bold]premiado(a)[/] com um cartão pré pago no valor de [bold]{cartoes}[/]')
