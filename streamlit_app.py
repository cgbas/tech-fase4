import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import urllib.request
import requests
from PIL import Image
from io import BytesIO

st.title('Variação do Preço por Barril do Petróleo Bruto Brent (FOB)')

# criar aba

st.sidebar.title('Menu')
st.sidebar.write('Selecione a opção desejada:')
option = st.sidebar.selectbox(
        '',
        ['Introdução', 'Método', 'Análise do Cenário', 'Modelo LSTM', 'Conclusão']
        )

multi = '''  
        Para executar o código localmente, você pode seguir os passos abaixo:

        0. Clone o repositório:  
        > git clone https://github.com/GustavoHenriqueDeCarvalho/tech-fase4.git
        1. Crie um ambiente virtual python:  
        > python -m venv myenv
        2. Ative o ambiente virtual:  
        > myenv\Scripts\activate
        3. Instale as bibliotecas necessárias:  
        > pip install -r requirements.txt
        4. Execute o código:  
        > streamlit run streamlit_app.py
'''
st.sidebar.markdown(multi)

# st.sidebar.markdown("*Streamlit* is **really** ***cool***.")
# st.sidebar.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
# st.sidebar.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


if option == 'Introdução':
        st.subheader('Introdução')
        multi = '''
                Você foi contratado(a) para uma consultoria, e seu trabalho envolve analisar os dados de preço do petróleo Brent, 
                 que pode ser encontrado no site do Ipea. Essa base de dados histórica envolve duas colunas: data e preço (em dólares).


                Um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo para gerar insights
                 relevantes para tomada de decisão. Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo.


                Este relatório tem como objetivo analisar o comportamento do preço do petróleo brent, a fim de gerar insights para tomadas de decisões
                  baseadas em dados e fornecer indicadores para um fácil acompanhamento. O preço do petróleo Brent, que é uma referência global para
                   o valor do petróleo, é determinado por uma combinação de fatores econômicos, políticos e ambientais. O Brent é extraído principalmente do Mar do Norte e serve como um benchmark para os contratos de petróleo negociados em mercados internacionais. 
                
                
                O preço do Brent é influenciado por eventos como conflitos geopolíticos, decisões da Organização dos Países Exportadores de Petróleo (OPEP),
                 mudanças na oferta e demanda global, flutuações cambiais e o crescimento ou desaceleração econômica mundial. Outros fatores,
                  como inovações tecnológicas na extração de petróleo e as políticas de transição para energias renováveis, também afetam o mercado do petróleo Brent.


                Durante crises globais, como a pandemia de COVID-19 ou tensões políticas em países produtores, o preço do Brent pode experimentar
                 volatilidade significativa. Por outro lado, períodos de estabilidade política e crescimento econômico geralmente resultam em preços mais equilibrados.


                As informações e análises apresentados dentro deste relatório apresentam dados fornecidos pelo site do ipeadata [Site - ipeadata](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) utilizamos informações do passado para entender os comportamentos e realizar previsão.'
                
                O Dashboard foi realizado utilizando o Power Bi da Microsoft onde foram realizados insights utilizando dados do inicio de 2000 até 2017. Para que seja compreendido utilizamos dados sobre demanda de energia, mortes por conflito armado e produção de petróleo.
                Clique [aqui](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) para acessar os dados do IPEA
                Clique [aqui](https://app.powerbi.com/view?r=eyJrIjoiNTg0ZDMyY2MtMzMwNi00ZDQ3LWEzY2EtMDVmZjYzZWZiYmQwIiwidCI6IjFjZTUxYjk4LWY4MmYtNGYxNy1iNDRmLTZlNzc0MDE5ZDBlOSIsImMiOjR9) para acessar o PowerBI
                Clique [aqui](https://colab.research.google.com/drive/1Gb3Ch5yoz9dnIax8BqqFZWWMX_2n6poR#scrollTo=X1RRCse9wRZI) para acessar o Machine Learning.
        '''

        st.markdown(multi)


