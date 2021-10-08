import random
import math
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

exemplo_1 = np.array([[random.uniform(-0.1, 0.1), random.uniform(0.9, 1.1)]for _ in range(50)])
exemplo_2 = np.array([[random.uniform(0.9, 1.1), random.uniform(-0.1, 0.1)]for _ in range(50)])
exemplo_3 = np.array([[random.uniform(0.9, 1.1), random.uniform(0.9, 1.1)]for _ in range(50)])
exemplo_4 = np.array([[random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]for _ in range(50)])

dataset = np.zeros((200, 3))

for l in range(50):
    for c in range(2):
        dataset[l][c] = exemplo_1[l][c]
        dataset[l][2] = 1
for l in range(50):
    for c in range(2):
        dataset[l+50][c] = exemplo_2[l][c]
        dataset[l+50][2] = 1
for l in range(50):
    for c in range(2):
        dataset[l+100][c] = exemplo_3[l][c]
        dataset[l+100][2] = 1
for l in range(50):
    for c in range(2):
        dataset[l+150][c] = exemplo_4[l][c]
        dataset[l+150][2] = 2

vet_atr_ini = dataset



classes = 3
amostras = 200
treino = 150
teste = amostras - treino
div = math.trunc(treino/classes)
quant_atr = 2

vet_atr_ini2 = np.zeros((amostras, 2))
vet_treino = cria_matriz(treino, quant_atr+1, 0)
vet_teste = cria_matriz(teste, quant_atr, 0)
vet_comp = cria_matriz(treino, quant_atr+1, 0)

vet_norm2 = cria_matriz(amostras, quant_atr, 'N')
vet_norm = cria_matriz(quant_atr, amostras, 'N')

vet_atr_trans = cria_matriz(quant_atr, amostras, 0)
vet_atr = cria_matriz(amostras, quant_atr+1, 0)
num_real = 50
acuracia = 0
vet_acuracia_graph = cria_matriz(1, num_real, 0) 
acc = float = 0
matriz_confusao = cria_matriz(4,4,0)

for l in range(amostras):
    for c in range(quant_atr):
        vet_atr_ini2[l][c] = vet_atr_ini2[l][c]

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
                 
for l in range(amostras):
    vet_atr[l][quant_atr] = vet_atr_ini[l][quant_atr]

