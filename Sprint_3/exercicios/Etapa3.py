
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

def le_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

def escrever_arquivo(resultado):
    with open('etapa-3.txt', 'w', encoding="utf8") as arquivo:
        arquivo.write(resultado)


def ator_com_maior_media_faturamento(linhas_csv):
    cabecalho = valida_campo(linhas_csv[0].strip())
    indice_ator = cabecalho.index('Actor')
    indice_media_faturamento = cabecalho.index('Average per Movie')

    ator_maior_media = None
    maior_media = 0

    for linha in linhas_csv[1:]:
        campos = valida_campo(linha.strip())
        ator = campos[indice_ator]
        media_faturamento = float(
            campos[indice_media_faturamento].replace(",", ""))

        if media_faturamento > maior_media:
            maior_media = media_faturamento
            ator_maior_media = ator

    return ator_maior_media, maior_media


def main():
    arquivo_csv = 'actors.csv'
    linhas_csv = le_arquivo(arquivo_csv)
    ator_maior_media, maior_media = ator_com_maior_media_faturamento(linhas_csv)

    resultado = f"O ator/atriz com maior média de faturamento por filme é '{ator_maior_media}' com média de {maior_media:.2f}"
    print(resultado)
    escrever_arquivo(resultado)


if __name__ == "__main__":
    main()