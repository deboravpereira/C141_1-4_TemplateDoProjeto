from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


bright_stars_url = 'https://pt.wikipedia.org/wiki/Lista_das_estrelas_mais_brilhantes'

#Acesse o conteúdo da página através de page
page = requests.get(bright_stars_url)

#Use o interpretador BS4
soup = bs(page.text,'html.parser')

#Encontre a tabela de classe 'wikitable'


#Crie uma lista temporária vazia, onde você vai armazenar os dados buscados
temp_list= []

#Encontre as linhas da tabela


#Use um laço for para extrair os dados da lista e adicione os dados a lista temporária


#Listas que irão armazenar dados do dataframe
Star_names = []
Constelation = []
Magnitude_Ap = []
Bayer = []
Classification_esp = []
Distance =[]

#Adicione os dados a suas respectivas listas
for i in range(1,len(temp_list)):
    ##Adicione aqui seu código

#Cabeçalho do dataframe
headers = ['Nome da estrela', 'Constelação', 'Magnitude Ap.', 'Bayer', 'Classificação','Distância']

#Crie o Dataframe
df1 = pd.DataFrame()
print(df1)

df1.to_csv('estrelas_mais_brilhantes.csv')



