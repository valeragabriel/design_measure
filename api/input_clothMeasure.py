import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Solicitar no views.py 
# def get_tamanho_camiseta(blusa_PP, blusa_P, blusa_M, blusa_G, blusa_GG, busto_PP, busto_P, busto_M, busto_G, busto_GG, manga_PP, manga_P, manga_M, manga_G, manga_GG):
#     blusa_PP = int(input("Digite o valor do comprimento da camiseta no tamanho PP: "))
#     blusa_P = int(input("Digite o valor do comprimento da camiseta no tamanho P: "))
#     blusa_M = int(input("Digite o valor do comprimento da camiseta no tamanho M: "))
#     blusa_G = int(input("Digite o valor do comprimento da camiseta no tamanho G: "))
#     blusa_GG = int(input("Digite o valor do comprimento da camiseta no tamanho GG: "))

#     busto_PP = int(input("Digite o valor do comprimento do busto no tamanho PP: "))
#     busto_P = int(input("Digite o valor do comprimento do busto no tamanho P: "))
#     busto_M = int(input("Digite o valor do comprimento do busto no tamanho M: "))
#     busto_G = int(input("Digite o valor do comprimento do busto no tamanho G: "))
#     busto_GG = int(input("Digite o valor do comprimento do busto no tamanho GG: "))

#     manga_PP = int(input("Digite o valor do comprimento da manga no tamanho PP: "))
#     manga_P = int(input("Digite o valor do comprimento da manga no tamanho P: "))
#     manga_M = int(input("Digite o valor do comprimento da manga no tamanho M: "))
#     manga_G = int(input("Digite o valor do comprimento da manga no tamanho G: "))
#     manga_GG = int(input("Digite o valor do comprimento da manga no tamanho GG: "))
    
#     return blusa_PP, blusa_P, blusa_M, blusa_G, blusa_GG, busto_PP, busto_P, busto_M, busto_G, busto_GG, manga_PP, manga_P, manga_M, manga_G, manga_GG

# def modelagem_camiseta():
#     print("Modelagem da Camiseta")
#     print("1 - Justa")
#     print("2 - Normal")
#     print("3 - Larga")
#     modelagem = input("Digite o número correspondente da modelagem que prefere: ")

#     return modelagem

