import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab') 
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')   

text = "I hope you are doing well. I came across the Intern AI & MarTech (Growth) role at Groww and wanted to reach out personally as the role strongly aligns with the kind of work I do."


# Tokenization 
sentences = sent_tokenize(text)
print(sentences)

# word tokenization
words = word_tokenize(text)
print("Word Tokens:")
print(words)

# Stop words removable
stop_words = set(stopwords.words('english'))

filtered_words = [word for word in words if word.lower() not in stop_words]

print("\nAfter Stopword Removal:")
print(filtered_words)


# Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]

print("\nStemmed Words:")
print(stemmed_words)


# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nLemmatized Words:")
print(lemmatized_words)