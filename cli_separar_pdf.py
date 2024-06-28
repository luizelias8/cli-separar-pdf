import argparse
from PyPDF2 import PdfReader, PdfWriter

__version__ = '1.0.0'

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

    extrair_paginas(args.pdf_entrada, args.pagina_inicial, args.pagina_final, args.pdf_saida)

if __name__ == '__main__':
    main()