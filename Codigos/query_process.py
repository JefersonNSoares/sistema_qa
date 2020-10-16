#!/usr/bin/python
# -*- coding: utf8 -*-
import nlpnet
from Codigos.pre_processamento_text import pre_processamento_texto
def query_process(texto_entrada):
    #Diretorio dos modelos de etiquetação
    data_dir = 'pos-pt'
    #Definição do diretorio e linguagem a utilizar
    tagger = nlpnet.POSTagger(data_dir, language='pt')
    tagged_str = tagger.tag(texto_entrada)
    #print(tagged_str)

    texto_consulta = []
    for i in tagged_str:
        #print(i)
        for k in i:
            # print(k)
            tags = ['NPROP', 'NUM', 'V', 'ADJ', 'N']
            entrada = k
            for i in tags:
                # print(i)
                if entrada[1] == i:
                    texto_consulta.append(entrada[0])

    return str(texto_consulta)

x = query_process("O rato roeu a ropa do rei de roma")
y = pre_processamento_texto(x)
print(y)