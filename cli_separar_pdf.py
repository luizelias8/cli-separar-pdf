import argparse
from PyPDF2 import PdfReader, PdfWriter
import os
import sys

__version__ = '3.2.0'

def parsear_intervalos_paginas(intervalo_paginas):
    """
    Converte uma string de intervalos de páginas em uma lista de números de páginas.
    Exemplo: '1,3-5,7' -> [1, 3, 4, 5, 7]
    """
    paginas = set()
    intervalos = intervalo_paginas.split(',')

    for intervalo in intervalos:
        if '-' in intervalo:
            inicio, fim = map(int, intervalo.split('-'))
            if inicio > 0 and fim > 0 and fim >= inicio:
                paginas.update(range(inicio, fim + 1))
            else:
                print(f'Erro: Intervalo de páginas inválido: {intervalo}')
                sys.exit(1)
        else:
            pagina = int(intervalo)
            if pagina > 0:
                paginas.add(pagina)
            else:
                print(f'Erro: Número de página inválido: {pagina}')
                sys.exit(1)

    return sorted(paginas)

def extrair_paginas(pdf_entrada, intervalos_paginas, dir_saida, nome_arquivo_base):
    """
    Extrai as páginas de pagina_inicial até pagina_final (inclusive) do pdf_entrada e salva em pdf_saida.
    """
    leitor = PdfReader(pdf_entrada)

    # Processar cada conjunto de intervalos de páginas separado por ';'
    intervalos_conjuntos = intervalos_paginas.split(';')
    for contador, intervalos in enumerate(intervalos_conjuntos, start=1):
        escritor = PdfWriter()
        paginas = parsear_intervalos_paginas(intervalos)

        for pagina in paginas:
            if pagina <= len(leitor.pages):
                escritor.add_page(leitor.pages[pagina - 1]) # Ajustar para índice zero
            else:
                print(f'Erro: Página {pagina} não existe no documento.')
                sys.exit(1)

        novo_nome = f'{nome_arquivo_base}_{contador}.pdf'
        caminho_saida = os.path.join(dir_saida, novo_nome)

        with open(caminho_saida, 'wb') as arquivo_saida:
            escritor.write(arquivo_saida)

        print(f'Páginas {intervalos_paginas} extraídas para {caminho_saida}')

def main():
    parser = argparse.ArgumentParser(
        prog='separar_pdf', # Nome do CLI
        description='Separar páginas de um PDF'
    )
    parser.add_argument('pdf_entrada', type=str, help='Caminho para o arquivo PDF de entrada')
    parser.add_argument('intervalos_paginas', type=str, help='Intervalos de páginas para extrair (ex: 1,3-5,7)')
    parser.add_argument('-d', '--dir_saida', type=str, default=None, help='Diretório para salvar o PDF de saída (opcional)')
    parser.add_argument('-n', '--nome_base', type=str, default=None, help='Nome base para os arquivos PDF de saída (opcional)')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    # Verificar se o arquivo PDF de entrada existe
    if not os.path.exists(args.pdf_entrada):
        print(f'Erro: O arquivo "{args.pdf_entrada}" não existe.')
        sys.exit(1)

    # Determinar o diretório de saída
    if args.dir_saida:
        if not os.path.exists(args.dir_saida):
            print(f'Erro: O diretório "{args.dir_saida}" não existe.')
            sys.exit(1)
        dir_saida = args.dir_saida
    else:
        dir_saida = os.getcwd()

    # Determinar o nome base do arquivo
    if args.nome_base:
        nome_arquivo_base = args.nome_base
    else:
        nome_arquivo_base, _ = os.path.splitext(os.path.basename(args.pdf_entrada))

    extrair_paginas(args.pdf_entrada, args.intervalos_paginas, dir_saida, nome_arquivo_base)

if __name__ == '__main__':
    main()