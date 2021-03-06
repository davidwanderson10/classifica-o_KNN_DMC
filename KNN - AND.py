import random
import math
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

def cria_matriz(n_linhas, n_colunas, valor):
        matriz = []
        for l in range(n_linhas):
            linha = []
            for c in range(n_colunas):
                linha.append(valor)
            
            matriz.append(linha)
        return matriz


vet_atr_ini=[[5.1,3.5,1.4,0.2, 1],
        [4.9,3.0,1.4,0.2, 1],
        [4.7,3.2,1.3,0.2, 1],
        [4.6,3.1,1.5,0.2, 1],
        [5.0,3.6,1.4,0.2, 1],
        [5.4,3.9,1.7,0.4, 1],
        [4.6,3.4,1.4,0.3, 1],
        [5.0,3.4,1.5,0.2, 1],
        [4.4,2.9,1.4,0.2, 1],
        [4.9,3.1,1.5,0.1, 1],
        [5.4,3.7,1.5,0.2, 1],
        [4.8,3.4,1.6,0.2, 1],
        [4.8,3.0,1.4,0.1, 1],
        [4.3,3.0,1.1,0.1, 1],
        [5.8,4.0,1.2,0.2, 1],
        [5.7,4.4,1.5,0.4, 1],
        [5.4,3.9,1.3,0.4, 1],
        [5.1,3.5,1.4,0.3, 1],
        [5.7,3.8,1.7,0.3, 1],
        [5.1,3.8,1.5,0.3, 1],
        [5.4,3.4,1.7,0.2, 1],
        [5.1,3.7,1.5,0.4, 1],
        [4.6,3.6,1.0,0.2, 1],
        [5.1,3.3,1.7,0.5, 1],
        [4.8,3.4,1.9,0.2, 1],
        [5.0,3.0,1.6,0.2, 1],
        [5.0,3.4,1.6,0.4, 1],
        [5.2,3.5,1.5,0.2, 1],
        [5.2,3.4,1.4,0.2, 1],
        [4.7,3.2,1.6,0.2, 1],
        [4.8,3.1,1.6,0.2, 1],
        [5.4,3.4,1.5,0.4, 1],
        [5.2,4.1,1.5,0.1, 1],
        [5.5,4.2,1.4,0.2, 1],
        [4.9,3.1,1.5,0.1, 1],
        [5.0,3.2,1.2,0.2, 1],
        [5.5,3.5,1.3,0.2, 1],
        [4.9,3.1,1.5,0.1, 1],
        [4.4,3.0,1.3,0.2, 1],
        [5.1,3.4,1.5,0.2, 1],
        [5.0,3.5,1.3,0.3, 1],
        [4.5,2.3,1.3,0.3, 1],
        [4.4,3.2,1.3,0.2, 1],
        [5.0,3.5,1.6,0.6, 1],
        [5.1,3.8,1.9,0.4, 1],
        [4.8,3.0,1.4,0.3, 1],
        [5.1,3.8,1.6,0.2, 1],
        [4.6,3.2,1.4,0.2, 1],
        [5.3,3.7,1.5,0.2, 1],
        [5.0,3.3,1.4,0.2, 1],
        [7.0,3.2,4.7,1.4, 2],
        [6.4,3.2,4.5,1.5, 2],
        [6.9,3.1,4.9,1.5, 2],
        [5.5,2.3,4.0,1.3, 2],
        [6.5,2.8,4.6,1.5, 2],
        [5.7,2.8,4.5,1.3, 2],
        [6.3,3.3,4.7,1.6, 2],
        [4.9,2.4,3.3,1.0, 2],
        [6.6,2.9,4.6,1.3, 2],
        [5.2,2.7,3.9,1.4, 2],
        [5.0,2.0,3.5,1.0, 2],
        [5.9,3.0,4.2,1.5, 2],
        [6.0,2.2,4.0,1.0, 2],
        [6.1,2.9,4.7,1.4, 2],
        [5.6,2.9,3.6,1.3, 2],
        [6.7,3.1,4.4,1.4, 2],
        [5.6,3.0,4.5,1.5, 2],
        [5.8,2.7,4.1,1.0, 2],
        [6.2,2.2,4.5,1.5, 2],
        [5.6,2.5,3.9,1.1, 2],
        [5.9,3.2,4.8,1.8, 2],
        [6.1,2.8,4.0,1.3, 2],
        [6.3,2.5,4.9,1.5, 2],
        [6.1,2.8,4.7,1.2, 2],
        [6.4,2.9,4.3,1.3, 2],
        [6.6,3.0,4.4,1.4, 2],
        [6.8,2.8,4.8,1.4, 2],
        [6.7,3.0,5.0,1.7, 2],
        [6.0,2.9,4.5,1.5, 2],
        [5.7,2.6,3.5,1.0, 2],
        [5.5,2.4,3.8,1.1, 2],
        [5.5,2.4,3.7,1.0, 2],
        [5.8,2.7,3.9,1.2, 2],
        [6.0,2.7,5.1,1.6, 2],
        [5.4,3.0,4.5,1.5, 2],
        [6.0,3.4,4.5,1.6, 2],
        [6.7,3.1,4.7,1.5, 2],
        [6.3,2.3,4.4,1.3, 2],
        [5.6,3.0,4.1,1.3, 2],
        [5.5,2.5,4.0,1.3, 2],
        [5.5,2.6,4.4,1.2, 2],
        [6.1,3.0,4.6,1.4, 2],
        [5.8,2.6,4.0,1.2, 2],
        [5.0,2.3,3.3,1.0, 2],
        [5.6,2.7,4.2,1.3, 2],
        [5.7,3.0,4.2,1.2, 2],
        [5.7,2.9,4.2,1.3, 2],
        [6.2,2.9,4.3,1.3, 2],
        [5.1,2.5,3.0,1.1, 2],
        [5.7,2.8,4.1,1.3, 2],
        [6.3,3.3,6.0,2.5, 3],
        [5.8,2.7,5.1,1.9, 3],
        [7.1,3.0,5.9,2.1, 3],
        [6.3,2.9,5.6,1.8, 3],
        [6.5,3.0,5.8,2.2, 3],
        [7.6,3.0,6.6,2.1, 3],
        [4.9,2.5,4.5,1.7, 3],
        [7.3,2.9,6.3,1.8, 3],
        [6.7,2.5,5.8,1.8, 3],
        [7.2,3.6,6.1,2.5, 3],
        [6.5,3.2,5.1,2.0, 3],
        [6.4,2.7,5.3,1.9, 3],
        [6.8,3.0,5.5,2.1, 3],
        [5.7,2.5,5.0,2.0, 3],
        [5.8,2.8,5.1,2.4, 3],
        [6.4,3.2,5.3,2.3, 3],
        [6.5,3.0,5.5,1.8, 3],
        [7.7,3.8,6.7,2.2, 3],
        [7.7,2.6,6.9,2.3, 3],
        [6.0,2.2,5.0,1.5, 3],
        [6.9,3.2,5.7,2.3, 3],
        [5.6,2.8,4.9,2.0, 3],
        [7.7,2.8,6.7,2.0, 3],
        [6.3,2.7,4.9,1.8, 3],
        [6.7,3.3,5.7,2.1, 3],
        [7.2,3.2,6.0,1.8, 3],
        [6.2,2.8,4.8,1.8, 3],
        [6.1,3.0,4.9,1.8, 3],
        [6.4,2.8,5.6,2.1, 3],
        [7.2,3.0,5.8,1.6, 3],
        [7.4,2.8,6.1,1.9, 3],
        [7.9,3.8,6.4,2.0, 3],
        [6.4,2.8,5.6,2.2, 3],
        [6.3,2.8,5.1,1.5, 3],
        [6.1,2.6,5.6,1.4, 3],
        [7.7,3.0,6.1,2.3, 3],
        [6.3,3.4,5.6,2.4, 3],
        [6.4,3.1,5.5,1.8, 3],
        [6.0,3.0,4.8,1.8, 3],
        [6.9,3.1,5.4,2.1, 3],
        [6.7,3.1,5.6,2.4, 3],
        [6.9,3.1,5.1,2.3, 3],
        [5.8,2.7,5.1,1.9, 3],
        [6.8,3.2,5.9,2.3, 3],
        [6.7,3.3,5.7,2.5, 3],
        [6.7,3.0,5.2,2.3, 3],
        [6.3,2.5,5.0,1.9, 3],
        [6.5,3.0,5.2,2.0, 3],
        [6.2,3.4,5.4,2.3, 3],
        [5.9,3.0,5.1,1.8, 3]]


