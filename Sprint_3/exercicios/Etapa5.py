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
    with open('etapa-5.txt', 'w', encoding="utf8") as arquivo:
        arquivo.write(
            "Lista dos atores ordenada pelo faturamento bruto total (em ordem decrescente):\n")
        for ator, faturamento in resultado:
            arquivo.write(f"{ator}: {faturamento:.2f}\n")


def faturamento_total_por_ator(linhas_csv):
    cabecalho = valida_campo(linhas_csv[0].strip())
    indice_ator = cabecalho.index('Actor')
    indice_total_gross = cabecalho.index('Total Gross')

    faturamento_por_ator = {}

    for linha in linhas_csv[1:]:
        campos = valida_campo(linha.strip())

        ator = campos[indice_ator]
        total_gross = float(campos[indice_total_gross].replace(',', ''))

        if ator in faturamento_por_ator:
            faturamento_por_ator[ator] += total_gross
        else:
            faturamento_por_ator[ator] = total_gross

    return faturamento_por_ator


def main():
    arquivo_csv = 'actors.csv'
    linhas_csv = le_arquivo(arquivo_csv)
    faturamento_por_ator = faturamento_total_por_ator(linhas_csv)

    atores_ordenados_por_faturamento = sorted(
        faturamento_por_ator.items(), key=lambda item: item[1], reverse=True)

    print("Lista dos atores")
    for ator, faturamento in atores_ordenados_por_faturamento:
        print(f"{ator}: {faturamento:.2f}")

    escrever_arquivo(atores_ordenados_por_faturamento)


if __name__ == "__main__":
    main()