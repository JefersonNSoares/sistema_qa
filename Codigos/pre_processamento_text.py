#implementação das funcões para pré-processamento dos texto
import importlib
import re
import nltk
import string
import unicodedata
import sys
importlib.reload(sys)

#------------------------------------------------
stopwords_nltk = nltk.corpus.stopwords.words('portuguese')
#--------------------------------------------------
#-------------------------------------------------
#removendo pontuações
#removendo stopwords com nltk
#removendo numeros
#-----------------------------------------------
def pre_processamento_texto(texto):
    #texto = str(texto)
    regex = re.compile('[%s]' % re.escape(string.punctuation))

    lista_de_palavras = []
    palavras = texto.split()
    for token in palavras:
        novo_token = regex.sub(u'',token)
        if not novo_token == u'':
            lista_de_palavras.append(novo_token)
    content = [w for w in lista_de_palavras if w.lower().strip() not in stopwords_nltk]

    texto_limpo = []
    for word in content:
        nfkd = unicodedata.normalize('NFKD', word)
        palavras_sem_acento = u''.join(c for c in nfkd if not unicodedata.combining(c))

        q = re.sub('[^a-zA-Z0-9 \\\]', ' ', palavras_sem_acento)

        texto_limpo.append(q.lower().strip())

    tokens = [t for t in texto_limpo if len(t)>2 and not t.isdigit()]
    result = ' '.join(tokens)

    return result