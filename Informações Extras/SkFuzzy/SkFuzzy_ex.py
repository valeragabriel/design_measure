import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperatura = ctrl.Antecedent(np.arange(-20, 51, 1), 'temperatura')
umidade_ar = ctrl.Antecedent(np.arange(0, 101, 1), 'umidade_ar')
umidade_solo = ctrl.Antecedent(np.arange(0, 101, 1), 'umidade_solo')
nivel_agua = ctrl.Antecedent(np.arange(0, 101, 1), 'nivel_agua')
sistema = ctrl.Consequent(np.arange(12, 36, 1), 'sistema')

sistema.defuzzify_method = 'centroid'

temperatura['muito baixa'] = fuzz.trapmf(temperatura.universe, [-20, -20, -5, 0])
temperatura['baixa'] = fuzz.trimf(temperatura.universe, [-5,10,18])
temperatura['média'] = fuzz.trapmf(temperatura.universe, [15,20,25,28])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [25,28,39])
temperatura['muito alta'] = fuzz.trapmf(temperatura.universe, [39,45,50,50])

umidade_ar['baixa'] = fuzz.trimf(umidade_ar.universe, [0, 0, 30])
umidade_ar['média'] = fuzz.trapmf(umidade_ar.universe, [25, 50, 80, 100])
umidade_ar['alta'] = fuzz.trimf(umidade_ar.universe, [80, 100, 100])

umidade_solo['baixa'] = fuzz.trimf(umidade_solo.universe, [0, 0, 30])
umidade_solo['média'] = fuzz.trapmf(umidade_solo.universe, [25, 50, 80, 100])
umidade_solo['alta'] = fuzz.trimf(umidade_solo.universe, [80, 100, 100])

nivel_agua['baixa'] = fuzz.trapmf(nivel_agua.universe, [0, 0, 30, 40])
nivel_agua['regular'] = fuzz.trimf(nivel_agua.universe, [28, 50, 72])
nivel_agua['alta'] = fuzz.trapmf(nivel_agua.universe, [60, 80, 100, 100])

sistema['resfriar2'] = fuzz.trimf(sistema.universe, [12, 12, 17])
sistema['resfriar1'] = fuzz.trimf(sistema.universe, [15, 18, 20])
sistema['desligar'] = fuzz.trimf(sistema.universe, [19, 22, 25])
sistema['aquecer1'] = fuzz.trimf(sistema.universe, [22, 25, 27])
sistema['aquecer2'] = fuzz.trapmf(sistema.universe, [25, 30, 35, 35])

temperatura.view()
umidade_ar.view()
umidade_solo.view()
nivel_agua.view()
sistema.view()

#Regras podem ser criadas conforme o plantio, pode ser especificada e modificadas conforme a necessidade
rule1 = ctrl.Rule(temperatura['muito baixa'], sistema['aquecer2'])
rule2 = ctrl.Rule(temperatura['muito alta'] | (temperatura['alta'] & umidade_ar['alta']), sistema['resfriar2'])
rule3 = ctrl.Rule((temperatura['média'] & umidade_ar['média']) | umidade_ar['baixa'], sistema['desligar'])
rule4 = ctrl.Rule(temperatura['baixa'] & (umidade_ar['média'] | umidade_ar['alta']), sistema['aquecer1'])
rule5 = ctrl.Rule(temperatura['alta'], sistema['resfriar1'])
rule6 = ctrl.Rule(umidade_solo['baixa'], sistema['resfriar2'])
rule7 = ctrl.Rule(nivel_agua['baixa'], sistema['resfriar2'])
rule8 = ctrl.Rule(nivel_agua['alta'], sistema['aquecer1'])
rule9 = ctrl.Rule((temperatura['média'] & umidade_solo['alta']) | (temperatura['baixa'] & umidade_solo['média']), sistema['desligar'])
rule10 = ctrl.Rule((temperatura['alta'] & nivel_agua['baixa']) | (temperatura['muito alta'] & nivel_agua['baixa']), sistema['resfriar1'])
rule11 = ctrl.Rule((umidade_ar['alta'] & umidade_solo['baixa']) | (umidade_ar['baixa'] & umidade_solo['média']), sistema['aquecer2'])

simulador_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11])
simulador = ctrl.ControlSystemSimulation(simulador_ctrl)

# Valores de entrada, simulação, caso voce queira testar com outros valores, basta alterar os valores abaixo
# Ou caso voce realmente queira utilizar para sua estufa, basta colocar esses valores os resultados captados pelos sensores 
VALOR_TEMPERATURA = 10
VALOR_UMIDADE_AR = 20
VALOR_UMIDADE_SOLO = 20
VALOR_NIVEL_AGUA = 50

simulador.input['temperatura'] = VALOR_TEMPERATURA
simulador.input['umidade_ar'] = VALOR_UMIDADE_AR
simulador.input['umidade_solo'] = VALOR_UMIDADE_SOLO
simulador.input['nivel_agua'] = VALOR_NIVEL_AGUA

simulador.compute()

# Obtenha o resultado
RESULTADO = simulador.output['sistema']
print("Resultado numérico: ", RESULTADO)

# Visualização do resultado
temperatura.view(sim=simulador)
umidade_ar.view(sim=simulador)
umidade_solo.view(sim=simulador)
nivel_agua.view(sim=simulador)
sistema.view(sim=simulador)

