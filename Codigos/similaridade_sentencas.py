#biblioteca utilizada para tratar o arquivo xml
import xml.etree.ElementTree as ET
import requests

#utilizado para abrir o arquivo xml
from Codigos.pre_processamento_text import pre_processamento_texto

arquivo2 = "Regimento_MACC.xml"
arquivo_regimento =  ET.parse(arquivo2)
lista_regimento = []

filtro = "*"
for child in arquivo_regimento.iter(filtro):
    #print(child.tag)#retorna as tags
   # print(child.text)#retorna conteudo das tags
    lista_regimento.append(child.text)
#gerando uma lista pre-processada do regimento
lista_regimento_pre_processado = []
for i in lista_regimento:
    lista = pre_processamento_texto(i)
    lista_regimento_pre_processado.append(lista)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# calcular similariedade do cosseno + TF-IDF
def similaridade_sentencas(sentenca):
    lista_similaridade = []
    # recebe a sentença para se analisar é ja faz o pré-processamento
    sentenca_entrada = pre_processamento_texto(sentenca)
    # adicionar a sentenca de entrada no conjunto do regimento
    lista_regimento.append(sentenca)
    lista_regimento_pre_processado.append(sentenca_entrada)

    # convertendo base de dados para tf-idf
    tfidf = TfidfVectorizer()
    palavras_vetorizadas = tfidf.fit_transform(lista_regimento_pre_processado)

    # calculo da similariedade
    # pega a ultima frase que foi adicionada que no caso e nossa 'sentenca_entrada'
    similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas)

    # ordena por ordem decrescente cada indice
    similaridade.argsort()

    # 5 maiores resultados de similariedade
    n1 = similaridade.argsort()[0][-2]
    n2 = similaridade.argsort()[0][-3]
    n3 = similaridade.argsort()[0][-4]
    n4 = similaridade.argsort()[0][-5]
    n5 = similaridade.argsort()[0][-6]

    lista_similaridade.append(str(lista_regimento[n1]))
    #lista_similaridade.append(str(lista_regimento[n2]))
    #lista_similaridade.append(str(lista_regimento[n3]))
    #lista_similaridade.append(str(lista_regimento[n4]))
    #lista_similaridade.append(str(lista_regimento[n5]))

    # remove a sentenca adicionada
    del (lista_regimento[-1])
    del (lista_regimento_pre_processado[-1])

    return str(lista_similaridade)

