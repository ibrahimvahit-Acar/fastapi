from bs4 import BeautifulSoup
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.tokenizers import Tokenizer   
from sumy.parsers.plaintext import PlaintextParser
from nltk.tokenize import sent_tokenize
import spacy
import pytextrank
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk


#Algorithms
def luhn(metin, cumle_sayisi=3):
    ozet_luhn = LuhnSummarizer()
    parser = PlaintextParser.from_string(metin, Tokenizer("turkish"))
    b = str(metin).split(".")
    ozet = ozet_luhn(parser.document, cumle_sayisi)
    a = ""
    for cumle in ozet:
        a = a + str(cumle)
    return a

def lex_rank(metin, cumle_sayisi=3):
    ozet_lex = LexRankSummarizer()
    parser = PlaintextParser.from_string(metin, Tokenizer("turkish"))
    ozet = ozet_lex(parser.document, cumle_sayisi)
    a = ""
    for cumle in ozet:
        a = a + str(cumle)
    return a

def lsa_summary(metin, cumle_sayisi=3):
    ozet_lsa = LsaSummarizer()
    parser = PlaintextParser.from_string(metin, Tokenizer("turkish"))
    ozet = ozet_lsa(parser.document, cumle_sayisi)
    lsa_summary = ""
    for sentence in ozet:
        lsa_summary += str(sentence)
    return lsa_summary



def giso(metin):
    splitted_sentences = str(metin).split(".")
    if len(splitted_sentences) >= 5 and len(splitted_sentences) <= 7:
        return str(splitted_sentences[0:2] + splitted_sentences[-1:-3]).replace("[,", "").replace("['", "").replace(
            "]", "").replace("[", "").strip("'").strip("',").replace("',", ".").replace("'", "").strip('"') + "."
    if len(splitted_sentences) >= 8 and len(splitted_sentences) <= 12:
        return str(splitted_sentences[0:3] + splitted_sentences[-1:-4]).replace("[,", "").replace("['", "").replace(
            "]", "").replace("[", "").strip("'").strip("',").replace("',", ".").replace("'", "").strip('"') + "."
    if len(splitted_sentences) >= 13:
        return str(splitted_sentences[0:4] + splitted_sentences[-1:-5]).replace("[,", "").replace("['", "").replace(
            "]", "").replace("[", "").strip("'").strip("',").replace("',", ".").replace("'", "").strip('"') + "."
    else:
        return metin
