from despesas import cadastrar, listar

# Testando o cadastro
cadastrar("Internet", 150.00, "Mensalidade de Janeiro", "2024-01-30")

# Testando a listagem
todas_despesas = listar()
for d in todas_despesas:
    print(d)