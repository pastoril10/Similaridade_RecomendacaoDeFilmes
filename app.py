import pickle
import streamlit as st
import pandas as pd
import requests


def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3b2638f12b86999283cf393efba3c112&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def sistema_recomendacao(movie):
    index = filmes[filmes["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse = True, key=lambda x: x[1])
    names = []
    poster = []
    
    for i in distances[1:6]:
        movie_id = filmes.iloc[i[0]].id
        poster.append(get_poster(movie_id))
        names.append(filmes.iloc[i[0]].title)

    return names, poster

st.header("Sistema de Recomendação de Filmes")
dict_filmes = pickle.load(open("models/lista_filmes.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))
filmes = pd.DataFrame(dict_filmes)


movie_list = filmes["title"].values
select_movies = st.selectbox("Selecionando Filme", movie_list)

##Criando botão de recomendação
if st.button("Mostrar Recomendação"):
    names, poster = sistema_recomendacao(select_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])