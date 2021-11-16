# Esse código visa responder a questão 1
# Gabriel de Souza Alves


class Fibo:
    def __init__(self, requested_interactions):
        self.target_interactions = requested_interactions

    def calc_fibo(self):
        if self.target_interactions < 0:
            return print("Utilize um valor positivo para encontrar o n-ésimo valor da sequência de Fibonacci.")
        if self.target_interactions == 0: #caso o número de interações seja 0, sempre retorna 0 sem fazer operação recursiva
            return 0
        if self.target_interactions == 1 or self.target_interactions == 2: #caso o número de interações seja 1 ou 2, sempre retorna 1 sem fazer operação recursiva
            return 1
        else:
            return self.recursive_fibo(self.target_interactions)

    def recursive_fibo(self, n_esimo):
        if n_esimo == 1 or n_esimo == 0 :#Aqui é verificado para parar a recursão ao chegar aos termos básicos de Fibonacci
            return n_esimo               #É verificado tanto 0 qu
        return self.recursive_fibo(n_esimo - 1) + self.recursive_fibo(n_esimo - 2)         


def main():
    import sys
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Entre com um valor inteiro positivo após o nome do programa, exemplo: 'python RecursiveFibonacci 1' ")
        return
    user_value = sys.argv[1]
    try:
        user_value_int = int(user_value)
    except ValueError as e:
        print("Entre com um valor inteiro positivo como argumento do programa.")
        return
    
    user_fibo = Fibo(user_value_int)
    print(user_fibo.calc_fibo())

if __name__ == "__main__": 
    main()        