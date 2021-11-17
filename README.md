# Fibonacci-Recursivo
Programa que devolve o n-ésimo elemento da sequência de Fibonacci solicitado ao rodar o programa utilizando algoritmo recursivo.

O algoritmo recursivo tem como base a utilização de funções que chamem a elas próprias. Esses algoritmos geralmente são mais simples que suas contra partes não recursivas, mas podem demandar muito recurso rapidamente.

No caso do algoritmo de cálculo do n-ésimo elemento de Fibonacci, a recurção para e começa a calcular o resultado quando o número chega em 1 ou 0 e começa a voltar nas chamadas para terminar, como pode ser visto na parte que faz esse cálculo:
  
def recursive_fibo(self, n_esimo):

    if n_esimo == 1 or n_esimo == 0 :
        return n_esimo               
    return self.recursive_fibo(n_esimo - 1) + self.recursive_fibo(n_esimo - 2)  

Por exemplo, ao calcular o valor de 5, ao entrar pela primeira vez n função, 5 não é 1 nem 0, então chama a própria função com 4 para depois somar com o resultado da função chamando com 3. Ao entrar com 4, ele chama a ela própria com 3 e com 2 e ao entrar com 3 ele chama a ela própria com 2 e com 1.

Prosseguindo com o algoritmo então, vai sendo empilhado as chamadas à função, que, somente ao chegar na condição de base começa a desempilhar e somar os resultados.

Por conta disso esse tipo de algoritmo consome muito recurso muito rápido, com um valor de n não tão grande o processo já começa a demorar muito.

O <i>Big O</i> desse algoritmo é <i>O(2^n)</i>. Caso queira saber mais sobre complexidade de algoritmos, há mais informações <a href="https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/">nesse link</a>.
