# 'W' foi ultizada para fazer a escrita do arquivo.
# Ao Utilizar 'W' em um arquivo ja existente ele reescreverá todo o conteudo do arquivo, fazendo com que todos os dados sejam apagados. 
arquivo = open('arqText.txt', 'w')

#Função 'Write' é utilizada para gravar informações no arquivo existente.
#O texto em deve ser gravado em aspas simples.
arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')

#A função close ultizada para encerrar o arquivo após a sua ultização. Se tentamos escrever em um arquivo e não fechamos depois de terminar a escrita, as informações não chegarão ao arquivo e nada será escrito.
arquivo.close()

#Leitura de arquivos
#A função 'Read()' ultizada para realizar leitura de todo coteudo do arquivo.
#Parametro 'R' representa que o arquivo esta sendo aberto para leitura.
leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()

# Modo de abertura de arquivos:

# r   - Abre o arquivo somente para leitura.
#       O arquivo deve já existir.

# r+  - Abre o arquivo para leitura e escrita.
#       O arquivo deve já existir.
#       A escrita começa a partir da primeira linha e,
#       caso exista algo escrito no arquivo, as linhas serão reescritas,
#       conforme formos escrevendo.

# w   - Abre o arquivo somente para escrita, no início do arquivo.
#       Apagará o conteúdo do arquivo se ele já existir.
#       Criará um arquivo novo se não existir.

# w+  - Abre o arquivo para escrita e leitura,
#       apagando o conteúdo preexistente.

# a   - Abre o arquivo para escrita no final do arquivo.
#       Não apaga o conteúdo preexistente.

# a+  - Abre o arquivo para escrita no final do arquivo e leitura.
