### Problem statement
The main goal of this project is to make a simple news keyword classifier. The classifier will be trained on a dataset of news articles and their respective keywords. The classifier will then be able to classify a news article into one or more keywords. The classifier will be used to classify news articles into keywords.


### Dataset
the dataset is made base on web scrapping from veriouse Bangli news websites . All those scraping notebook are in the folder "notebook_for_new_scraping" . 

preprocess data contain Title and content of the news article  also contain 9 label classes .Present classes are : 'ক্রেডিট রেটিং', 'পর্ষদ সভা', 'ইপিএস', 'প্রান্তিক প্রকাশ', 'পিই রেশিও', 'ডিভিডেন্ড', 'ব্লক মার্কেট', 'স্পট মার্কেট','লভ্যাংশ ঘোষণা'

['download the dataset']()


### Model 
model used : there lots of model used in this project . but models are selected based on accuracy and f1 score . Also this accouracy and f1 score are calculated by using cross validation and stratified k fold=10  . there was a thrashold of 0.8 for both accuracy and f1 score .Base of this (svm , decision tree, ada boost and gradient boost) are selected .Then hyperparameter tuning is done for these models .Maximum accuracy and f1 score is 0.85% is achived after making a voiting classification using those tuned models  .

we also train a bert model for this project . that model gives the best result of 0.97% . We used simpletransformers library for this . 



### training and testing 
traing tredisional models : 

1. create a conda environment 
   command : conda create -n name_of_env python=3.7
2. activate the environment
    command : conda activate name_of_env
3. install the requirements
    command : pip install -r requirements.txt
4. run Ml_model.ipynb file 

training bert model : 

1. create a conda environment 
   command : conda create -n name_of_env python=3.7
2. activate the environment
    command : conda activate name_of_env
3. install the requirements
    command : pip install -r requirements.txt
4. install simpletransformers library 
   conda install pytorch>=1.6 cudatoolkit=11.0 -c pytorch  [for gpu] 
   conda install pytorch cpuonly -c pytorch [for cpu]
5. run bert_multi_label_classification.ipynb file    



### Result 


   
