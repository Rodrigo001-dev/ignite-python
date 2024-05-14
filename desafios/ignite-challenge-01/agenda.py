def adicionar_contato(contatos, nome_contato, telefone, email):

  contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"Contato {nome_contato} foi adicionada com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "✓" if contato["favorito"] else " "
    nome_contato = contato["nome"]
    print(f"{indice}. [{status}] {nome_contato}")

  return

def ver_contatos_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      status = "✓" 
      nome_contato = contato["nome"]
      print(f"{indice}. [{status}] {nome_contato}")

  return

def atualizar_numero_contato(contatos, indice_contato, novo_numero_contato):
  indice_contato_ajustado = int(indice_contato) - 1

  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["telefone"] = novo_numero_contato
    print(f"Contato {indice_contato} atualizado para {novo_numero_contato}")
  else: 
    print("Índice de contato inválido")

  return

def marcar_contato_como_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1

  contatos[indice_contato_ajustado]["favorito"] = True
  print(f"Contato {indice_contato} marcado como favorito")
  
  return

def desmarcar_contato_como_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1

  contatos[indice_contato_ajustado]["favorito"] = False
  print(f"Contato {indice_contato} desmarcado como favorito")
  
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1

  contatos.remove(contatos[indice_contato_ajustado])
      
  print("Contato deletado.")
  return

contatos = []
while True:
  print("\nMenu do Gerenciador de Lista de tarefas:")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Ver contatos favoritos")
  print("4. Atualizar numero do contato")
  print("5. Marcar contato como favorito")
  print("6. Desmarcar contato como favorito")
  print("7. Deletar contato")
  print("8. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    telefone = input("Digite o telefone do contato que deseja adicionar: ")
    email = input("Digite o email do contato que deseja adicionar: ")
    adicionar_contato(contatos, nome_contato, telefone, email)

  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    ver_contatos_favoritos(contatos)

  elif escolha == "4":
    indice_contato = input("Digite o número do contato que deseja atualizar: ")
    novo_numero = input("Digite o novo numero do contato: ")
    atualizar_numero_contato(contatos, indice_contato, novo_numero)

  elif escolha == "5":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja marcar como favorito:")
    marcar_contato_como_favorito(contatos, indice_contato)

  elif escolha == "6":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja desmarcar como favorito:")
    desmarcar_contato_como_favorito(contatos, indice_contato)

  elif escolha == "7":
    indice_contato = input("Digite o número do contato que deseja deletar:")
    deletar_contato(contatos, indice_contato)
    ver_contatos(contatos)

  elif escolha == "8":
    break

print("Programa finalizado")