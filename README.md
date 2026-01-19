Gerador de QR Code 🎥
Este é um script simples em Python que automatiza a criação de QR Codes em ambientes de trabalho. Nesse script ao invés de colar a URL completa, o usuário insere apenas o ID do final da página, e o programa gera a imagem correspondente, criei especificamente para usar em meu trabalho.

🚀 Funcionalidades
URL Dinâmica: Você utiliza uma base fixa, permitindo a geração rápida através de IDs.

F-Strings: Uso de formatação moderna de strings para construção de caminhos e URLs.

Automação: Gera e salva o arquivo .png diretamente em um diretório específico.

🛠️ Tecnologias Utilizadas
Python (v3.11+)

Biblioteca qrcode

Biblioteca Pillow (para processamento de imagem)

📋 Pré-requisitos
Antes de rodar o script, você precisará instalar as dependências necessárias:

Bash

pip install qrcode Pillow
🔧 Como usar
Clone o repositório ou baixe o arquivo .py.

Certifique-se de que o caminho definido na variável file_path existe em sua máquina.

Execute o script:

Bash

python nome_do_seu_arquivo.py
Quando solicitado, digite o ID do link (ex: 324).

O QR Code será gerado e salvo na pasta configurada.

📝 O Código
O coração do projeto utiliza a classe QRCode para configurar a imagem e o método add_data para inserir a URL formatada
# Trecho principal
f_string = f"{base_url}{final_id}"
qr.add_data(f_string)
