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
    arquivo = open(nome_arquivo, 'r', encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

def escrever_arquivo(resultado):
    with open('etapa-2.txt', 'w', encoding="utf8") as arquivo:
        for ator, media_faturamentos in resultado.items():
            media = sum(media_faturamentos) / len(media_faturamentos)
            arquivo.write(f"{ator}: {media:.2f}\n")


def average_per_actor(linhas_csv):
    cabecalho = valida_campo(linhas_csv[0].strip())
    indice_ator = cabecalho.index('Actor')
    average_billing_index = cabecalho.index('Average per Movie')

    atores_medias = {}

    for linha in linhas_csv[1:]:
        campos = valida_campo(linha.strip())

        ator = campos[indice_ator]
        media_faturamento = float(
            campos[average_billing_index].replace(",", ""))

        if ator in atores_medias:
            atores_medias[ator].append(media_faturamento)
        else:
            atores_medias[ator] = [media_faturamento]

    return atores_medias


def main():
    arquivo_csv = 'actors.csv'
    linhas_csv = le_arquivo(arquivo_csv)
    resultado = average_per_actor(linhas_csv)

    print("Média faturamento dos atores:")
    for ator, media_faturamentos in resultado.items():
        media = sum(media_faturamentos) / len(media_faturamentos)
        print(f"{ator}: {media:.2f}")

    escrever_arquivo(resultado)


if __name__ == "__main__":
    main()
