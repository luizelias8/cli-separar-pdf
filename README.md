# Separar PDF

Script simples em Python para separar páginas específicas de um arquivo PDF.

## Visão Geral

Script de linha de comando (CLI) que permite extrair um intervalo de páginas de um PDF e salvar essas páginas em um novo arquivo PDF.

## Funcionalidades

- Extrai páginas específicas de um PDF.
- Salva o PDF separado no diretório especificado ou no diretório atual com nome modificado.
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
python cli_separar_pdf.py <pdf_entrada> <intervalos_paginas> [-d <dir_saida>]
```

### Parâmetros

- `<pdf_entrada>`: Caminho para o arquivo PDF de entrada.
- `<intervalos_paginas>`: Intervalos de páginas para extrair (ex: '1,3-5,7').
- `-d <dir_saida>`: (Opcional) Diretório para salvar o PDF de saída. Se não for especificado, o script salvará no diretório atual.

### Exemplo

Para extrair as páginas 2, 4 a 6, e 8 do arquivo **documento.pdf** e salvar como **documento_1.pdf** no diretório especificado:

```
python cli_separar_pdf.py documento.pdf "2,4-6,8" -d /caminho/para/diretorio
```

Ou, para salvar no diretório atual:

```
python cli_separar_pdf.py documento.pdf "2,4-6,8"
```

### Verificações

O script inclui verificações para garantir a validade e a segurança:

- **Existência do arquivo de entrada**: Verifica se o arquivo PDF de entrada especificado existe. Se o arquivo não for encontrado, o script imprime uma mensagem de erro e encerra a execução.

- **Validação de páginas**:
  - Verifica se o número da página inicial e da página final são maiores que zero.
  - Garante que a página final não seja menor que a página inicial.

## Argumentos Opcionais
- `-v`, `--version`: Exibe a versão do script.

## Contribuição

Contribuições são bem-vindas!

## Autor

[Luiz Elias](https://github.com/luizelias8)