#DEFININDO A PORCENTAGEM PRA TREINO E TESTE
amostras = 150
treino = 100
teste = amostras - treino
knn = int = 1
max_knn = int
y = 1
knn_cv = 15
k_fold = 5
cross_validation = int = treino/k_fold
num_real = 1
acuracia_media = 0
quant_atr = 4



vet_atr = cria_matriz(amostras, quant_atr+1, 'N')
vet_norm2 = cria_matriz(amostras, quant_atr, 'N')
vet_norm = cria_matriz(quant_atr, amostras, 'N')
vet_atr = vet_atr_ini[:]
vet_treino = cria_matriz(treino, quant_atr+1, 'N')
vet_teste = cria_matriz(teste, quant_atr, 'N')
vet_comp = cria_matriz(teste, quant_atr+1, 'N')
vet_qua = cria_matriz(teste, treino, 'N')
men = cria_matriz(teste, 1, 'N')    
vet_euc = cria_matriz(teste, treino, 'N')
men_transp = cria_matriz(1, teste,'a')
ord_men = cria_matriz(teste, 1, 'a')
ord_men_transp = cria_matriz(1, teste, 'a')
vetor_euclideano = cria_matriz(1, teste, 0)
ord_vet_euc = cria_matriz(teste, treino, 0)
ord_vet_treino = cria_matriz(treino, quant_atr, 0)
ord_vet_comp = cria_matriz(treino, quant_atr+1, 0)

tot = float = 0
euc = float = 0
a = float = 0

vet_treino_val1 = cria_matriz(math.trunc(cross_validation)*4, quant_atr+1, 0)
vet_treino_val2 = cria_matriz(math.trunc(cross_validation)*4, quant_atr+1, 0)
vet_treino_val3 = cria_matriz(math.trunc(cross_validation)*4, quant_atr+1, 0)
vet_treino_val4 = cria_matriz(math.trunc(cross_validation)*4, quant_atr+1, 0)
vet_treino_val5 = cria_matriz(math.trunc(cross_validation)*4, quant_atr+1, 0)

