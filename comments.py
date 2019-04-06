import sys, re
import numpy as np
import pandas as pd
import nltk #Natural lenguage tool kit
from nltk.corpus import stopwords #remove stop words
from nltk.stem.porter import PorterStemmer #stemming
from sklearn.feature_extraction.text import CountVectorizer #model of words
from sklearn.model_selection import train_test_split #split training set and test set
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


data = pd.read_csv(sys.argv[1], delimiter='\t', error_bad_lines=False)


# remover signos de puntuacion, numeros 
# tomar el root de la palabra fishing, finished = fish
# pasar todas las palablas a lowercase

# nltk.download('stopwords')

corpus = []

for i in range(0, 1000):  
    review = re.sub('[^a-zA-Z]', ' ', data['Review'][i])  
    review = review.lower()  
    review = review.split()  
     
    ps = PorterStemmer()  
           
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]  
    review = ' '.join(review)   
        
    corpus.append(review)  

cv = CountVectorizer(max_features=1500)

X = cv.fit_transform(corpus).toarray()
y = data.iloc[:,1].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25)

model = RandomForestClassifier(n_estimators= 501, criterion='entropy')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
# print(y_pred)

cm = confusion_matrix(y_test, y_pred)

print(cm)