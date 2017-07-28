from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger
from nltk.corpus import treebank
import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet


# function that takes file name returns the file content
def read_file(fileName):
    input_file = open(fileName,'r')
    return input_file.read()

# function split into sentence takes input from read_file() func
def sent_split(input_file):
    sentence = read_file(input_file)
    return sent_tokenize(sentence)

# function that prints all required given output
def get_contents(setence_input):
    tokenize_word = word_tokenize(setence_input)
    unigrm_object = UnigramTagger(treebank.tagged_sents(), backoff= DefaultTagger("RB"))
    tagged_words = unigrm_object.tag(tokenize_word)
    print("Nouns: " + ", ".join([word[0] for word in tagged_words if re.match('N', str(word[1]))]))
    print("Verbs: " + ", ".join([word[0] for word in tagged_words if re.match('V', str(word[1]))]))
    print("Adjectives: " + ", ".join([word[0] for word in tagged_words if re.match('J', str(word[1]))]))
    print("Adverbs: " + ", ".join([word[0] for word in tagged_words if re.match('R', str(word[1]))]))
    print("Stopwords: " + ", ".join([word[0] for word in tagged_words if word[0] in set(stopwords.words('english'))]))
    print("synonym of adjectives words: " + ", ".join([", ".join(wordnet.synsets(word[0])[0].lemma_names()) for word in tagged_words if re.match('J', str(word[1]))]))
    print("antonym of adjectives words: " + ", ".join([wordnet.synsets(word[0])[0].lemmas() [0].antonyms()[0].name() for word in tagged_words if re.match('J', str(word[1]))]))
    print("Entities: " + ", ".join([word[0] for word in tagged_words if re.match('NNP', str(word[1]))]))








if __name__ == "__main__":
    #calling sent_split() func to create object contain splitted setences
    splited_sentences = sent_split("input_file.txt")
    #going loop for each sentence in corpus
    for each_sentence in splited_sentences:
            get_contents(each_sentence)



