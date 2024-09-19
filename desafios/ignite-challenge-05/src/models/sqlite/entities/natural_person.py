from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, String, BIGINT, REAL

class NaturalPerson(Base):
  __tablename__ = "pessoa_fisica"

  id = Column(BIGINT, primary_key=True)
  renda_mensal = Column(REAL, nullable=False)
  idade = Column(BIGINT, nullable=False)
  celular = Column(String, nullable=False)
  email = Column(String, nullable=False)
  categoria = Column(String, nullable=False)
  saldo = Column(REAL, nullable=False)

  def __repr__(self):
    return f"Nome: {self.nome}, Idade: {self.idade}, Saldo: {self.saldo}"