vet_validation1 = cria_matriz(math.trunc(cross_validation), quant_atr, 0)
vet_validation2 = cria_matriz(math.trunc(cross_validation), quant_atr, 0)
vet_validation3 = cria_matriz(math.trunc(cross_validation), quant_atr, 0)
vet_validation4 = cria_matriz(math.trunc(cross_validation), quant_atr, 0)
vet_validation5 = cria_matriz(math.trunc(cross_validation), quant_atr, 0)

vet_validation1_comp = cria_matriz(math.trunc(cross_validation), quant_atr+1, 0)
vet_validation2_comp = cria_matriz(math.trunc(cross_validation), quant_atr+1, 0)
vet_validation3_comp = cria_matriz(math.trunc(cross_validation), quant_atr+1, 0)
vet_validation4_comp = cria_matriz(math.trunc(cross_validation), quant_atr+1, 0)
vet_validation5_comp = cria_matriz(math.trunc(cross_validation), quant_atr+1, 0)


grid = {}
grid2 = {}
grade = list()
grade_knn = list()
acc_grid = list()
k_grid = list()
realization = 1 #vari??vel que define as realiza????es do modelo
vet_knn = list()

for l in range(amostras):
        for c in range(quant_atr):
            vet_norm[c][l] = vet_atr_ini[l][c]
               
    
for l in range(quant_atr):
        for c in range(amostras):
            vet_norm2[c][l] = vet_norm[l][c]
               

for l in range(amostras):      
        for c in range(quant_atr):
                 minimo = min(vet_norm[c])
                 maximo = max(vet_norm[c])
                 vet_atr[l][c] = (vet_norm2[l][c] - minimo)/(maximo - minimo)
