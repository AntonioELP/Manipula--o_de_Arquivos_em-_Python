# Manipulação_de_Arquivos_em _Python

Este projeto faz parte de uma atividade de faculdade sobre manipulação de arquivos texto usando Python.

O objetivo é:

Ler o conteúdo de um arquivo chamado entrada.txt

Processar o texto seguindo algumas regras

Salvar o resultado em saida.txt

Manter o arquivo original sem alterações

📁 Arquivos Necessários
1. programa.py

Arquivo principal do código em Python (você pode usar esse nome ou outro de sua preferência).

2. entrada.txt

Arquivo de texto criado manualmente, contendo o texto que será processado.

O arquivo entrada.txt deve ficar na mesma pasta do programa e deve conter o seguinte conteúdo:

Este é um problema simples.
Podemos resolver este problema facilmente.
Esta linha deve ser ignorada.
Outro problema aparece aqui.
Linha comum sem problemas.

🔧 Regras de Processamento

O programa faz três operações:

Substitui todas as palavras "problema" por "desafio".

Remove qualquer linha que contenha a palavra "ignorar".

Mantém todas as outras linhas como estão.

📝 Resultado Esperado (saida.txt)

Após rodar o programa, será criado automaticamente um arquivo chamado saida.txt com o conteúdo:

Este é um desafio simples.
Podemos resolver este desafio facilmente.
Outro desafio aparece aqui.
Linha comum sem desafios.

▶️ Como Executar

Tenha o Python instalado no computador.

Coloque os arquivos programa.py e entrada.txt na mesma pasta.

Abra o terminal ou CMD na pasta do projeto.

Execute o comando:

python programa.py


Será criado o arquivo saida.txt com o texto processado.

✔️ Observações

O arquivo entrada.txt não é modificado.

Apenas o arquivo saida.txt é criado/alterado.

O código foi escrito de forma simples, próprio para iniciantes.
