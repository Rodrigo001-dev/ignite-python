class NaturalPersonView:
  def __init__(self, natural_person_controller):
    self.natural_person_controller = natural_person_controller

  def create_natural_person(self, request):
    try:
      # Obter os parâmetros do request
      renda_mensal = request.get('renda_mensal')
      idade = request.get('idade')
      celular = request.get('celular')
      email = request.get('email')
      categoria = request.get('categoria')
      saldo = request.get('saldo')

      # Chamar o método da controladora para cadastrar pessoa física
      self.natural_person_controller.create_natural_person(
        renda_mensal=renda_mensal,
        idade=idade,
        celular=celular,
        email=email,
        categoria=categoria,
        saldo=saldo
      )

      # Retornar uma mensagem de sucesso
      return "Pessoa física cadastrada com sucesso."
  
    except Exception as e:
      # Lidar com exceção
      return str(e)

  def check_balance(self, request):
    try:
      nome_pessoa_fisica = request.get('nome_pessoa_fisica')

      saldo = self.natural_person_controller.check_balance(nome_pessoa_fisica)

      return f"Saldo da pessoa física {nome_pessoa_fisica}: {saldo}"

    except Exception as e:
      return str(e)

  def withdraw_money(self, request):
    try:
      quantia = request.get('quantia')
      nome_pessoa_fisica = request.get('nome_pessoa_fisica')

      mensagem = self.natural_person_controller.withdraw_money(quantia, nome_pessoa_fisica)

      return mensagem

    except Exception as e:
      return str(e)

  def perform_extract(self, request):
    try:
      nome_pessoa_fisica = request.get('nome_pessoa_fisica')

      extrato = self.natural_person_controller.perform_extract(nome_pessoa_fisica)

      return extrato

    except Exception as e:
      return str(e)