for realization in range(realization):
    knn = 1
    max_knn = 0
    for grid_search in range(y):
    
        knn += 2
        
        
        for realizacoes in range(num_real):
                acuracia_media1 = float = 0
                acuracia_media2 = float = 0
                acuracia_media3 = float = 0
                acuracia_media4 = float = 0
                acuracia_media5 = float = 0
    
            
                random.shuffle(vet_atr)
                
                for l in range(treino): #MATRIZ COM 100 AMOSTRAS PARA TREINO
                    for c in range(quant_atr+1):
                        vet_treino[l][c] = vet_atr[l][c]
            
                
                for l in range(treino, amostras): #MATRIZ COM 50 AMOSTRAS PARA TESTE SEM O CLASSIFICADOR
                    for c in range(4):
                        vet_teste[l-treino][c] = vet_atr[l][c]
            
                    
                for l in range(treino, amostras): #MATRIZ PARA REALIZAR A COMPARA????O COM A MATRIZ TESTADA
                    for c in range(quant_atr+1):
                        vet_comp[l-treino][c] = vet_atr[l][c]
                        
                vet_treino_copy1 = vet_treino[:]
                vet_treino_copy2 = vet_treino[:]
                vet_treino_copy3 = vet_treino[:]
                vet_treino_copy4 = vet_treino[:]
                vet_treino_copy5 = vet_treino[:]
            
                   
            ####################################################################################################
                           
                for l in range(math.trunc(cross_validation)*(k_fold-1), math.trunc(cross_validation)*(k_fold)):
                    for c in range(quant_atr+1):
                         vet_validation1_comp[l - math.trunc(cross_validation)*(k_fold-1)][c] = vet_treino_copy1[l][c]
                         
                for l in range(math.trunc(cross_validation)*(k_fold-1), math.trunc(cross_validation)*(k_fold)):
                    for c in range(quant_atr):
                         vet_validation1[l - math.trunc(cross_validation)*(k_fold-1)][c] = vet_treino_copy1[l][c]
            
                del(vet_treino_copy1[math.trunc(cross_validation)*(k_fold-1):math.trunc(cross_validation)*(k_fold)])
                
                vet_treino_val1 = vet_treino_copy1[:]
            #####################################################################################################
                for l in range(math.trunc(cross_validation)*(k_fold-2), math.trunc(cross_validation)*(k_fold-1)):
                    for c in range(quant_atr+1):
                        vet_validation2_comp[l - math.trunc(cross_validation)*(k_fold-2)][c] = vet_treino_copy2[l][c]
                
                for l in range(math.trunc(cross_validation)*(k_fold-2), math.trunc(cross_validation)*(k_fold-1)):
                    for c in range(quant_atr):
                        vet_validation2[l - math.trunc(cross_validation)*(k_fold-2)][c] = vet_treino_copy2[l][c]
            
              
                del(vet_treino_copy2[math.trunc(cross_validation)*(k_fold-2): math.trunc(cross_validation)*(k_fold-1)])
                vet_treino_val2 = vet_treino_copy2[:]
            #######################################################################################################            
                for l in range(math.trunc(cross_validation)*(k_fold-3), math.trunc(cross_validation)*(k_fold-2)):
                    for c in range(quant_atr+1):
                        vet_validation3_comp[l - math.trunc(cross_validation)*(k_fold-3)][c] = vet_treino_copy3[l][c]
                
                for l in range(math.trunc(cross_validation)*(k_fold-3), math.trunc(cross_validation)*(k_fold-2)):
                    for c in range(quant_atr):
                        vet_validation3[l - math.trunc(cross_validation)*(k_fold-2)][c] = vet_treino_copy3[l][c]
            
              
                del(vet_treino_copy3[math.trunc(cross_validation)*(k_fold-3): math.trunc(cross_validation)*(k_fold-2)])
                vet_treino_val3 = vet_treino_copy3[:]    
            ###################################################################################################    
                for l in range(math.trunc(cross_validation)*(k_fold-4), math.trunc(cross_validation)*(k_fold-3)):
                    for c in range(quant_atr+1):
                        vet_validation4_comp[l - math.trunc(cross_validation)*(k_fold-4)][c] = vet_treino_copy4[l][c]
                
                for l in range(math.trunc(cross_validation)*(k_fold-4), math.trunc(cross_validation)*(k_fold-3)):
                    for c in range(quant_atr):
                        vet_validation4[l - math.trunc(cross_validation)*(k_fold-3)][c] = vet_treino_copy4[l][c]
            
              
                del(vet_treino_copy4[math.trunc(cross_validation)*(k_fold-4): math.trunc(cross_validation)*(k_fold-3)])
                vet_treino_val4 = vet_treino_copy4[:]  
            ####################################################################################################    
                for l in range(math.trunc(cross_validation)):
                    for c in range(quant_atr+1):
                        vet_validation5_comp[l][c] = vet_treino_copy5[l][c]
                
                for l in range(math.trunc(cross_validation)):
                    for c in range(quant_atr):
                        vet_validation5[l][c] = vet_treino_copy5[l][c]
            
              
                del(vet_treino_copy5[:math.trunc(cross_validation)])
                vet_treino_val5 = vet_treino_copy5[:]     
            ##################################################################################################   
               
            
                men_val1 = cria_matriz(math.trunc(cross_validation), 1, 0)
                ord_men_val1 = cria_matriz(math.trunc(cross_validation), 1, 0)
                men_transp_val1 = cria_matriz(1, math.trunc(cross_validation), 0)
                vet_euc_val1 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*(k_fold-1), 0)
                ord_vet_euc_val1 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*k_fold, 0)
                
                for l in range(math.trunc(cross_validation)):
                    for c in range(math.trunc(cross_validation)*(k_fold - 1)):
                            euc = 0
                            euc += math.pow(vet_validation1[l][0] - vet_treino_val1[c][0], 2) 
                            euc += math.pow(vet_validation1[l][1] - vet_treino_val1[c][1], 2)
                            euc += math.pow(vet_validation1[l][2] - vet_treino_val1[c][2], 2)
                            euc += math.pow(vet_validation1[l][3] - vet_treino_val1[c][3], 2)
                            
                            vet_euc_val1[l][c] = euc
                    men_val1[l][0] = min(vet_euc_val1[l])   
               
                for l in range(math.trunc(cross_validation)):
                    men_transp_val1[0][l] = men_val1[l][0]
                      
                for l in range(math.trunc(cross_validation)):
                    ord_men_val1[l][0] = men_transp_val1[0][l]
                    
                for l in range(math.trunc(cross_validation)):# LA??O PARA ORDENAR O VETOR COM OS RESULTADOS DAS DIST??NCIAS
                    ord_vet_euc_val1[l] = sorted(vet_euc_val1[l])
                
                aux = 0
                class1 = class2 = class3 = int = 0 
                k = 0
                a = 0
                for l in range(math.trunc(cross_validation)):
                    class1 = 0
                    class2 = 0
                    class3 = 0
                    for x in range(knn):
                        for c in range(math.trunc(cross_validation)*(k_fold - 1)):    
                            
                          if ord_vet_euc_val1[l][k] == vet_euc_val1[l][c]:
                                ord_vet_euc_val1[l][k] = 'a'
                                k += 1
                                if vet_treino_val1[c][quant_atr] == 1:
                                    class1 += 1
                                elif vet_treino_val1[c][quant_atr] == 2:
                                    class2 += 1
                                elif vet_treino_val1[c][quant_atr] == 3:
                                    class3 += 1
                                    
                          if k == knn:
                            
                              if (class1 > class2) and (class1 > class3):
                                  moda = 1
                              elif class2 > class3 and (class2 > class1):
                                  moda = 2
                              elif class3 > class1 and (class3 > class2):
                                  moda = 3
                              k = 0
                             
                              if moda == vet_validation1_comp[l][quant_atr]:
                                  a += 1
                                 
                         
                acuracia_media1 += (a/cross_validation)*100
                grid [(acuracia_media1)/num_real] = {knn}
                   
               # print('A ACUR??CIA FOI DE {} %' .format(acuracia_media/num_real))    
            
            ##########################################################################################
                acuracia_media = 0
                a = 0
                men_val2 = cria_matriz(math.trunc(cross_validation), 1, 0)
                ord_men_val2 = cria_matriz(math.trunc(cross_validation), 1, 0)
                men_transp_val2 = cria_matriz(1, math.trunc(cross_validation), 0)
                vet_euc_val2 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*(k_fold-1), 0)
                ord_vet_euc_val2 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*k_fold, 0)
                
                for l in range(math.trunc(cross_validation)):
                    for c in range(math.trunc(cross_validation)*(k_fold - 1)):
                            euc = 0
                            euc += math.pow(vet_validation2[l][0] - vet_treino_val2[c][0], 2) 
                            euc += math.pow(vet_validation2[l][1] - vet_treino_val2[c][1], 2)
                            euc += math.pow(vet_validation2[l][2] - vet_treino_val2[c][2], 2)
                            euc += math.pow(vet_validation2[l][3] - vet_treino_val2[c][3], 2)
                            
                            vet_euc_val2[l][c] = euc
                    men_val2[l][0] = min(vet_euc_val2[l])   
               
                for l in range(math.trunc(cross_validation)):
                    men_transp_val2[0][l] = men_val2[l][0]
                      
                for l in range(math.trunc(cross_validation)):
                    ord_men_val2[l][0] = men_transp_val2[0][l]
                    
                for l in range(math.trunc(cross_validation)):# LA??O PARA ORDENAR O VETOR COM OS RESULTADOS DAS DIST??NCIAS
                    ord_vet_euc_val2[l] = sorted(vet_euc_val2[l])
                
                aux = 0
                class1 = class2 = class3 = int = 0 
                k = 0
                a = 0
                for l in range(math.trunc(cross_validation)):
                    class1 = 0
                    class2 = 0
                    class3 = 0
                    for x in range(knn):
                        for c in range(math.trunc(cross_validation)*(k_fold - 1)):    
                            
                          if ord_vet_euc_val2[l][k] == vet_euc_val2[l][c]:
                                ord_vet_euc_val2[l][k] = 'a'
                                k += 1
                                if vet_treino_val2[c][quant_atr] == 1:
                                    class1 += 1
                                elif vet_treino_val2[c][quant_atr] == 2:
                                    class2 += 1
                                elif vet_treino_val2[c][quant_atr] == 3:
                                    class3 += 1
                                    
                          if k == knn:
                            
                              if (class1 > class2) and (class1 > class3):
                                  moda = 1
                              elif class2 > class3 and (class2 > class1):
                                  moda = 2
                              elif class3 > class1 and (class3 > class2):
                                  moda = 3
                              k = 0
                             
                              if moda == vet_validation2_comp[l][quant_atr]:
                                  a += 1
                                 
                         
                acuracia_media2 += (a/cross_validation)*100
                grid [(acuracia_media2)/num_real] = {knn}
                   
            #print('A ACUR??CIA FOI DE {} %' .format(acuracia_media/num_real))    
            
            #####################################################################################
                acuracia_media = 0
                a = 0
                men_val3 = cria_matriz(math.trunc(cross_validation), 1, 0)
                ord_men_val3 = cria_matriz(math.trunc(cross_validation), 1, 0)
                men_transp_val3 = cria_matriz(1, math.trunc(cross_validation), 0)
                vet_euc_val3 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*(k_fold-1), 0)
                ord_vet_euc_val3 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*k_fold, 0)
                
                for l in range(math.trunc(cross_validation)):
                    for c in range(math.trunc(cross_validation)*(k_fold - 1)):
                            euc = 0
                            euc += math.pow(vet_validation3[l][0] - vet_treino_val3[c][0], 2) 
                            euc += math.pow(vet_validation3[l][1] - vet_treino_val3[c][1], 2)
                            euc += math.pow(vet_validation3[l][2] - vet_treino_val3[c][2], 2)
                            euc += math.pow(vet_validation3[l][3] - vet_treino_val3[c][3], 2)
                            
                            vet_euc_val3[l][c] = euc
                    men_val3[l][0] = min(vet_euc_val3[l])   
               
                for l in range(math.trunc(cross_validation)):
                    men_transp_val3[0][l] = men_val3[l][0]
                      
                for l in range(math.trunc(cross_validation)):
                    ord_men_val3[l][0] = men_transp_val3[0][l]
                    
                for l in range(math.trunc(cross_validation)):# LA??O PARA ORDENAR O VETOR COM OS RESULTADOS DAS DIST??NCIAS
                    ord_vet_euc_val3[l] = sorted(vet_euc_val3[l])
                
                aux = 0
                class1 = class2 = class3 = int = 0 
                k = 0
                a = 0
                for l in range(math.trunc(cross_validation)):
                    class1 = 0
                    class2 = 0
                    class3 = 0
                    for x in range(knn):
                        for c in range(math.trunc(cross_validation)*(k_fold - 1)):    
                            
                          if ord_vet_euc_val3[l][k] == vet_euc_val3[l][c]:
                                ord_vet_euc_val3[l][k] = 'a'
                                k += 1
                                if vet_treino_val3[c][quant_atr] == 1:
                                    class1 += 1
                                elif vet_treino_val3[c][quant_atr] == 2:
                                    class2 += 1
                                elif vet_treino_val3[c][quant_atr] == 3:
                                    class3 += 1
                                    
                          if k == knn:
                            
                              if (class1 > class2) and (class1 > class3):
                                  moda = 1
                              elif class2 > class3 and (class2 > class1):
                                  moda = 2
                              elif class3 > class1 and (class3 > class2):
                                  moda = 3
                              k = 0
                             
                              if moda == vet_validation3_comp[l][quant_atr]:
                                  a += 1
                                 
                         
                acuracia_media3 += (a/cross_validation)*100    
                grid [(acuracia_media3)/num_real] = {knn}
                   
            #print('A ACUR??CIA FOI DE {} %' .format(acuracia_media/num_real))    
            
            ##################################################################################################
                acuracia_media = 0
                a = 0
                men_val4 = cria_matriz(math.trunc(cross_validation), 1, 0)
                ord_men_val4 = cria_matriz(math.trunc(cross_validation), 1, 0)
                men_transp_val4 = cria_matriz(1, math.trunc(cross_validation), 0)
                vet_euc_val4 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*(k_fold-1), 0)
                ord_vet_euc_val4 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*k_fold, 0)
                
                for l in range(math.trunc(cross_validation)):
                    for c in range(math.trunc(cross_validation)*(k_fold - 1)):
                            euc = 0
                            euc += math.pow(vet_validation4[l][0] - vet_treino_val4[c][0], 2) 
                            euc += math.pow(vet_validation4[l][1] - vet_treino_val4[c][1], 2)
                            euc += math.pow(vet_validation4[l][2] - vet_treino_val4[c][2], 2)
                            euc += math.pow(vet_validation4[l][3] - vet_treino_val4[c][3], 2)
                            
                            vet_euc_val4[l][c] = euc
                    men_val4[l][0] = min(vet_euc_val4[l])   
               
                for l in range(math.trunc(cross_validation)):
                    men_transp_val4[0][l] = men_val4[l][0]
                      
                for l in range(math.trunc(cross_validation)):
                    ord_men_val4[l][0] = men_transp_val4[0][l]
                    
                for l in range(math.trunc(cross_validation)):# LA??O PARA ORDENAR O VETOR COM OS RESULTADOS DAS DIST??NCIAS
                    ord_vet_euc_val4[l] = sorted(vet_euc_val4[l])
                
                aux = 0
                class1 = class2 = class3 = int = 0 
                k = 0
                a = 0
                for l in range(math.trunc(cross_validation)):
                    class1 = 0
                    class2 = 0
                    class3 = 0
                    for x in range(knn):
                        for c in range(math.trunc(cross_validation)*(k_fold - 1)):    
                            
                          if ord_vet_euc_val4[l][k] == vet_euc_val4[l][c]:
                                ord_vet_euc_val4[l][k] = 'a'
                                k += 1
                                if vet_treino_val4[c][quant_atr] == 1:
                                    class1 += 1
                                elif vet_treino_val4[c][quant_atr] == 2:
                                    class2 += 1
                                elif vet_treino_val4[c][quant_atr] == 3:
                                    class3 += 1
                                    
                          if k == knn:
                            
                              if (class1 > class2) and (class1 > class3):
                                  moda = 1
                              elif class2 > class3 and (class2 > class1):
                                  moda = 2
                              elif class3 > class1 and (class3 > class2):
                                  moda = 3
                              k = 0
                             
                              if moda == vet_validation4_comp[l][quant_atr]:
                                  a += 1
                                 
                         
                acuracia_media4 += (a/cross_validation)*100     
                grid [(acuracia_media4)/num_real] = {knn}   
            #print('A ACUR??CIA FOI DE {} %' .format(acuracia_media/num_real))    
            
            ################################################################################################
                acuracia_media = 0
                a = 0
                men_val5 = cria_matriz(math.trunc(cross_validation), 1, 0)
                ord_men_val5 = cria_matriz(math.trunc(cross_validation), 1, 0)
                men_transp_val5 = cria_matriz(1, math.trunc(cross_validation), 0)
                vet_euc_val5 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*(k_fold-1), 0)
                ord_vet_euc_val5 = cria_matriz(math.trunc(cross_validation), math.trunc(cross_validation)*k_fold, 0)
                
                for l in range(math.trunc(cross_validation)):
                    for c in range(math.trunc(cross_validation)*(k_fold - 1)):
                            euc = 0
                            euc += math.pow(vet_validation5[l][0] - vet_treino_val5[c][0], 2) 
                            euc += math.pow(vet_validation5[l][1] - vet_treino_val5[c][1], 2)
                            euc += math.pow(vet_validation5[l][2] - vet_treino_val5[c][2], 2)
                            euc += math.pow(vet_validation5[l][3] - vet_treino_val5[c][3], 2)
                            
                            vet_euc_val5[l][c] = euc
                    men_val5[l][0] = min(vet_euc_val5[l])   
               
                for l in range(math.trunc(cross_validation)):
                    men_transp_val5[0][l] = men_val5[l][0]
                      
                for l in range(math.trunc(cross_validation)):
                    ord_men_val5[l][0] = men_transp_val5[0][l]
                    
                for l in range(math.trunc(cross_validation)):# LA??O PARA ORDENAR O VETOR COM OS RESULTADOS DAS DIST??NCIAS
                    ord_vet_euc_val5[l] = sorted(vet_euc_val5[l])
                
                aux = 0
                class1 = class2 = class3 = int = 0 
                k = 0
                a = 0
                for l in range(math.trunc(cross_validation)):
                    class1 = 0
                    class2 = 0
                    class3 = 0
                    for x in range(knn):
                        for c in range(math.trunc(cross_validation)*(k_fold - 1)):    
                            
                          if ord_vet_euc_val5[l][k] == vet_euc_val5[l][c]:
                                ord_vet_euc_val5[l][k] = 'a'
                                k += 1
                                if vet_treino_val5[c][quant_atr] == 1:
                                    class1 += 1
                                elif vet_treino_val5[c][quant_atr] == 2:
                                    class2 += 1
                                elif vet_treino_val5[c][quant_atr] == 3:
                                    class3 += 1
                                    
                          if k == knn:
                            
                              if (class1 > class2) and (class1 > class3):
                                  moda = 1
                              elif class2 > class3 and (class2 > class1):
                                  moda = 2
                              elif class3 > class1 and (class3 > class2):
                                  moda = 3
                              k = 0
                             
                              if moda == vet_validation5_comp[l][quant_atr]:
                                  a += 1
                                 
                         
                acuracia_media5 += (a/cross_validation)*100 
        media_cv = ((acuracia_media1/num_real) + (acuracia_media2/num_real) + (acuracia_media3/num_real) + (acuracia_media4/num_real) + (acuracia_media5/num_real))/5
    #    grid [knn] = media_cv
    #    max_var = max(grid)
    #    max_knn = next(iter(grid[max_var]))
        grade.append(media_cv)
        grade_knn.append(knn)
        
        max_var = max(grade)
        indice = grade.index(max_var)
        max_knn = grade_knn[indice]
        
        
        
        print('KNN de {}' .format(knn))   
        print(media_cv)
        print(f'O kNN ideal ?? ', max_knn)
