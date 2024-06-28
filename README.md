# Separar PDF

Script simples em Python para separar páginas específicas de um arquivo PDF.

## Visão Geral

Script de linha de comando (CLI) que permite extrair um intervalo de páginas de um PDF e salvar essas páginas em um novo arquivo PDF.

## Funcionalidades

- Extrai páginas específicas de um PDF.
- Gera um novo arquivo PDF com as páginas extraídas.
- Suporta a especificação das páginas.

## Requisitos

- Python 3.x
- PyPDF2

## Instalação

Clone o repositório:

```
git clone https://github.com/luizelias8/cli-separar-pdf.git
cd cli-separar-pdf
```

Instale os requisitos necessários:
```
pip install -r requirements.txt
```

## Uso

Para usar o script, execute seguido dos parâmetros necessários:

```
python cli_separar_pdf.py <pdf_entrada> <pagina_inicial> <pagina_final> <pdf_saida>
```

### Parâmetros

- `<pdf_entrada>`: Caminho para o arquivo PDF de entrada.
- `<pagina_inicial>`: Número da página inicial.
- `<pagina_final>`: Número da página final.
- `<pdf_saida>`: Caminho para o arquivo PDF de saída.

### Exemplo

Para extrair as páginas 2 a 4 de **documento.pdf** e salvar em **saida.pdf**:

```
python cli_separar_pdf.py documento.pdf 2 4 saida.pdf
```

## Argumentos Opcionais
- `-v`, `--version`: Exibe a versão do script.

## Contribuição

Contribuições são bem-vindas!

## Autor

[Luiz Elias](https://github.com/luizelias8)