def camiseta(resultado_busto, resultado_manga, resultado_blusa, blusa_PP, blusa_P, blusa_M, blusa_G, blusa_GG, busto_PP, busto_P, busto_M, busto_G, busto_GG, manga_PP, manga_P, manga_M, manga_G, manga_GG, modelagem):
    comprimento_busto = ctrl.Antecedent(np.arange(busto_PP, busto_GG, 1), 'comprimento_busto')    
    comprimento_manga = ctrl.Antecedent(np.arange(manga_PP, manga_GG, 1), 'comprimento_manga')
    comprimento_blusa = ctrl.Antecedent(np.arange(blusa_PP, blusa_GG, 1), 'comprimento_blusa')

    comprimento_busto['PP'] = fuzz.trimf(comprimento_busto.universe, [busto_PP, busto_PP, busto_P])
    comprimento_busto['P'] = fuzz.trimf(comprimento_busto.universe, [busto_PP, busto_P, busto_M])
    comprimento_busto['M'] = fuzz.trimf(comprimento_busto.universe, [busto_P, busto_M, busto_G])
    comprimento_busto['G'] = fuzz.trimf(comprimento_busto.universe, [busto_M, busto_G, busto_GG])
    comprimento_busto['GG'] = fuzz.trimf(comprimento_busto.universe, [busto_G, busto_GG, busto_GG])

    comprimento_blusa['PP'] = fuzz.trimf(comprimento_blusa.universe, [blusa_PP, blusa_PP, blusa_P])
    comprimento_blusa['P'] = fuzz.trimf(comprimento_blusa.universe, [blusa_PP, blusa_P, blusa_M])
    comprimento_blusa['M'] = fuzz.trimf(comprimento_blusa.universe, [blusa_P, blusa_M, blusa_G])
    comprimento_blusa['G'] = fuzz.trimf(comprimento_blusa.universe, [blusa_M, blusa_G, blusa_GG])
    comprimento_blusa['GG'] = fuzz.trimf(comprimento_blusa.universe, [blusa_G, blusa_GG, blusa_GG])

    comprimento_manga['PP'] = fuzz.trimf(comprimento_manga.universe, [manga_PP, manga_PP, manga_P])
    comprimento_manga['P'] = fuzz.trimf(comprimento_manga.universe, [manga_PP, manga_P, manga_M])
    comprimento_manga['M'] = fuzz.trimf(comprimento_manga.universe, [manga_P, manga_M, manga_G])
    comprimento_manga['G'] = fuzz.trimf(comprimento_manga.universe, [manga_M, manga_G, manga_GG])
    comprimento_manga['GG'] = fuzz.trimf(comprimento_manga.universe, [manga_G, manga_GG, manga_GG])

    tamanho_camiseta = ctrl.Consequent(np.arange(0, 101, 1), 'tamanho_camiseta')
   
    if modelagem == '1':
        tamanho_camiseta.defuzzify_method = 'som' # baixa min das max
    elif modelagem == '2':
        tamanho_camiseta.defuzzify_method = 'mom' # regular media
    elif modelagem == '3':
        tamanho_camiseta.defuzzify_method = 'lom' # alta max das max
    
    tamanho_camiseta['PP'] = fuzz.trimf(tamanho_camiseta.universe, [0, 0, 20])
    tamanho_camiseta['P'] = fuzz.trimf(tamanho_camiseta.universe, [0, 20, 40])
    tamanho_camiseta['M'] = fuzz.trimf(tamanho_camiseta.universe, [20, 40, 60])
    tamanho_camiseta['G'] = fuzz.trimf(tamanho_camiseta.universe, [40, 60, 80])
    tamanho_camiseta['GG'] = fuzz.trimf(tamanho_camiseta.universe, [60, 80, 100])

    regras = [
    ctrl.Rule(comprimento_busto['PP'] | comprimento_blusa['PP'], tamanho_camiseta['PP']),
    ctrl.Rule(comprimento_busto['P'] | comprimento_blusa['P'], tamanho_camiseta['P']),
    ctrl.Rule(comprimento_busto['M'] | comprimento_blusa['M'], tamanho_camiseta['M']),
    ctrl.Rule(comprimento_busto['G'] | comprimento_blusa['G'], tamanho_camiseta['G']),
    ctrl.Rule(comprimento_busto['GG'] | comprimento_blusa['GG'], tamanho_camiseta['GG']),

    ctrl.Rule(comprimento_busto['PP'] & comprimento_manga['PP'] & comprimento_blusa['PP'], tamanho_camiseta['PP']),
    ctrl.Rule(comprimento_busto['P'] & comprimento_manga['P'] & comprimento_blusa['P'], tamanho_camiseta['P']),
    ctrl.Rule(comprimento_busto['M'] & comprimento_manga['M'] & comprimento_blusa['M'], tamanho_camiseta['M']),
    ctrl.Rule(comprimento_busto['G'] & comprimento_manga['G'] & comprimento_blusa['G'], tamanho_camiseta['G']),
    ctrl.Rule(comprimento_busto['GG'] & comprimento_manga['GG'] & comprimento_blusa['GG'], tamanho_camiseta['GG']),

    ctrl.Rule(comprimento_busto['M'] & comprimento_manga['PP'] & comprimento_blusa['M'], tamanho_camiseta['M']),
    ctrl.Rule(comprimento_busto['M'] & comprimento_manga['P'] & comprimento_blusa['M'], tamanho_camiseta['M']),
    ctrl.Rule(comprimento_busto['M'] & comprimento_manga['G'] & comprimento_blusa['M'], tamanho_camiseta['M']),

    ctrl.Rule(comprimento_busto['GG'] & comprimento_manga['M'] & comprimento_blusa['GG'], tamanho_camiseta['GG']),
    ctrl.Rule(comprimento_busto['GG'] & comprimento_manga['G'] & comprimento_blusa['GG'], tamanho_camiseta['GG']),
    ctrl.Rule(comprimento_busto['GG'] & comprimento_manga['GG'] & comprimento_blusa['GG'], tamanho_camiseta['GG'])
]

    sistema_controle = ctrl.ControlSystem(regras)
    tamanho_roupas = ctrl.ControlSystemSimulation(sistema_controle)
    
    tamanho_roupas.input['comprimento_busto'] = resultado_busto
    tamanho_roupas.input['comprimento_manga'] = resultado_manga
    tamanho_roupas.input['comprimento_blusa'] = resultado_blusa

    tamanho_roupas.compute()

    tamanho = tamanho_roupas.output['tamanho_camiseta']

    def get_tamanho_camiseta(valor):
        if valor <= 20:
            return 'PP'
        elif valor <= 40:
            return 'P'
        elif valor <= 60:
            return 'M'
        elif valor <= 80:
            return 'G'
        else:
            return 'GG'

    tamanho_camiseta_final = get_tamanho_camiseta(tamanho)
    return tamanho_camiseta_final
    
# Vou deixar pre-definido os valores das medidas corporais pois nao vou disponibilizar o códgio de extracão de medidas corporais 
def main(blusa_PP, blusa_P, blusa_M, blusa_G, blusa_GG, busto_PP, busto_P, busto_M, busto_G, busto_GG, manga_PP, manga_P, manga_M, manga_G, manga_GG, modelagem):
    resultado_busto = 60
    resultado_manga = 26
    resultado_blusa = 77


    tamanho_camiseta = camiseta(resultado_busto, resultado_manga, resultado_blusa, blusa_PP, blusa_P, blusa_M, blusa_G, blusa_GG, busto_PP, busto_P, busto_M, busto_G, busto_GG, manga_PP, manga_P, manga_M, manga_G, manga_GG, modelagem)
    return {'camiseta': tamanho_camiseta}