#        print('A ACUR??CIA 01 FOI DE {} %' .format(acuracia_media1/num_real))
#        print('A ACUR??CIA 02 FOI DE {} %' .format(acuracia_media2/num_real))
#        print('A ACUR??CIA 03 FOI DE {} %' .format(acuracia_media3/num_real))    
#        print('A ACUR??CIA 04 FOI DE {} %' .format(acuracia_media4/num_real))
#        print('A ACUR??CIA 05 FOI DE {} %' .format(acuracia_media5/num_real))       
##########################################################################################
    
    a = 0
    acuracia_media = 0
    knn =  max_knn
    acc = float = 0
    #knn = 0
    num_real = 1
    vet_acuracia_graph = cria_matriz(1, num_real, 0)
    #vet_knn = cria_matriz(1, num_real, 0)
    for realizacao in range(num_real):
            
           # random.shuffle(vet_atr) 
            
            matriz_confusao = cria_matriz(4,4,0)
            
            for l in range(treino): #MATRIZ COM 100 AMOSTRAS PARA TREINO
                for c in range(quant_atr+1):
                    vet_treino[l][c] = vet_atr[l][c]
        
            
            for l in range(treino, amostras): #MATRIZ COM 50 AMOSTRAS PARA TESTE SEM O CLASSIFICADOR
                for c in range(quant_atr):
                    vet_teste[l-treino][c] = vet_atr[l][c]
        
                
            for l in range(treino, amostras): #MATRIZ PARA REALIZAR A COMPARA????O COM A MATRIZ TESTADA
                for c in range(quant_atr+1):
                    vet_comp[l-treino][c] = vet_atr[l][c]
            
            for l in range(teste):#30
                for c in range(treino):#120
                        euc = 0
                        euc += math.pow(vet_teste[l][0] - vet_treino[c][0], 2) 
                        euc += math.pow(vet_teste[l][1] - vet_treino[c][1], 2)
                        euc += math.pow(vet_teste[l][2] - vet_treino[c][2], 2)
                        euc += math.pow(vet_teste[l][3] - vet_treino[c][3], 2)
                        
                        vet_euc[l][c] = euc
                men[l][0] = min(vet_euc[l])   
        
            for l in range(teste):
                men_transp[0][l] = men[l][0]
                  
            for l in range(teste):
                ord_men[l][0] = men_transp[0][l]
            
            for l in range(teste):
                ord_vet_euc[l] = sorted(vet_euc[l])
                
            for l in range(treino):
                ord_vet_treino[l] = sorted(vet_treino[l])
                
            for l in range(teste):
                ord_vet_comp[l] = sorted(vet_comp[l])
            
            aux = 0
            class1 = class2 = class3 = int = 0 
            k = 0
            acuracia = 0
            a = 0
            for l in range(teste):
                class1 = 0
                class2 = 0
                class3 = 0
                for x in range(knn):
                    for c in range(treino):    
                        
                      if ord_vet_euc[l][k] == vet_euc[l][c]:
                            ord_vet_euc[l][k] = 'a'
                            k += 1
                            if vet_treino[c][quant_atr] == 1:
                                class1 += 1
                            elif vet_treino[c][quant_atr] == 2:
                                class2 += 1
                            elif vet_treino[c][quant_atr] == 3:
                                class3 += 1
                      
                        
                      if k == knn:
                        
                          if (class1 > class2) and (class1 > class3):
                              moda = 1
                          elif class2 > class3 and (class2 > class1):
                              moda = 2
                          elif class3 > class1 and (class3 > class2):
                              moda = 3
                          k = 0
                          
                          matriz_confusao[vet_comp[l][quant_atr]][moda] += 1
                          if moda == vet_comp[l][quant_atr]:
                              a += 1
                            
                     
            acuracia_media += (a/teste)*100   
            acuracia = (a/teste)*100
            print(acuracia)
            #vet_acuracia_graph.append(acuracia) 
           
            acc_grid.append(acuracia)
            k_grid.append(knn)

