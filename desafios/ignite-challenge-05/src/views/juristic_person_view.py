class PessoaJuridicaView:
  def __init__(self, juristic_person_controller):
    self.juristic_person_controller = juristic_person_controller

  def create_juristic_person(self, request):
    try:
      faturamento = request.get('faturamento')
      idade = request.get('idade')
      nome_fantasia = request.get('nome_fantasia')
      celular = request.get('celular')
      email = request.get('email')
      categoria = request.get('categoria')
      saldo = request.get('saldo')

      self.juristic_person_controller.criar_pessoa_juridica(
        faturamento=faturamento,
        idade=idade,
        nome_fantasia=nome_fantasia,
        celular=celular,
        email=email,
        categoria=categoria,
        saldo=saldo
      )

      return "Pessoa jurídica cadastrada com sucesso."

    except Exception as e:
      return str(e)

  def check_balance(self, request):
    try:
      nome_pessoa_juridica = request.get('nome_pessoa_juridica')

      saldo = self.juristic_person_controller.check_balance(nome_pessoa_juridica)

      return f"Saldo da pessoa jurídica {nome_pessoa_juridica}: {saldo}"

    except Exception as e:
      return str(e)

  def withdraw_money(self, request):
    try:
      quantia = request.get('quantia')
      nome_pessoa_juridica = request.get('nome_pessoa_juridica')

      mensagem = self.juristic_person_controller.withdraw_money(quantia, nome_pessoa_juridica)

      return mensagem

    except Exception as e:
      return str(e)

  def perform_extract(self, request):
    try:
      nome_pessoa_juridica = request.get('nome_pessoa_juridica')

      extrato = self.juristic_person_controller.perform_extract(nome_pessoa_juridica)

      return extrato

    except Exception as e:
      return str(e)