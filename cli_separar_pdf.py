import argparse
from PyPDF2 import PdfReader, PdfWriter
import os
import sys

__version__ = '1.0.1'

def extrair_paginas(pdf_entrada, pagina_inicial, pagina_final, pdf_saida):
    """
    Extrai as páginas de pagina_inicial até pagina_final (inclusive) do pdf_entrada e salva em pdf_saida.
    """
    leitor = PdfReader(pdf_entrada)
    escritor = PdfWriter()

    # Ajustar índices de página (PyPDF2 começa do 0)
    pagina_inicial -= 1
    pagina_final -= 1

    for i in range(pagina_inicial, pagina_final + 1):
        escritor.add_page(leitor.pages[i])

    with open(pdf_saida, 'wb') as arquivo_saida:
        escritor.write(arquivo_saida)

    print(f'Páginas {pagina_inicial + 1} a {pagina_final + 1} extraídas para {pdf_saida}')

def main():
    parser = argparse.ArgumentParser(
        prog='separar_pdf', # Nome do CLI
        description='Separar páginas de um PDF'
    )
    parser.add_argument('pdf_entrada', type=str, help='Caminho para o arquivo PDF de entrada')
    parser.add_argument('pagina_inicial', type=int, help='Número da página inicial (começa em 1)')
    parser.add_argument('pagina_final', type=int, help='Número da página final (incluindo esta)')
    parser.add_argument('pdf_saida', type=str, help='Caminho para o arquivo PDF de saída')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    # Verificar se o arquivo PDF de entrada existe
    if not os.path.exists(args.pdf_entrada):
        print(f'Erro: O arquivo "{args.pdf_entrada}" não existe.')
        sys.exit(1)

    # Verificar se as páginas são válidas
    if args.pagina_inicial <= 0:
        print(f'Erro: A página inicial deve ser maior que 0. Você forneceu {args.pagina_inicial}.')
        sys.exit(1)

    if args.pagina_final <= 0:
        print(f'Erro: A página final deve ser maior que 0. Você forneceu {args.pagina_final}.')
        sys.exit(1)

    if args.pagina_final < args.pagina_inicial:
        print(f'Erro: A página final ({args.pagina_final}) não pode ser menor que a página inicial ({args.pagina_inicial}).')
        sys.exit(1)

    extrair_paginas(args.pdf_entrada, args.pagina_inicial, args.pagina_final, args.pdf_saida)

if __name__ == '__main__':
    main()