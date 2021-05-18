# Projeto2 - ARIES Micro-Estações

Aluno:
Gabriel Vilaça

Link do Website(Heroku):
https://safe-spire-18268.herokuapp.com/

Descrição:
A Aries Micro-Estações é uma plataforma de monitoramento dinâmico de parâmetros climáticos georreferenciados, que podem ser visualizados via gráficos, e possibilitam o usuário receber alertas nas estações em que este se cadastra. A ferramenta possui algumas funcionalidades, como:

* Criar de usuários (Login e Sign Up e Log Out)
* Criar e deletar estações
* Criar e deletar parâmetros de monitoramento dessas estações
* Monitoramento dos valores dos parâmetros via 3 tipos de gráficos diferentes (Graph.js)
* Monitoramento da localização da origem dos dados (Google Maps Embed)
* Inscrição do usuário nos parâmetros nos quais deseja receber alertas (Emails via MAILGUN API)

## Criar Usuários 

Nestas telas, o usuário pode se cadastrar e logar na plataforma.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/118579650-dac6b400-b764-11eb-9087-889428a35c02.png" width="600" height="500"></img>
  <img src="https://user-images.githubusercontent.com/60860861/118579720-fc27a000-b764-11eb-9c24-3b55bfff5626.png" width="600" height="500"></img>
</p>

## Tela Principal (Criar e Deletar Estações/ Criar e deletar parâmetros de monitoramento dessas estações)

Nesta tela, o usuário pode criar novas estações com o forms central e clicando em Criar. Cada estação irá aparecer como um objeto na parte inferior. As estações podem ser apagadas com o ícone de lixeira Azul. Caso o usuário queira adicionar um parâmetro de leitura a uma dessas estações, basta escrever na caixa parâmetro e clicar em Adicionar Parâmetro. Os parâmetros estão contidos na caixa dropdown em cada card de estação logo acima do forms de criar parâmetros. Basta passar o mouse em cima e clicar em um parâmetro para observar. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/118582625-09935900-b76a-11eb-909e-33cad6827d9e.png" width="1000" height="600"></img>
</p>

## Monitoramento dos valores dos parâmetros via 3 tipos de gráficos diferentes (Graph.js)

Nesta tela, o usuário pode visualizar os dados obtidos pelo parâmetro no formato de gráfico. Ao clicar em gráfico, é possível escolher outras 2 opções de visualização. O usuário pode também apagar o parâmetro ao clicar no ícone azul com a lixeira no canto superior. Há também os botões de localização e de inscrição, que serão descritos adiante.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/118581207-9b4d9700-b767-11eb-922b-c54fdcb76c22.png" width="800" height="600"></img>
</p>

## Monitoramento da localização da origem dos dados (Google Maps Embed)

Nesta tela, o usuário pode visualizar a localização de origem dos dados, a partir do Google Maps Embed, que utiliza as coordenadas obtidas pela leitura dos dados, e coloca o marcador no local. A tela também indica qual é o id do parâmetro, que é utilizado para receber os dados da estação física.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/118581837-b076f580-b768-11eb-9e99-dd5def32920e.png" width="600" height="600"></img>
</p>

## Inscrição do usuário nos parâmetros nos quais deseja receber alertas (Emails via MAILGUN API)

Nesta tela, o usuário pode se cadastrar no parâmetro escolhido, ao colocar um valor Threshold de análise. Este valor será lido a cada vez que o servidor receber novos dados, e enviará um email para os usuários cadastrados nos parâmetros escolhidos quando os valores recebidos pelo servidor para aquele parâmetro excederem o valor do Threshold. O serviço de email é feito pela API MAILGUN.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/118581915-e025fd80-b768-11eb-8957-be8ba7aa745c.png" width="600" height="600"></img>
</p>

## Enviando dados com o sendremote.py

O arquivo sendremote no repositório é utilizado para enviar dados para o servidor. Para enviar um dado ao servidor, basta o usuário alterar o valor parameter pelo parameter id obtido na tela de localização. Assim, ao enviar os dados, o servidor saberá para qual será o parâmetro que os dados serão enviados.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/118582469-c2a56380-b769-11eb-80eb-7879ec66f886.png" width="600" height="600"></img>
</p>
