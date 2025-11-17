def main():
    # Abre o arquivo de entrada para leitura
    with open("entrada.txt", "r", encoding="utf-8") as arquivo_entrada:
        linhas = arquivo_entrada.readlines()

    novas_linhas = []

    # Processa cada linha do arquivo
    for linha in linhas:

        # Verifica se deve ignorar a linha
        if "ignorar" in linha.lower():
            continue  # pula essa linha

        # Substitui a palavra problema por desafio
        linha = linha.replace("problema", "desafio")
        linha = linha.replace("Problema", "Desafio")

        novas_linhas.append(linha)

    # Grava o resultado no arquivo de saída
    with open("saida.txt", "w", encoding="utf-8") as arquivo_saida:
        for linha in novas_linhas:
            arquivo_saida.write(linha)

    print("Processamento concluído. Arquivo saida.txt criado com sucesso.")

# Chama a função principal
main()
def main():
    # Abre o arquivo de entrada para leitura
    with open("entrada.txt", "r", encoding="utf-8") as arquivo_entrada:
        linhas = arquivo_entrada.readlines()

    novas_linhas = []

    # Processa cada linha do arquivo
    for linha in linhas:

        # Verifica se deve ignorar a linha
        if "ignorar" in linha.lower():
            continue  # pula essa linha

        # Substitui a palavra problema por desafio
        linha = linha.replace("problema", "desafio")
        linha = linha.replace("Problema", "Desafio")

        novas_linhas.append(linha)

    # Grava o resultado no arquivo de saída
    with open("saida.txt", "w", encoding="utf-8") as arquivo_saida:
        for linha in novas_linhas:
            arquivo_saida.write(linha)

    print("Processamento concluído. Arquivo saida.txt criado com sucesso.")