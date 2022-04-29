"""
Ranking de Breach
"""

while True:
    print('Bem vindo ao ranqueador de vazamento de dados!')
    print(
        'Para que seja possivel a utilizacao da ferramenta e recomendado utilizar o site "https://haveibeenpwned.com/"')
    print('Essa ferramenta mostra os vazamento de informacao que aconteceu atraves do seu e-mail e celular')
    print('\nVamos lá\n')

    while True:
        valor_ranking = []
        empresas_breaches = []
        senha = []
        dica_senha = []
        email = []
        telefone = []
        nome = []
        data = []
        tipo_breaches = ['senha', 'email', 'dica_senha', 'telefone', 'nome']
        breaches = [senha, email, dica_senha, telefone, nome]

        # informa o tipo de dado pesquisado, celular ou e-mail
        tipo_entrada = input('Digite se foi e-mal ou celular que foi utilizado para pesquisa\n')
        valor_entrada = input(f'Digite o {tipo_entrada} digitado\n')

        # informa quantidade de vazamentos no dado pesquisado
        qtd_breaches = int(input('Quantos vazamentos foram encontrados?\n'))

        # colhe as empresas listadas com vazamento
        for i in range(0, qtd_breaches):
            empresas_breaches.append(input(f'Digite a empresa de numero {i + 1} da lista\n'))
            valor_ranking.append(0)
            data.append(input('Qual o ano do vazamento?\n'))

            # colhe os tipos de vazamento de cada empresa
            for j in range(0, len(tipo_breaches)):
                aux = input(
                    f'A empresa {empresas_breaches[i]} teve vazamento de {tipo_breaches[j]}? [1] sim ou [0] nao\n')

                # adiciona a empresa na lista de vazamentos daquela informaçao
                if aux == '1':
                    breaches[j].append(empresas_breaches[i])
                    if tipo_breaches[j] == 'senha':
                        valor_ranking[i] += 10000
                    elif tipo_breaches[j] == 'email':
                        valor_ranking[i] += 1000
                    elif tipo_breaches[j] == 'dica_senha':
                        valor_ranking[i] += 100
                    elif tipo_breaches[j] == 'telefone':
                        valor_ranking[i] += 10
                    elif tipo_breaches[j] == 'nome':
                        valor_ranking[i] += 1

        # estrutura para ordenaçao dos valores de informaçao vazada
        troca = 1
        while troca == 1:
            troca = 0
            for i in range(0, len(valor_ranking) - 1):
                # verifica se o valor da atual é menor que o valor da próxima casa da lista
                if valor_ranking[i] < valor_ranking[i + 1]:
                    # mostra que teve troca de valores
                    troca = 1
                    # inverte os valores do ranking e a ordem das empresas
                    valor_ranking[i], valor_ranking[i + 1] = valor_ranking[i + 1], valor_ranking[i]
                    empresas_breaches[i], empresas_breaches[i + 1] = empresas_breaches[i + 1], empresas_breaches[i]
                    data[i], data[i + 1] = data[i + 1], data[i]

        print(f'\n\nO ranking ficou da seguinte forma para o {tipo_entrada} {valor_entrada}:\n')

        # apresenta o resultado do ranking
        for ordem in range(0, len(empresas_breaches)):
            print(f'A empresa de número {ordem + 1} é a empresa "{empresas_breaches[ordem]}" com o vazamento '
                  f'da informaçoes abaixo que ocorreu no ano de {data[ordem]}')

            # mostras os tipos de informaçoes vazadas
            for itens in range(0, len(tipo_breaches)):
                if empresas_breaches[ordem] in breaches[itens]:
                    print(tipo_breaches[itens])

        # finaliza o programa
        finaliza = input('\nDeseja fazer uma nova consulta? [1] sim ou [0] nao\n')
        if finaliza == '0':
            break

    break