max_acc = max(acc_grid)
indice = acc_grid.index(max_acc)
melhor_k = k_grid[indice]
melhor_acc = np.mean(acc_grid)
del(matriz_confusao[0])
del(matriz_confusao[0][0])
del(matriz_confusao[1][0])
del(matriz_confusao[2][0])
print('\n\nMATRIZ DE CONFUS??O\n\n')
for l in range(3):
    for c in range(3):
        print(f'{(matriz_confusao[l][c]/teste)*100}  ', end = '')
    print()
#print('{}'.format(matriz_confusao))
print('\n\n\n')
print('O K selecionado foi de {}' .format(melhor_k))            
print('A MAIOR ACUR??CIA M??DIA FOI DE {} %' .format((max_acc)))    

#plt.boxplot(vet_acuracia_graph)
#plt.title('Boxplot DMC - IRIS 80% TREINO')
#plt.ylabel('ACUR??CIA')

#plt.title('ACUR??CIA EM FUN????O DO K')
#plt.xlabel('KNN')
#plt.ylabel('ACUR??CIA')
#plt.plot (k_grid, acc_grid, 1, color = "blue")
#
##plt.boxplot (vet_acuracia_graph[0], len(vet_acuracia_graph[0]), 1 )     
#plt.show()           
#        

######################################################################################
##  GR??FICO DE SUPERF??CIE  ###########################################################

