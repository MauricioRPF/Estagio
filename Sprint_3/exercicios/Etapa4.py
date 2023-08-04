def valida_campo(linha):
    campos = []
    campo = ""
    aspas = False

    for char in linha:
        if char == ',' and not aspas:
            campos.append(campo.strip())
            campo = ""
        else:
            campo += char
            if char == '"':
                aspas = not aspas

    campos.append(campo.strip())
    return campos


def encontrar_filmes_mais_frequentes(linhas_csv):
    cabecalho = valida_campo(linhas_csv[0].strip())
    indice_filme = cabecalho.index('#1 Movie')

    filmes_frequencias = {}

    for linha in linhas_csv[1:]:
        campos = valida_campo(linha.strip())

        filme = campos[indice_filme]

        if filme in filmes_frequencias:
            filmes_frequencias[filme] += 1
        else:
            filmes_frequencias[filme] = 1

    filmes_mais_frequentes = sorted(
        filmes_frequencias.items(), key=lambda item: item[1], reverse=True)

    return filmes_mais_frequentes

def le_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

def escrever_arquivo(resultado):
    with open('etapa-4.txt', 'w', encoding="utf8") as arquivo:
        arquivo.write("O(s) filme(s) mais frequente(s) é(são):\n")
        for filme, frequencia in resultado:
            arquivo.write(f"{filme}: {frequencia} vezes\n")

        arquivo.write(
            "\nO filmes que aparecem uma vez \n")


def main():
    arquivo_csv = 'actors.csv'
    linhas_csv = le_arquivo(arquivo_csv)
    filmes_mais_frequentes = encontrar_filmes_mais_frequentes(linhas_csv)

    filmes_com_mais_de_uma_vez = [
        (filme, frequencia) for filme, frequencia in filmes_mais_frequentes if frequencia > 1]

    print("Os filmes mais frequentes são:")
    for filme, frequencia in filmes_com_mais_de_uma_vez:
        print(f"{filme}: {frequencia} vezes")

    print("\nO filmes que aparecem uma vez na coluna")

    escrever_arquivo(filmes_com_mais_de_uma_vez)


if __name__ == "__main__":
    main()