for realizacoes in range (num_real):
        
        random.shuffle(vet_atr)
        
        
        for l in range(treino): #MATRIZ COM 100 AMOSTRAS PARA TREINO
            for c in range(quant_atr+1):
                        vet_treino[l][c] = vet_atr[l][c]
            
                
        for l in range(treino, amostras): #MATRIZ COM 50 AMOSTRAS PARA TESTE SEM O CLASSIFICADOR
            for c in range(quant_atr):
                        vet_teste[l-treino][c] = vet_atr[l][c]
            
                    
        for l in range(treino, amostras): #MATRIZ PARA REALIZAR A COMPARAÇÃO COM A MATRIZ TESTADA
            for c in range(quant_atr+1):
                        vet_comp[l-treino][c] = vet_atr[l][c]
                
        
        for l in range(quant_atr):
            for c in range(treino):
                vet_atr_trans[l][c] = vet_treino[c][l]
        
        x = y = z = int = 0
        
        for l in range(treino):
                if vet_treino[l][quant_atr] == 1:
                     x += 1
        
                elif vet_treino[l][quant_atr] == 2:
                     y += 1
                    
                elif vet_treino[l][quant_atr] == 3:
                     z += 1
        
        vet_classe1 = cria_matriz(x, quant_atr, 0)
        vet_classe2 = cria_matriz(y, quant_atr, 0)
        vet_classe3 = cria_matriz(z, quant_atr, 0)         
        
        x=0
        y=0
        z=0
        for l in range(treino):
                if vet_treino[l][quant_atr] == 1:
                     vet_classe1[x][0] = vet_treino[l][0]
                     vet_classe1[x][1] = vet_treino[l][1]
                    
                     x += 1
                    
        
                if vet_treino[l][quant_atr] == 2:
                     vet_classe2[y][0] = vet_treino[l][0]
                     vet_classe2[y][1] = vet_treino[l][1]
                    
                     y += 1
                    
                elif vet_treino[l][quant_atr] == 3:
                     vet_classe3[z][0] = vet_treino[l][0]
                     vet_classe3[z][1] = vet_treino[l][1]
                    
                     z += 1
        
        vet_classe1_transp = cria_matriz(quant_atr, x, 0)
        vet_classe2_transp = cria_matriz(quant_atr, y, 0)
        vet_classe3_transp = cria_matriz(quant_atr, z, 0)
        
        for l in range(x):
            for c in range(quant_atr):
                vet_classe1_transp[c][l] = vet_classe1[l][c]
                
        for l in range(y):
            for c in range(quant_atr):
                vet_classe2_transp[c][l] = vet_classe2[l][c]
                
        for l in range(z):
            for c in range(quant_atr):
                vet_classe3_transp[c][l] = vet_classe3[l][c]
        
        media1 = cria_matriz(1, quant_atr, 0)
        for l in range(quant_atr):
            media1[0][l]  = np.mean(vet_classe1_transp[l]) 
            
        media2 = cria_matriz(1, quant_atr, 0)
        for l in range(quant_atr):
            media2[0][l]  = np.mean(vet_classe2_transp[l]) 
            
        media3 = cria_matriz(1, quant_atr, 0)
        for l in range(quant_atr):
            media3[0][l]  = np.mean(vet_classe3_transp[l]) 
            
        classe1 = 0
        classe2 = 0
        classe3 = 0
        
        euc1 = euc2 = euc3 = 0
        vet_euc1 = cria_matriz(1, teste, 0)
        vet_euc2 = cria_matriz(1, teste, 0)
        vet_euc3 = cria_matriz(1, teste, 0)
        #random.shuffle(vet_atr)
            
        for l in range(teste):
                 euc1 = 0
                 euc1 += math.pow(media1[0][0] - vet_teste[l][0], 2)
                 euc1 += math.pow(media1[0][1] - vet_teste[l][1], 2)
     
                 
                 euc2 = 0
                 euc2 += math.pow(media2[0][0] - vet_teste[l][0], 2)
                 euc2 += math.pow(media2[0][1] - vet_teste[l][1], 2)
                
                 
                 euc3 = 0
                 euc3 += math.pow(media3[0][0] - vet_teste[l][0], 2)
                 euc3 += math.pow(media3[0][1] - vet_teste[l][1], 2)
                
                 vet_euc1[0][l] = euc1
                 vet_euc2[0][l] = euc2
                 vet_euc3[0][l] = euc3
        a = 0
        acuracia = 0       
        for l in range(teste):
            
            if (vet_euc1[0][l] < vet_euc2[0][l]) and (vet_euc1[0][l] < vet_euc3[0][l]):
                classe = 1
                if classe == vet_comp[l][quant_atr]:
                    a += 1
            if (vet_euc2[0][l] < vet_euc1[0][l]) and (vet_euc2[0][l] < vet_euc3[0][l]):
                classe = 2
                if classe == vet_comp[l][quant_atr]:
                    a += 1
            
                    
            #matriz_confusao[vet_comp[l][quant_atr]][classe] += 1
        acuracia = (a/teste)*100
        acc += (a/teste)*100
        vet_acuracia_graph[0][realizacoes] = acuracia
        print(acuracia)
acuracia_media = (acc/num_real)
print('A ACURÁCIA MÉDIA FOI DE:')
print(acuracia_media)

del(matriz_confusao[0])
del(matriz_confusao[0][0])
del(matriz_confusao[1][0])
del(matriz_confusao[2][0])
print('\n\nMATRIZ DE CONFUSÃO\n\n')
for l in range(3):
    for c in range(3):
        print(f'{(matriz_confusao[l][c]/(teste*num_real)*100):.2f}  ', end = '')
    print()

######################################################################################
##  GRÁFICO DE SUPERFÍCIE  ###########################################################

intervalo = 0.005
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
p_grid_resp = np.zeros((len(atr1), 3))
       
for l in range(len(atr1)):
    p_grid[l][0] = atr1[l]
    
for l in range(len(atr1)):
    p_grid[l][1] = atr2[l]

class_graph = np.zeros((len(atr1), 1))
                            


#######################################################################################
### CLASSIFICAÇÃO ################    

vetor_dist = np.zeros((len(atr1), amostras))
men_graph = np.zeros((len(atr1), 1))
men_transp_graph = np.zeros((1, len(atr1)))
ord_men_graph = np.zeros((len(atr1), 1))     
ord_vetor_dist_graph = np.zeros((len(atr1), amostras))
vet_atr_graph = np.zeros((amostras, quant_atr))

for l in range(amostras):
    for c in range(quant_atr):
        vet_atr_graph[l][c] = vet_atr[l][c]

