import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Posso fazer com que o  usuario insira os valores de tamanhos da roupas, entretanto 
# para facilitar a visualização e testes, inseri valores fixos para os tamanhos das roupas com base 
# em uma tabela de medidas de roupas masculinas de uma loja online 
# estou pensando em colocar uma deep learning para aprender o tamanho das roupas com base nas medidas do usuário
# entretanto esse algoritmo é apenas para testes e não será utilizado no projeto final 
def camiseta(resultado_busto, resultado_manga, resultado_blusa):
    comprimento_busto = ctrl.Antecedent(np.arange(46, 61, 1), 'comprimento_busto')    
    comprimento_manga = ctrl.Antecedent(np.arange(20, 25, 1), 'comprimento_manga')
    comprimento_blusa = ctrl.Antecedent(np.arange(73, 81, 1), 'comprimento_blusa')

    comprimento_busto['PP'] = fuzz.trimf(comprimento_busto.universe, [46, 46, 53])
    comprimento_busto['P'] = fuzz.trimf(comprimento_busto.universe, [46, 53, 59])
    comprimento_busto['M'] = fuzz.trimf(comprimento_busto.universe, [53, 59, 61])
    comprimento_busto['G'] = fuzz.trimf(comprimento_busto.universe, [59, 61, 61])
    comprimento_busto['GG'] = fuzz.trimf(comprimento_busto.universe, [59, 61, 61])

    comprimento_blusa['PP'] = fuzz.trimf(comprimento_blusa.universe, [73, 73, 75])
    comprimento_blusa['P'] = fuzz.trimf(comprimento_blusa.universe, [73, 75, 77])
    comprimento_blusa['M'] = fuzz.trimf(comprimento_blusa.universe, [75, 77, 79])
    comprimento_blusa['G'] = fuzz.trimf(comprimento_blusa.universe, [77, 79, 81])
    comprimento_blusa['GG'] = fuzz.trimf(comprimento_blusa.universe, [79, 81, 81])

    comprimento_manga['PP'] = fuzz.trimf(comprimento_manga.universe, [20, 20, 22])
    comprimento_manga['P'] = fuzz.trimf(comprimento_manga.universe, [20, 20, 22])
    comprimento_manga['M'] = fuzz.trimf(comprimento_manga.universe, [20, 22, 25])
    comprimento_manga['G'] = fuzz.trimf(comprimento_manga.universe, [22, 25, 25])
    comprimento_manga['GG'] = fuzz.trimf(comprimento_manga.universe, [22, 25, 25])

    tamanho_camiseta = ctrl.Consequent(np.arange(0, 101, 1), 'tamanho_camiseta')
    tamanho_camiseta.defuzzify_method = 'centroid'

    tamanho_camiseta['PP'] = fuzz.trimf(tamanho_camiseta.universe, [0, 0, 20])
    tamanho_camiseta['P'] = fuzz.trimf(tamanho_camiseta.universe, [0, 20, 40])
    tamanho_camiseta['M'] = fuzz.trimf(tamanho_camiseta.universe, [20, 40, 60])
    tamanho_camiseta['G'] = fuzz.trimf(tamanho_camiseta.universe, [40, 60, 80])
    tamanho_camiseta['GG'] = fuzz.trimf(tamanho_camiseta.universe, [60, 80, 100])

    #preciso definir outras regras, defini apenas padrão para testar
    regras = [
        ctrl.Rule(comprimento_busto['PP'] & comprimento_manga['PP'], tamanho_camiseta['PP']),
        ctrl.Rule(comprimento_busto['P'] & comprimento_manga['P'], tamanho_camiseta['P']),
        ctrl.Rule(comprimento_busto['M'] & comprimento_manga['M'], tamanho_camiseta['M']),
        ctrl.Rule(comprimento_busto['G'] & comprimento_manga['G'], tamanho_camiseta['G']),
        ctrl.Rule(comprimento_busto['GG'] & comprimento_manga['GG'], tamanho_camiseta['GG']),
        ctrl.Rule(comprimento_blusa['PP'] & comprimento_manga['PP'], tamanho_camiseta['PP']),
        ctrl.Rule(comprimento_blusa['P'] & comprimento_manga['P'], tamanho_camiseta['P']),
        ctrl.Rule(comprimento_blusa['M'] & comprimento_manga['M'], tamanho_camiseta['M']),
        ctrl.Rule(comprimento_blusa['G'] & comprimento_manga['G'], tamanho_camiseta['G']),
        ctrl.Rule(comprimento_blusa['GG'] & comprimento_manga['GG'], tamanho_camiseta['GG'])
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
    # Métodos de desfuzzificação, buscar sobre 
    tamanho_camiseta_final = get_tamanho_camiseta(tamanho)

    return tamanho_camiseta_final

def camisa(resultado_busto, resultado_mangaL, resultado_blusa):
    comprimento_busto = ctrl.Antecedent(np.arange(46, 61, 1), 'comprimento_busto')    
    comprimento_mangaL = ctrl.Antecedent(np.arange(20, 25, 1), 'comprimento_mangaL')
    comprimento_blusa = ctrl.Antecedent(np.arange(73, 81, 1), 'comprimento_blusa')

    comprimento_busto['PP'] = fuzz.trimf(comprimento_busto.universe, [46, 46, 53])
    comprimento_busto['P'] = fuzz.trimf(comprimento_busto.universe, [46, 53, 59])
    comprimento_busto['M'] = fuzz.trimf(comprimento_busto.universe, [53, 59, 61])
    comprimento_busto['G'] = fuzz.trimf(comprimento_busto.universe, [59, 61, 61])
    comprimento_busto['GG'] = fuzz.trimf(comprimento_busto.universe, [59, 61, 61])

    comprimento_blusa['PP'] = fuzz.trimf(comprimento_blusa.universe, [73, 73, 75])
    comprimento_blusa['P'] = fuzz.trimf(comprimento_blusa.universe, [73, 75, 77])
    comprimento_blusa['M'] = fuzz.trimf(comprimento_blusa.universe, [75, 77, 79])
    comprimento_blusa['G'] = fuzz.trimf(comprimento_blusa.universe, [77, 79, 81])
    comprimento_blusa['GG'] = fuzz.trimf(comprimento_blusa.universe, [79, 81, 81])

    comprimento_mangaL['PP'] = fuzz.trimf(comprimento_mangaL.universe, [20, 20, 22])
    comprimento_mangaL['P'] = fuzz.trimf(comprimento_mangaL.universe, [20, 20, 22])
    comprimento_mangaL['M'] = fuzz.trimf(comprimento_mangaL.universe, [20, 22, 25])
    comprimento_mangaL['G'] = fuzz.trimf(comprimento_mangaL.universe, [22, 25, 25])
    comprimento_mangaL['GG'] = fuzz.trimf(comprimento_mangaL.universe, [22, 25, 25])


    tamanho_camisa = ctrl.Consequent(np.arange(0, 101, 1), 'tamanho_camisa')
    tamanho_camisa.defuzzify_method = 'centroid'

    tamanho_camisa['PP'] = fuzz.trimf(tamanho_camisa.universe, [0, 0, 20])
    tamanho_camisa['P'] = fuzz.trimf(tamanho_camisa.universe, [0, 20, 40])
    tamanho_camisa['M'] = fuzz.trimf(tamanho_camisa.universe, [20, 40, 60])
    tamanho_camisa['G'] = fuzz.trimf(tamanho_camisa.universe, [40, 60, 80])
    tamanho_camisa['GG'] = fuzz.trimf(tamanho_camisa.universe, [60, 80, 100])

    #preciso definir outras regras, defini apenas padrão para testar
    regras = [
        ctrl.Rule(comprimento_busto['PP'] & comprimento_mangaL['PP'], tamanho_camisa['PP']),
        ctrl.Rule(comprimento_busto['P'] & comprimento_mangaL['P'], tamanho_camisa['P']),
        ctrl.Rule(comprimento_busto['M'] & comprimento_mangaL['M'], tamanho_camisa['M']),
        ctrl.Rule(comprimento_busto['G'] & comprimento_mangaL['G'], tamanho_camisa['G']),
        ctrl.Rule(comprimento_busto['GG'] & comprimento_mangaL['GG'], tamanho_camisa['GG']),
        ctrl.Rule(comprimento_blusa['PP'] & comprimento_mangaL['PP'], tamanho_camisa['PP']),
        ctrl.Rule(comprimento_blusa['P'] & comprimento_mangaL['P'], tamanho_camisa['P']),
        ctrl.Rule(comprimento_blusa['M'] & comprimento_mangaL['M'], tamanho_camisa['M']),
        ctrl.Rule(comprimento_blusa['G'] & comprimento_mangaL['G'], tamanho_camisa['G']),
        ctrl.Rule(comprimento_blusa['GG'] & comprimento_mangaL['GG'], tamanho_camisa['GG'])
    ]

    sistema_controle = ctrl.ControlSystem(regras)
    tamanho_roupas = ctrl.ControlSystemSimulation(sistema_controle)
    
    tamanho_roupas.input['comprimento_busto'] = resultado_busto
    tamanho_roupas.input['comprimento_mangaL'] = resultado_mangaL
    tamanho_roupas.input['comprimento_blusa'] = resultado_blusa

    tamanho_roupas.compute()

    tamanho = tamanho_roupas.output['tamanho_camisa']


    def get_tamanho_camisa(valor):
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

    tamanho_camisa_final = get_tamanho_camisa(tamanho)


    return tamanho_camisa_final

def calca(resultado_perna, resultado_quadril):
    comprimento_perna = ctrl.Antecedent(np.arange(70, 91, 1), 'comprimento_perna')    
    comprimento_quadril = ctrl.Antecedent(np.arange(90, 111, 1), 'comprimento_quadril')

    comprimento_perna['38'] = fuzz.trimf(comprimento_perna.universe, [70, 70, 75])
    comprimento_perna['40'] = fuzz.trimf(comprimento_perna.universe, [70, 75, 80])
    comprimento_perna['42'] = fuzz.trimf(comprimento_perna.universe, [75, 80, 85])
    comprimento_perna['44'] = fuzz.trimf(comprimento_perna.universe, [80, 85, 90])
    comprimento_perna['46'] = fuzz.trimf(comprimento_perna.universe, [85, 90, 91])

    comprimento_quadril['38'] = fuzz.trimf(comprimento_quadril.universe, [90, 90, 95])
    comprimento_quadril['40'] = fuzz.trimf(comprimento_quadril.universe, [90, 95, 100])
    comprimento_quadril['42'] = fuzz.trimf(comprimento_quadril.universe, [95, 100, 105])
    comprimento_quadril['44'] = fuzz.trimf(comprimento_quadril.universe, [100, 105, 110])
    comprimento_quadril['46'] = fuzz.trimf(comprimento_quadril.universe, [105, 110, 111])

    tamanho_calca = ctrl.Consequent(np.arange(38, 47, 1), 'tamanho_calca')
    tamanho_calca.defuzzify_method = 'centroid'

    tamanho_calca['38'] = fuzz.trimf(tamanho_calca.universe, [38, 38, 40])
    tamanho_calca['40'] = fuzz.trimf(tamanho_calca.universe, [38, 40, 42])
    tamanho_calca['42'] = fuzz.trimf(tamanho_calca.universe, [40, 42, 44])
    tamanho_calca['44'] = fuzz.trimf(tamanho_calca.universe, [42, 44, 46])
    tamanho_calca['46'] = fuzz.trimf(tamanho_calca.universe, [44, 46, 47])

    #preciso definir outras regras, defini apenas padrão para testar   
    regras = [
        ctrl.Rule(comprimento_perna['38'] & comprimento_quadril['38'], tamanho_calca['38']),
        ctrl.Rule(comprimento_perna['40'] & comprimento_quadril['40'], tamanho_calca['40']),
        ctrl.Rule(comprimento_perna['42'] & comprimento_quadril['42'], tamanho_calca['42']),
        ctrl.Rule(comprimento_perna['44'] & comprimento_quadril['44'], tamanho_calca['44']),
        ctrl.Rule(comprimento_perna['46'] & comprimento_quadril['46'], tamanho_calca['46'])
    ]

    sistema_controle = ctrl.ControlSystem(regras)
    tamanho_calca_simulacao = ctrl.ControlSystemSimulation(sistema_controle)
    
    tamanho_calca_simulacao.input['comprimento_perna'] = resultado_perna
    tamanho_calca_simulacao.input['comprimento_quadril'] = resultado_quadril

    tamanho_calca_simulacao.compute()

    tamanho = tamanho_calca_simulacao.output['tamanho_calca']

    return tamanho

def bermuda(resultado_quadril_joelho, resultado_quadril):
    comprimento_quadril_joelho = ctrl.Antecedent(np.arange(44, 51, 1), 'comprimento_quadril_joelho')    
    comprimento_quadril = ctrl.Antecedent(np.arange(90, 111, 1), 'comprimento_quadril')

    comprimento_quadril_joelho['38'] = fuzz.trimf(comprimento_quadril_joelho.universe, [44, 44, 46])
    comprimento_quadril_joelho['40'] = fuzz.trimf(comprimento_quadril_joelho.universe, [44, 46, 48])
    comprimento_quadril_joelho['42'] = fuzz.trimf(comprimento_quadril_joelho.universe, [46, 48, 50])
    comprimento_quadril_joelho['44'] = fuzz.trimf(comprimento_quadril_joelho.universe, [48, 50, 51])
    comprimento_quadril_joelho['46'] = fuzz.trimf(comprimento_quadril_joelho.universe, [50, 51, 51])

    comprimento_quadril['38'] = fuzz.trimf(comprimento_quadril.universe, [90, 90, 95])
    comprimento_quadril['40'] = fuzz.trimf(comprimento_quadril.universe, [90, 95, 100])
    comprimento_quadril['42'] = fuzz.trimf(comprimento_quadril.universe, [95, 100, 105])
    comprimento_quadril['44'] = fuzz.trimf(comprimento_quadril.universe, [100, 105, 110])
    comprimento_quadril['46'] = fuzz.trimf(comprimento_quadril.universe, [105, 110, 111])

    tamanho_bermuda = ctrl.Consequent(np.arange(38, 47, 1), 'tamanho_bermuda')
    tamanho_bermuda.defuzzify_method = 'centroid'

    tamanho_bermuda['38'] = fuzz.trimf(tamanho_bermuda.universe, [38, 38, 40])
    tamanho_bermuda['40'] = fuzz.trimf(tamanho_bermuda.universe, [38, 40, 42])
    tamanho_bermuda['42'] = fuzz.trimf(tamanho_bermuda.universe, [40, 42, 44])
    tamanho_bermuda['44'] = fuzz.trimf(tamanho_bermuda.universe, [42, 44, 46])
    tamanho_bermuda['46'] = fuzz.trimf(tamanho_bermuda.universe, [44, 46, 47])
    
    #preciso definir outras regras, defini apenas padrão para testar
    regras = [
        ctrl.Rule(comprimento_quadril_joelho['38'] & comprimento_quadril['38'], tamanho_bermuda['38']),
        ctrl.Rule(comprimento_quadril_joelho['40'] & comprimento_quadril['40'], tamanho_bermuda['40']),
        ctrl.Rule(comprimento_quadril_joelho['42'] & comprimento_quadril['42'], tamanho_bermuda['42']),
        ctrl.Rule(comprimento_quadril_joelho['44'] & comprimento_quadril['44'], tamanho_bermuda['44']),
        ctrl.Rule(comprimento_quadril_joelho['46'] & comprimento_quadril['46'], tamanho_bermuda['46'])
    ]

    sistema_controle = ctrl.ControlSystem(regras)
    tamanho_bermuda_simulacao = ctrl.ControlSystemSimulation(sistema_controle)
    
    tamanho_bermuda_simulacao.input['comprimento_quadril_joelho'] = resultado_quadril_joelho
    tamanho_bermuda_simulacao.input['comprimento_quadril'] = resultado_quadril

    tamanho_bermuda_simulacao.compute()

    tamanho = tamanho_bermuda_simulacao.output['tamanho_bermuda']

    return tamanho

def run(forearm, arm, waist_shoulder, leg, bust, waist_knee, waist):
    resultado_busto = bust
    resultado_manga = forearm
    resultado_mangaL = arm
    resultado_blusa = waist_shoulder
    resultado_quadril = waist
    resultado_perna = leg
    resultado_quadril_joelho = waist_knee

    
    tamanho_camiseta = camiseta(resultado_busto, resultado_manga, resultado_blusa)
    tamanho_camisa = camisa(resultado_busto, resultado_mangaL, resultado_blusa)
    tamanho_calca = calca(resultado_perna, resultado_quadril)
    tamanho_bermuda = bermuda(resultado_quadril_joelho, resultado_quadril)

    return {'camiseta': tamanho_camiseta, 'camisa': tamanho_camisa, 'calca': tamanho_calca, 'bermuda': tamanho_bermuda}

