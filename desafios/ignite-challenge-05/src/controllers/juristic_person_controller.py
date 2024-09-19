class JuristicPersonController:
  def __init__(self, juristic_person_repository):
    self.juristic_person_repository = juristic_person_repository

  def create_juristic_person(self, faturamento, idade, nome_fantasia, celular, email, categoria, saldo):
    try:
      self.juristic_person_repository.create_juristic_person(
        faturamento=faturamento,
        idade=idade,
        nome_fantasia=nome_fantasia,
        celular=celular,
        email=email,
        categoria=categoria,
        saldo=saldo
      )
    except Exception as exception:
      raise exception

  def check_balance(self, nome_pessoa_juridica):
    try:
      saldo = self.juristic_person_repository.check_balance(nome_pessoa_juridica)
      return saldo
    except Exception as exception:
      raise exception

  def withdraw_money(self, quantia, nome_pessoa_juridica):
    try:
      mensagem = self.juristic_person_repository.withdraw_money(quantia, nome_pessoa_juridica)
      return mensagem
    except Exception as exception:
      raise exception

  def perform_extract(self, nome_pessoa_juridica):
    try:
      extrato = self.juristic_person_repository.perform_extract(nome_pessoa_juridica)
      return extrato
    except Exception as exception:
      raise exception