intervalo = 0.05
f_inf = 0
f_sup = 1 + intervalo 
faixa = np.arange(f_inf, f_sup, intervalo)
fator = f_sup / intervalo

atr1 = []
atr2 = []

for l in range(len(faixa)):
    atr1.extend([faixa[l]]*math.trunc(fator))
    
for l in range(len(faixa)):
    for c in range(math.trunc(fator)):
        atr2.extend([faixa[c]])
        
p_grid = np.zeros((len(atr1), 2))
       
for l in range(len(atr1)):
    p_grid[l][0] = atr1[l]
    
for l in range(len(atr1)):
    p_grid[l][1] = atr2[l]

class_graph = np.zeros((len(atr1), 1))
                            


#######################################################################################
### CLASSIFICA????O ################    

vetor_dist = np.zeros((len(atr1), amostras))
men_graph = np.zeros((len(atr1), 1))
men_transp_graph = np.zeros((1, len(atr1)))
ord_men_graph = np.zeros((len(atr1), 1))     
ord_vetor_dist_graph = np.zeros((len(atr1), amostras))
vet_atr_graph = np.zeros((amostras, quant_atr))

for l in range(amostras):
    for c in range(quant_atr):
        vet_atr_graph[l][c] = vet_atr[l][c]


      
for l in range(len(atr1)):
    for c in range(amostras):
        euc = 0
        euc += math.pow(p_grid[l][0] - vet_atr_graph[c][0], 2)
        euc += math.pow(p_grid[l][1] - vet_atr_graph[c][1], 2)
                        
        vetor_dist[l][c] = euc
    men_graph[l][0] = min(vetor_dist[l])   
    