## DISTÂNCIA
vetor_dist1 = np.zeros((1, len(atr1)))
vetor_dist2 = np.zeros((1, len(atr1)))
vetor_dist3 = np.zeros((1, len(atr1)))
for l in range(len(atr1)):
                 euc1 = 0
                 euc1 += math.pow(media1[0][0] - p_grid[l][0], 2)
                 euc1 += math.pow(media1[0][1] - p_grid[l][1], 2)
                 
                 
                 euc2 = 0
                 euc2 += math.pow(media2[0][0] - p_grid[l][0], 2)
                 euc2 += math.pow(media2[0][1] - p_grid[l][1], 2)
              
                 
                 euc3 = 0
                 euc3 += math.pow(media3[0][0] - p_grid[l][0], 2)
                 euc3 += math.pow(media3[0][1] - p_grid[l][1], 2)
                
                
                 vetor_dist1[0][l] = euc1
                 vetor_dist2[0][l] = euc2
                 vetor_dist3[0][l] = euc3
                       

a = 0
acuracia = 0   
classe1 = 0
classe2 = 0
classe3 = 0    
for l in range(len(atr1)):
            
    if (vetor_dist1[0][l] < vetor_dist2[0][l]):
        classe = 1
        p_grid_resp[l][2] = classe
        
    if (vetor_dist2[0][l] < vetor_dist1[0][l]):
        classe = 2
        p_grid_resp[l][2] = classe
        
   
       
                    
for l in range(len(atr1)):
    class_graph[l][0] = p_grid_resp[l][2]

  
from matplotlib.colors import ListedColormap
quant_a = 0
quant_b = 0


for l in range(len(vet_treino)):
        if vet_treino[l][quant_atr] == 1:
            quant_a += 1
        elif vet_treino[l][quant_atr] == 2:
            quant_b += 1
        

a = np.zeros((quant_a, 2))
b = np.zeros((quant_b, 2))

x = 0
y = 0

for l in range(len(vet_treino)):
        if vet_treino[l][quant_atr] == 1:
            a[x][0] = vet_treino[l][0]
            a[x][1] = vet_treino[l][1]
            x+=1
        elif vet_treino[l][quant_atr] == 2:
            b[y][0] = vet_treino[l][0]
            b[y][1] = vet_treino[l][1]
            y+=1
       
quant_a_t = 0
quant_b_t = 0


for l in range(len(vet_comp)):
        if vet_comp[l][quant_atr] == 1:
            quant_a_t += 1
        elif vet_comp[l][quant_atr] == 2:
            quant_b_t += 1
        
a_t = np.zeros((quant_a_t, 2))
b_t = np.zeros((quant_b_t, 2))

x = 0
y = 0
w = 0 
for l in range(len(vet_comp)):
        if vet_comp[l][quant_atr] == 1:
            a_t[x][0] = vet_comp[l][0]
            a_t[x][1] = vet_comp[l][1]
            x+=1
        elif vet_comp[l][quant_atr] == 2:
            b_t[y][0] = vet_comp[l][0]
            b_t[y][1] = vet_comp[l][1]
            y+=1
        



#cmap_bold = ListedColormap(['#FF0000', '#00FF00'])
#cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
#plt.scatter(p_grid[:, 0], p_grid[:, 1], c=class_graph[:, 0], cmap=cmap_light)
#plt.scatter(vet_atr_graph[:, 0], vet_atr_graph[:, 1], c=dataset[:, 2], cmap=cmap_bold)

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])


plt.xlabel('ATRIBUTO A')
plt.ylabel('ATRIBUTO B')
    
plt.scatter(p_grid[:, 0], p_grid[:, 1], c=class_graph[:, 0], cmap=cmap_light)
plt.scatter(np.array(vet_atr_graph)[:, 0], np.array(vet_atr_graph)[:, 1], c=np.array(vet_atr)[:, 2], cmap=cmap_bold)

#plt.scatter (np.array(a)[:, 0], np.array(a)[:, 1], s=30, edgecolor = 'k', c='red', label='ATRIBUTO A TREINO')
#plt.scatter (np.array(b)[:, 0], np.array(b)[:, 1], s=30, edgecolor = 'k', c='blue', label='ATRIBUTO B TREINO')
#plt.scatter (np.array(a_t)[:, 0], np.array(a_t)[:, 1], s=30, edgecolor = 'k', c='orange', label='ATRIBUTO A TESTE')
#plt.scatter (np.array(b_t)[:, 0], np.array(b_t)[:, 1], s=30, edgecolor = 'k', c='black', label='ATRIBUTO B TESTE')
#plt.legend() 

#cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
#plt.scatter(vet_atr_graph[:, 0], vet_atr_graph[:, 1], c=vet_atr_graph[:, 2], cmap=cmap_light)
