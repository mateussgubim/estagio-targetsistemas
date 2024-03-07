# estagio-targetsistemas
Questões do desafio para o estágio da Target Sistemas

1 - Observe o trecho de código abaixo: 
```
int INDICE = 13, SOMA = 0, K = 0; 

 	enquanto K < INDICE faça 

	{ 

		K = K + 1; 

		SOMA = SOMA + K; 

	} 

 	imprimir(SOMA); 
```
P: Ao final do processamento, qual será o valor da variável SOMA?

R: O valor será 91.

2 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:  

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 

Clique [aqui](/resoluções/fibonacci.py) para acessar a resolução.

3 - Descubra a lógica e complete o próximo elemento:  
```
a) 1, 3, 5, 7, `9`

b) 2, 4, 8, 16, 32, 64, `128`

c) 0, 1, 4, 9, 16, 25, 36, `49`

d) 4, 16, 36, 64, `100`

e) 1, 1, 2, 3, 5, 8, `13`

f) 2, 10, 12, 16, 17, 18, 19, `20`
```

4 - Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

R: Supondo que todos os interruptores estejam na posição de desligado, eu ligaria o primeiro e o terceiro, e verificaria quais lâmpadas acenderam. Após isso, voltaria e apagaria o último interruptor, e veria novamente qual lâmpada foi apagada; dessa maneira, conseguiria descobrir qual lâmpada é controlada por cada interruptor.

    O primeiro controla a lâmpada que ficou acesa o tempo todo.

    O segundo controla a lâmpada que não foi acesa em momento algum.

    O terceiro controla a lâmpada que foi apagada durante a segunda interação.

5) Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: 

	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

	b) Evite usar funções prontas, como, por exemplo, reverse; 

Clique [aqui](/resoluções/invert-order.py) para acessar a resolução.
