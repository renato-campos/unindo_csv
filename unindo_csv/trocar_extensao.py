import os


def mudar_extensao(pasta, extensao_atual, nova_extensao):
    # Percorre todos os arquivos na pasta
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(extensao_atual):
            # Remove a extensão antiga e adiciona a nova
            novo_nome_arquivo = os.path.splitext(arquivo)[0] + nova_extensao

            # Caminho completo do arquivo antigo e do novo arquivo
            caminho_antigo = os.path.join(pasta, arquivo)
            caminho_novo = os.path.join(pasta, novo_nome_arquivo)

            # Renomeia o arquivo com a nova extensão
            os.rename(caminho_antigo, caminho_novo)

            print(f'{arquivo} renomeado para {novo_nome_arquivo}')


# Exemplo de uso
pasta = 'data_in'
extensao_atual = '.xls'
nova_extensao = '.csv'

mudar_extensao(pasta, extensao_atual, nova_extensao)