elif option == 'Método':

        st.subheader('Método')
        st.write('Para a análise, utilizamos dados fornecidos pelo site do ipeadata, e através de ferramentas como o Python, foi montado um modelo de Machine Learning que realiza a previsão do preço do petróleo diariamente.')
        st.write('Ao utilizarmos destes modelos obtemos diversas vantagens como:')

        st.write('**Capacidade de Processar Grandes Volumes de Dados:** O Machine Learning pode analisar grandes quantidades de dados de maneira muito mais eficiente do que os métodos manuais ou tradicionais. Isso é essencial em um mundo cada vez mais orientado por dados, onde a quantidade e a complexidade das informações disponíveis aumentam constantemente.')
        st.write('**Capacidade de Aprendizado Automático:** Uma das principais vantagens do ML é que ele pode aprender automaticamente a partir de dados históricos sem a necessidade de programações manuais detalhadas. Isso permite que o modelo se adapte e melhore com o tempo, à medida que mais dados são disponibilizados.')
        st.write('**Automação e Eficiência:** O uso de ML para previsões reduz a necessidade de intervenção manual constante. Isso resulta em uma maior eficiência operacional, pois os modelos podem fazer previsões de forma autônoma, liberando os analistas para tarefas mais estratégicas.')
        st.write('**Análise em Tempo Real:** O ML é capaz de realizar previsões em tempo real ou quase em tempo real, o que é particularmente útil em áreas como o comércio eletrônico, a previsão do tempo, ou a análise de risco financeiro, onde decisões rápidas podem ser necessárias.')
elif option == 'Análise do Cenário':
        # create subheader
        st.subheader('Demanda de Energia')
        st.write('Nesse primeiro momento de exploração alteramos a medida de energia no DataSet em relação ao apresentado, pois o valor original de MWh onde havia países com valores superiores a trilhão, onde fizemos a transformação para GWh para um melhor entendimento. Gostaríamos de demonstrar  alguns pontos de demanda de energia do Paises em relação com sua população,  observamos as seguintes informações: ')
        #colocar graficos
        st.write('Se compararmos pela média da População mundial levando em conta os dados de 1950 até 2023 conseguimos observar que se não levarmos em conta a China que seria um dos países com maior quantidade de habitantes os países mais desenvolvidos ocupam a maior parte do topo do ranking de países com maiores demandas por energia. Isso nos mostra que densidade populacional não significa necessariamente mais custo com energia, um país que nos mostra isso seria o Brasil, que mesmo sendo um dos países com a maior média de população não chega a ser um dos dez maiores países com demanda de energia.')
        #colocar graficos
        st.write('Quando levantamos a produção do Óleo bruto conseguimos observar que os Estados Unidos tem uma alta demanda de energia e é um dos que mais o produz, com essa informação podemos supor com muita segurança que os Estados Unidos é um dos países que mais utilizam Petróleo para satisfazer sua demanda por energia. E ao pesquisarmos mais a fundo sobre o assunto conseguimos encontrar artigos do Governo brasileiro que confirmam que ele não é só um dos maiores consumidores como foi o maior consumidor nos anos de 2021 e 2022 ocupando a primeira posição.')
        st.subheader('Conflito Armado:')
        #colocar graficos
        # inserir imagem
        st.write('Infelizmente muitas são as causas que podem influenciar diretamente e indiretamente na produção e comercialização do óleo bruto, ao verificarmos o valor médio por ano conseguimos constatar que os anos que tiveram os maiores valores seriam entre os anos de 2011 a 2013, onde conseguimos identificar alguns dos conflitos que podem ter influenciado.')
        #colocar graficos
        st.write('Dentro desses anos gostaríamos de citar dois conflitos:')
        st.write('O conflito do Iraque (2011-2013) se instaurou logo após as tropas dos Estados Unidos se retirarem do território Iraquiano depois de 8 anos de guerra começaram várias revoltas da população local onde se desprendeu uma Guerra Civil que seguiu até meados de 2017. Além de ser o país com a maior quantidade de conflitos armados dentro do período citado, podemos observar a  grafico 3 e verificar que se trata de um dos 10 países que mais produzem petróleo no mundo.')
        st.write('A Guerra Civil na Líbia(2011) engloba a 16ª região que mais produzem petróleo conforme a Imagem 3, houve uma Guerra Civil entre as forças do governo regente de Muammar Gaddafi contra grupos revolucionistas populares que durou até meados do final do ano. Sendo a 9ª região com a maior média de mortos no período, de acordo com a Imagem 5 podemos citar como um dos possíveis motivos.')
        st.write('Houve outros conflitos na época como a Guerra Civil na Síria(2011) e o Conflito no Bahrein (2011-2014).')
        st.subheader('Referências Extras')
        st.write('U.S. ENERGY INFORMATION ADMINISTRATION. **Homepage**. United States: EIA,2024. Disponível em: [https://www.eia.gov](http://https://www.eia.gov). Acesso em:20 nov. 2024.')
elif option == 'Modelo LSTM':
        st.write('Machine Learning')
elif option == 'Conclusão':
        st.write('Conclusão')









