def valida_campo(linha):  # Robert Downey, Jr.
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


def ator_com_maior_numero_de_filmes(linhas_csv):
    cabecalho = valida_campo(linhas_csv[0].strip())
    indice_filmes = cabecalho.index('Number of Movies')

    ator_maior_numero_filmes = None
    maior_numero_filmes = 0

    for linha in linhas_csv[1:]:
        campos = valida_campo(linha.strip())

        numero_filmes = int(
            float(campos[indice_filmes].replace(",", "")))

        if numero_filmes > maior_numero_filmes:
            maior_numero_filmes = numero_filmes
            ator_maior_numero_filmes = campos[0]

    return ator_maior_numero_filmes, maior_numero_filmes

def le_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas


def escrever_arquivo(resultado):
    with open('etapa-1.txt', 'w', encoding="utf8") as arquivo:
        arquivo.write(resultado)


def main():
    arquivo_csv = 'actors.csv'
    linhas_csv = le_arquivo(arquivo_csv)
    ator, numero_filmes = ator_com_maior_numero_de_filmes(linhas_csv)

    resultado = f"O ator/atriz com maior número de filmes é '{ator}' com {numero_filmes} filmes."
    print(resultado)

    escrever_arquivo(resultado)


if __name__ == "__main__":
    main()

