# category

from sklearn.feature_extraction.text import CountVectorizer

corpus = ["Authman ran faster than Harry because he is an athlete.",
          "Authman and Harry ran faster and faster."]
          
bow = CountVectorizer() 

X = bow.fit_transform(corpus) # Sparse Matrix

print(bow.get_feature_names())

print(X.toarray())

