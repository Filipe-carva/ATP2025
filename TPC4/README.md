# TPC4 – Aplicação de Gestão de Salas de Cinema em Python

## Autor
- **Nome:** Filipe Carvalho  
- **ID:** A111961  
- **Foto:**  
  ![Foto do autor](foto.jpg)

## Resumo
Neste trabalho (TPC4) desenvolvi uma aplicação em Python para a **gestão de um conjunto de salas de cinema** de um centro comercial.  

Cada sala tem um número total de lugares, uma lista com os bilhetes vendidos (lugares ocupados) e o nome do filme que está a ser exibido. O conjunto das salas forma o cinema.  

O programa permite realizar várias operações através de um menu interativo, como:  
- Inserir novas salas no cinema;  
- Listar todos os filmes em exibição;  
- Verificar se um determinado lugar está disponível para um certo filme;  
- Vender bilhetes (marcar lugares como ocupados);  
- Listar as disponibilidades de cada sala (quantos lugares ainda estão livres).  

As principais funções implementadas foram:  
- `listar(cinema)` – lista todos os filmes que estão em exibição;  
- `disponivel(cinema, filme, lugar)` – verifica se um lugar está livre;  
- `vendebilhete(cinema, filme, lugar)` – regista a venda de um bilhete;  
- `listardisponibilidades(cinema)` – mostra, para cada sala, o filme e o número de lugares disponíveis;  
- `inserirSala(cinema, sala)` – adiciona uma nova sala ao cinema (verificando se já existe).  

Durante o desenvolvimento aprendi a trabalhar melhor com **estruturas de dados compostas (listas de tuplos)**, a criar e manipular funções que alteram o estado interno de um programa e a construir uma aplicação com **menu interativo**, que junta várias funcionalidades num só programa.  

Este exercício ajudou-me a consolidar a noção de modelação de dados e a perceber como organizar a informação de forma estruturada para representar situações do mundo real.

## Resultados
- [Resolução da Aplicação de Gestão de Cinema]- Ficheiro Cinema.py

