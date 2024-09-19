from src.models.sqlite.entities.natural_person import NaturalPerson
from src.models.sqlite.interfaeces.client_repository import Client

class NaturalPersonRepository(Client):
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection

  def create_natural_person(
    self,
    renda_mensal: float,
    idade: int,
    celular: str,
    email: str,
    categoria: str,
    saldo: float,
  ) -> None:
    with self.__db_connection as database:
      try:
        pessoa_fisica = NaturalPerson(
          renda_mensal=renda_mensal,
          idade=idade,
          celular=celular,
          email=email,
          categoria=categoria,
          saldo=saldo
        )
        database.session.add(pessoa_fisica)
        database.session.commit()

      except Exception as exception:
        database.session.rollback()

        raise exception

  def check_balance(self, pessoa_fisica):
    with self.__db_connection as database:
      try:

        consulta = database.session.query(NaturalPerson).filter_by(nome=pessoa_fisica.nome).first()
        return consulta.saldo

      except Exception as exception:
        database.session.rollback()

        raise exception

  def withdraw_money(self, quantia, pessoa_fisica):
    limite_saque = 5000

    saldo = self.check_balance(pessoa_fisica)

    if quantia <= limite_saque and quantia <= saldo:

      saldo -= quantia
      return f"Saque de R${quantia} realizado com sucesso. Saldo restante: R${saldo}"

    else:
      return "Erro: Quantia de saque excede o limite ou saldo insuficiente."

  def perform_extract(self, pessoa_fisica):
    with self.__db_connection as database:
      try:

        pessoa = database.session.query(NaturalPerson).filter_by(nome=pessoa_fisica.nome).first()
        return {
          "Nome": pessoa.nome,
          "Saldo": pessoa.saldo,
          "categoria": pessoa.categoria,
        }

      except Exception as exception:

        raise exception