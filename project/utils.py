
import re
import numpy as np
from config import pre_process_config

def bert_label_maker(targets):
    list1=[]
    col_list=[]
    for j in range(len(targets)):
        for i in targets.loc[j]:
            list1.append(i)
        col_list.append(list1)
        list1=[]
    return col_list

def preprocess_news(news,main_stopwords=pre_process_config.main_stopwords):
    main_stopwords =main_stopwords.split(" ")
    news = remove_numbers(news)
    news = remove_extra_spaces(news)
    news = remove_english_words(news)
    news = remove_stopwords(news,main_stopwords)
    news = remove_perenthesis(news)
    news = remove_prone(news)
    news = remove_symbols(news)
    news = remove_dash(news)
    news = remove_3rdbreket(news)
    return news





#remove numbers
def remove_numbers(text):
    text = re.sub(r'\d+', '', text)
    return text

#remove extra spaces
def remove_extra_spaces(text):
    text = re.sub(r'\s+', ' ', text)
    return text

#remove english words
def remove_english_words(text):
    text = re.sub(r'[a-zA-Z]', '', text)
    return text

#remove stopwords
def remove_stopwords(text,main_stopwords):
    text = ' '.join([word for word in text.split() if word not in main_stopwords])
    return text

#remove all perenthesis 
def remove_perenthesis(text):
    text = re.sub(r'\([^)]*\)', '', text)
    return text

#remove all -pron-
def remove_prone(text):
    text = re.sub(r'-pron-', '', text)
    return text

#remove symbols
def remove_symbols(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text

def remove_dash(text):
    text = re.sub(r'--', '', text)
    return text


def remove_3rdbreket(text):
    text = text.replace(']', '').replace('[', '').replace("'", "").replace('(', '').replace(')', '').replace('/', '')
    return text


def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std()) 


def voting_with_model(model_list, X_test):
    '''
    This function takes a list of models and makes predictions on the test set. 
    It then takes the average of the predictions and returns the index of the highest probability. 
    '''
    y_pred = []
    for model in model_list:
        y_pred.append(model.predict(X_test))
    y_pred = np.array(y_pred)
    y_pred = np.mean(y_pred, axis=0)
    
    # y_pred = np.argmax(y_pred, axis=1)
    return y_pred

