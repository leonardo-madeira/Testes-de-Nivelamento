# ⚠ AVISO: neste teste é importante especificar o caminho da pasta <b>dados</b>! 

Em meu computador, usei o caminho <b>"D:/dados/"</b> para realizar o carregamento dos dados em suas determinadas tabelas.

Portanto, é importante vefificar onde se encontra o caminho da pasta <b>dados</b> em seu próprio computador para indicá-lo da maneira correda no arquivo <b>"Script_SQL_Teste3.sql"</b>.

# Exemplo:

A pasta <b>dados</b> em seu computador está no seguinte diretório: <b>"C:/dados/"</b>

Porém, no <b>"Script_SQL_Teste3.sql"</b>, o comando indicado para carregamento de dados nas tabelas é o seguinte: <br><br>
`<b>LOAD DATA INFILE 'D:/dados/Relatorio_cadop.csv'</b>`

Neste caso, a sua pasta está salva no diretório <b>"C"</b> enquanto seu computador está buscando a pasta no diretório <b>"D"</b>

### Dessa forma, basta alterar no <b>"Script_SQL_Teste3.sql"</b> o caminho correto que sua pasta <b>Dados</b> se encontra, da seguinte maneira: <br>
`<b>LOAD DATA INFILE 'C:/dados/Relatorio_cadop.csv'</b>`