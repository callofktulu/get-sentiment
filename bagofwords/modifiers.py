import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class Modifiers:
    @staticmethod
    def turn_text_into_words(text):
        #return re.sub(r"[^\w]", " ", word_list).split()    
        return word_tokenize(text)
    @staticmethod
    def lowercase_and_cleanup(text):
        replace_no_space = re.compile(r"[.;:!\'?,\"()\[\]]")
        replace_with_space = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)")
        text = [replace_no_space.sub("", line.lower()) for line in text]
        text = [replace_with_space.sub("", line) for line in text]
        return text
    @staticmethod
    def remove_stop_words(corpus):
        english_stop_words = stopwords.words('english')
        removed_stop_words = []
        for review in corpus:
            removed_stop_words.append(' '.join([word for word in review.split()
                                                if word not in english_stop_words]))
        return removed_stop_words
    @staticmethod
    def stemmize(text):
        stemmer = PorterStemmer()
        return [' '.join([stemmer.stem(word) for word in text.split()])]
    @staticmethod
    def lemmatize(text):
        lemmatizer = WordNetLemmatizer()
        return [' '.join([lemmatizer.lemmatize(word) for word in text.split()])]
