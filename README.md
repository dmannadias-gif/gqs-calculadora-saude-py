# gqs-calculadora-saude-py

## Descrição do Projeto

Sistema de linha de comando em Python para cálculos básicos de saúde e bem-estar: cálculo de IMC (com classificação), recomendação de consumo diário de água e estimativa de frequência cardíaca máxima. O código original continha erros de lógica matemática e de fluxo de execução, corrigidos como parte do exercício de Garantia da Qualidade de Software (GQS).

## Relatório de Bugs Encontrados

| # | Local do Bug (função/linha) | Comportamento Incorreto Observado | Solução Aplicada |
|---|---|---|---|
| 1 | `calcular_imc` | IMC calculado como `peso / (altura * 2)`, uma multiplicação em vez da potenciação correta, gerando resultado matematicamente errado | Alterado para `peso / (altura ** 2)` |
| 2 | `classificar_imc` | Comparações com `>` deixavam valores exatos (18.5, 25.0, entre 24.9 e 25.0) sem nenhuma faixa correspondente, retornando `None` silenciosamente | Reescrito com `<` / `<=` em cadeia contínua, cobrindo todos os valores possíveis |
| 3 | `calcular_agua_diaria` | Fórmula dividia o peso por 35 em vez de multiplicar por 0.035 (35ml/kg), gerando valores muito abaixo do recomendado | Alterado para `peso * 0.035` |
| 4 | `calcular_frequencia_cardiaca_maxima` | Fórmula somava a idade a 220 em vez de subtrair, gerando FC máxima acima do fisiologicamente esperado | Alterado para `220 - idade` |
| 5 | `menu()` | `input()` retorna string, mas o valor não era convertido para número | Conversão para `int()` feita dentro do próprio `menu()`, com tratamento de exceção para entradas não numéricas |
| 6 | `main()` | Comparações `if opcao == 1` (int) nunca eram verdadeiras porque `opcao` era string, fazendo o programa sempre cair no `else` | Corrigido automaticamente ao resolver o Bug 5 (opção já chega como int) |
| 7 | `main()`, opção 4 | Faltava `break` após exibir a mensagem de encerramento, mantendo o `while True` rodando indefinidamente | Adicionado `break` para encerrar o loop corretamente |

## Como Executar

Pré-requisito: Python 3 instalado.

```bash
python3 calculadora_saude.py
```

Ou, dependendo da instalação:

```bash
python calculadora_saude.py
```

Siga o menu interativo exibido no terminal e escolha uma opção de 1 a 4.
