from src.models.sqlite.entities.juristic_person import JuristicPerson
from src.models.sqlite.interfaeces.client_repository import Client

class JuristicPersonRepository(Client):
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection

  def create_juristic_person(
    self,
    faturameno: float,
    idade: int,
    nome_fantasia: str,
    celular: str,
    email: str,
    categoria: str,
    saldo: float,
  ) -> None:
    with self.__db_connection as database:
      try:
        pessoa_fisica = JuristicPerson(
          faturameno=faturameno,
          idade=idade,
          nome_fantasia=nome_fantasia,
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

  def check_balance(self, pessoa_juridica):
    with self.__db_connection as database:
      try:

        consulta = database.session.query(JuristicPerson).filter_by(nome=pessoa_juridica.nome_fantasia).first()
        return consulta.saldo

      except Exception as exception:
        database.session.rollback()

        raise exception

  def withdraw_money(self, quantia, pessoa_juridica):
    limite_saque = 10000

    saldo = self.check_balance(pessoa_juridica)

    if quantia <= limite_saque and quantia <= saldo:

      saldo -= quantia
      return f"Saque de R${quantia} realizado com sucesso. Saldo restante: R${saldo}"

    else:
      return "Erro: Quantia de saque excede o limite ou saldo insuficiente."

  def perform_extract(self, pessoa_juridica):
    with self.__db_connection as database:
      try:

        pessoa = database.session.query(JuristicPerson).filter_by(nome=pessoa_juridica.nome_fantasia).first()
        return {
          "Nome": pessoa.nome_fantasia,
          "Saldo": pessoa.saldo,
          "categoria": pessoa.categoria,
        }

      except Exception as exception:

        raise exception