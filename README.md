# py-crazy-calculator
Projeto de calculadora usando o Flask.

## Primeira calculadora
* Um número é dividido em 3 partes iguais.
* A primeira parte é dividida por 4 e seu resultado somado a 7. Após isso, o resultado é elevado ao quadrado e multiplicado por um valor de 0.257.
* A segunda parte é elevada a potência de 2.121, dividida por 5 e somado a 1.
* A terceira parte se mantém no mesmo valor.

Por fim, é somado esses 3 valores e entregado o resultado.

## Segunda calculadora
* N números são enviados.
* Todos esses N números são multiplicados por 11 e elevados a potência de 0.95.
* Por fim, é retirado o `desvio padrão` desses resultados e retornado o inverso desse valor (1/result)

Utilizando a lib NumPy para calcular o `desvio padrão`

## Terceira calculadora
* N números são colocados como entrada
* Caso a variância de todos esses números for menor que a multiplicação deles, é apresentado um informação de sucesso ao usuário.
* Caso contrário, é apresentado uma informação de falha.

Obs: Para o cálculo de variância, utilize o método "var" da lib NumPy.