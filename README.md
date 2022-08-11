# sugarscape_competition

Esse modelo e uma variacao do modelo sugarscape_cg dos exemplos do mesa. Foi introduzida uma nova classe de agente, que serve como competidora pelo acucar disponivel. Foram introduzidas na interface duas variaveis manipulaveis que controlam a quantidade de agentes de cada classe, e tambem uma variavel dependente nova que representa a media de ganho de peso dos agentes.

# hipotese causal

A hipotese e de que um aumento na quantidade de competidores ira causar uma queda na quantidade de agentes vivos e no peso medio dos agentes apos uma quantidade de passos.

# justificativa

As alteracoes feitas permitem simular competicao interespecifica, e providenciam uma forma de verificar o ganho de peso dos agentes de forma simplificada.

# orientacoes

para rodar o simulador use o comando python3 run.py na pasta sugarscape_competition/sugarscape_cg. use os sliders para definir a quantidade de agentes de cada classe. aperte reset para efetuar as mudancas no modelo. os botoes start e step permitem fazer a simulacao avancar.

# variaveis

a variavel SsAgent mostrada no grafico e a quantidade de todos os agentes da classe SsAgent. a variavel SsAgentMassAvg mostra a media do ganho de peso dos agentes dessa classe.
