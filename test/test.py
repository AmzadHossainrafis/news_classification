import pytest 
import os
import pandas as pd
from project.config import *
from project.utils import * 


@pytest.fixture
def data():
    # Load data for testing from csv file
    read_data = pd.read_csv(list_dir['all_news_dir'])
    # random 40 data for testing
    read_data = read_data.sample(n=40) 
    return read_data


def test_preprocess_news(data):
    # read data 
    read_data = data 