for l in range(len(atr1)):
                men_transp_graph[0][l] = men_graph[l][0]
                  
for l in range(len(atr1)):
                ord_men_graph[l][0] = men_transp_graph[0][l]
            
for l in range(len(atr1)):
                ord_vetor_dist_graph[l] = sorted(vetor_dist[l])
                        

aux = 0
class1 = class2 = class3 = int = 0 
k = 0
acuracia = 0
a = 0
knn = 7
p_grid_resp = np.zeros((len(atr1), 3))

for l in range(len(atr1)):
    for c in range(2):
        p_grid_resp[l][c] = p_grid[l][c]

for l in range(len(atr1)):
    class1 = 0
    class2 = 0
    class3 = 0
    for x in range(knn):
        for c in range(amostras):    
                        
            if ord_vetor_dist_graph[l][k] == vetor_dist[l][c]:
                ord_vetor_dist_graph[l][k] = 300000
                k += 1
                if vet_atr[c][quant_atr] == 1:
                    class1 += 1
                elif vet_atr[c][quant_atr] == 2:
                    class2 += 1
                elif vet_atr[c][quant_atr] == 3:
                    class3 += 1
                      
                        
                if k == knn:
                        
                          if (class1 > class2) and (class1 > class3):
                              moda = 1
                              p_grid_resp[l][2] = 1
                          elif class2 > class3 and (class2 > class1):
                              moda = 2
                              p_grid_resp[l][2] = 2
                          elif class3 > class1 and (class3 > class2):
                              moda = 3
                              p_grid_resp[l][2] = 3
                          k = 0
o = int = 0
                          
for l in range(len(atr1)):
    class_graph[l][0] = p_grid_resp[l][2]
    
for l in range(len(atr1)):
    if class_graph[l][0] == 0:
        o += 1
        class_graph[l][0] = 1
print(o)    
from matplotlib.colors import ListedColormap


cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
plt.scatter(p_grid[:, 0], p_grid[:, 1], c=class_graph[:, 0], cmap=cmap_light)

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
plt.scatter(vet_atr_graph[:, 0], vet_atr_graph[:, 1], c=vet_atr_graph[:, 2], cmap=cmap_bold)


#
#plt.pcolormesh(atr1, atr2, Z, cmap=cmap_light)                         
#                     
#                            
#for l in range(len(atr1)):
#    if p_grid_resp[l][2] == 1:
#        plt.plot(p_grid_resp[l], 0.2, 'go')
#plt.show()            
#      
# 