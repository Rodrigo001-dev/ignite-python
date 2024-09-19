class NaturalPersonController:
  def __init__(self, natural_person_repository):
    self.natural_person_repository = natural_person_repository

  def create_natural_person(self, renda_mensal, idade, celular, email, categoria, saldo):
    try:
      self.natural_person_repository.create_natural_person(
        renda_mensal=renda_mensal,
        idade=idade,
        celular=celular,
        email=email,
        categoria=categoria,
        saldo=saldo
      )
    except Exception as exception:
      raise exception

  def check_balance(self, nome_pessoa_fisica):
    try:
      saldo = self.natural_person_repository.check_balance(nome_pessoa_fisica)
      return saldo
    except Exception as exception:
      raise exception

  def withdraw_money(self, quantia, nome_pessoa_fisica):
    try:
      mensagem = self.natural_person_repository.withdraw_money(quantia, nome_pessoa_fisica)
      return mensagem
    except Exception as exception:
      raise exception

  def perform_extract(self, nome_pessoa_fisica):
    try:
      extrato = self.natural_person_repository.perform_extract(nome_pessoa_fisica)
      return extrato
    except Exception as exception:
      raise exception