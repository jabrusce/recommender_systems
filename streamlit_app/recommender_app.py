import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import en_core_web_lg
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_distances, cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import time
import os
from os import listdir

#Headers
st.header('What should I check out next?')
st.subheader("Choose a category from below:")

#Choose Media
books_box = st.checkbox('Recommend some books')
games_box = st.checkbox('Recommend some board games')

if books_box:
    rec_df = pd.read_pickle('./data/books.pk1')
    user_input = st.selectbox('What\'s a recent book you enjoyed', rec_df)
    def book_recommender(user_input):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i + 1)
        return 1- rec_df[user_input].sort_values()[1:6]
    st.subheader("Other books you may enjoy include:")
    book_recomendations = book_recommender(user_input)
    book_recomendations.index[0]
    book_recomendations.index[1]
    book_recomendations.index[2]
    book_recomendations.index[3]
    book_recomendations.index[4]

if games_box:
    rec_df = pd.read_pickle('./data/games.pk1')
    user_input = st.selectbox('What\'s a recent board game you enjoyed', rec_df)
    user_input_minplayers = st.slider("How many players?", min_value=0, max_value = 20, value = 0)
    user_input_playingtime = st.slider("How much time do you have to play?", min_value=0, max_value = 22500, value = 22500)
    def game_recommender(user_input):
        rec_df2 = rec_df[rec_df['average_rating'] >= 7.5]
        rec_df3 = rec_df2[rec_df2['minplayers'] >= user_input_minplayers]
        rec_df4 = rec_df3[rec_df3['playingtime'] <= user_input_playingtime]
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i + 1)
        return 1- rec_df4[user_input].sort_values()[1:6]
    st.subheader("Other games you may enjoy include:")
    game_recomendations = game_recommender(user_input)
    game_recomendations.index[0]
    game_recomendations.index[1]
    game_recomendations.index[2]
    game_recomendations.index[3]
    game_recomendations.index[4]