## SkFuzzy 

A biblioteca scikit-fuzzy, ou skfuzzy, é uma biblioteca Python para processamento de lógica difusa e sistemas de controle difuso. Seu principal propósito é fornecer ferramentas para modelagem e simulação de sistemas baseados em lógica difusa, que é uma técnica de modelagem matemática usada para lidar com incerteza e imprecisão.
A lógica fuzzy, também conhecida como lógica difusa, é uma extensão da lógica clássica que permite lidar com a incerteza e a imprecisão de uma maneira mais flexível e realista. Enquanto na lógica clássica uma proposição é verdadeira ou falsa (valores binários), na lógica fuzzy, as proposições podem ter graus de verdade entre 0 e 1, representando assim a incerteza e a imprecisão presentes em muitos sistemas do mundo real.


Tutorial guia: 
1. Instalação:
Certifique-se de ter o Python instalado em seu sistema. Em seguida, instale a OpenCV usando o pip:
    ```
    pip install -U scikit-fuzzy
    ```
2. Importação: 
    ```
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    ```
3. Criando Conjutos fuzzy:
    ```
    # Variáveis de entrada
    qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
    servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

    # Variável de saída
    gorjeta = ctrl.Consequent(np.arange(0, 26, 1), 'gorjeta')
    ```
4. Definir as Funções de Pertinência:
    ```
    # Funções de pertinência para a qualidade
    qualidade['baixa'] = fuzz.trimf(qualidade.universe, [0, 0, 5])
    qualidade['media'] = fuzz.trimf(qualidade.universe, [0, 5, 10])
    qualidade['alta'] = fuzz.trimf(qualidade.universe, [5, 10, 10])

    # Funções de pertinência para o serviço
    servico['ruim'] = fuzz.trimf(servico.universe, [0, 0, 5])
    servico['aceitavel'] = fuzz.trimf(servico.universe, [0, 5, 10])
    servico['excelente'] = fuzz.trimf(servico.universe, [5, 10, 10])

    # Funções de pertinência para a gorjeta
    gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 13])
    gorjeta['media'] = fuzz.trimf(gorjeta.universe, [0, 13, 25])
    gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [13, 25, 25])
    ```
5. Criando Regras Fuzzy: 
    ```
    # Regras
    regra1 = ctrl.Rule(qualidade['baixa'] | servico['ruim'], gorjeta['baixa'])
    regra2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
    regra3 = ctrl.Rule(servico['excelente'] | qualidade['alta'], gorjeta['alta'])
    ```
6. Criando o Sistema de Controle 
    ```
    # Sistema de controle 
    sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
    sistema = ctrl.ControlSystemSimulation(sistema_controle)
    ```
7. Fazendo Inferência e Obtenção de Resultados
    ```
    # Entradas
    sistema.input['qualidade'] = 6.5
    sistema.input['servico'] = 9.8

    # Computando o resultado
    sistema.compute()

    # Obtendo o valor da gorjeta
    print(sistema.output['gorjeta'])
    ```
8. Visualizando as Funções de Pertinência (Opcional) 
Para visualizar voce tem que usar o matplotlib
    ```
    # Visualizando as funções de pertinência
    qualidade.view()
    servico.view()
    gorjeta.view()
    ```

Com este guia, você deve ter uma boa compreensão básica de como começar a usar a biblioteca scikit-fuzzy para lógica difusa e sistemas de controle difuso em Python. Experimente ajustar os conjuntos fuzzy, as regras e as entradas para ver como elas afetam a saída do sistema.

Deixarei um exemplo de lógica fuzzy disponível Skfuzzy_ex.py 