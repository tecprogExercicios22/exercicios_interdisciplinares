###Exercício 12
__A distância entre várias cidades é dada pela tabela abaixo (em km):

```text
       1    2    3    4    5
    -------------------------
  1 | 00   15   30   05   12
  2 | 15   00   10   17   28
  3 | 30   10   00   03   11
  4 | 05   17   03   00   80
  5 | 12   28   11   80   00
```

Implemente um programa que:
*   leia a tabela acima em um *array* bidimensional. O programa não deve perguntar distâncias já informadas (por exemplo, se o usuário já forneceu a distância entre 1 e 3 não é necessário informar a distância entre 3 e 1, que é a mesma) e também não deve perguntar a distância de uma cidade para ela mesma, que é 0.
*   leia um percurso fornecido pelo usuário em um *array* unidimensional. Calcule e mostre a distância percorrida. Por exemplo: dado o percurso 1, 2, 3, 2, 5, 1, 4, para a tabela mostrada como exemplo teremos: $15 + 10 + 10 + 28 + 12 + 5 = 80\text{ km}$.__
