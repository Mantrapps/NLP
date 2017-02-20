# HomeWork-1 cs6322 Nature Language Processing
# Kai Zhu
# kxz160030@utdallas.edu


import nltk
import re
import os
import pandas as pd
from string import punctuation
import glob
import math
from nltk.stem import WordNetLemmatizer


class util:
    def __init___(self):
        pass

    #without smoothing
    def bigramTableCorpus(self,T):
        # generate token table with term as key
        bTable=dict();
        for index,value in enumerate(T):
            if value not in bTable:
                bTable[value] = [1, dict()]
            else:
                bTable[value][0] += 1
            if index<len(T)-1:
                if T[index+1] not in bTable[value][1]:
                    bTable[value][1][T[index+1]]=1
                else:
                    bTable[value][1][T[index + 1]] += 1;
        return bTable

    def bigramTable(self,t, corpus):
        # generate token table with term as key
        bTable=list();
        for term1 in t:
            curr=[]
            if term1 in corpus:
                for term2 in t:
                    if term2 in corpus[term1][1]:
                        curr.append(corpus[term1][1][term2])
                    else:
                        curr.append(0)
            else:
                print "not exist"
            bTable.append(curr)
        print pd.DataFrame(bTable,index=t,columns=t)

    #with add-one smoothing
    def bigramTableWithSmoothing(self,t, corpus):
        # generate token table with term as key
        bTable = list();
        for term1 in t:
            curr = []
            if term1 in corpus:
                for term2 in t:
                    if term2 in corpus[term1][1]:
                        curr.append(corpus[term1][1][term2]+1)
                    else:
                        curr.append(1)
            else:
                print "not exist"
            bTable.append(curr)
        print pd.DataFrame(bTable, index=t, columns=t)

    #with Good-Turing smoothing
    def bigramTableWithGoodTuringSmoothing(self,t, corpus):
        pass

    def tokenize(self, text):
        text = re.sub(r'([:,])([^\d])', r' \1 \2', text)
        text = ' '.join(filter(None, (word.strip(punctuation) for word in text.split())))
        text = re.sub((r'[\]\[\(\)\{\}\<\>]'), r" ", text)
        text = re.sub((r"([^' ])('[sS]|'[mM]|'[dD]|') "), r"\1 \2 ", text)
        text = re.sub((r"([^' ])('ll|'re|'ve|n't) "), r"\1 \2 ", text)
        text = re.sub((r"[-_]"), " ", text)
        text = re.sub("$\d+\W+|\b\d+\b|\W+\d+$", " ", text)
        return text.split()

    def readFile(self, file):
        file_table = []
        obj = open(file)
        lines =obj.readlines()
        for x in lines:
            if x.rstrip() is not '':
                file_table +=self.tokenize(x.rstrip().lower())
        # Create your bigrams
        return self.bigramTableCorpus(file_table)

    def readSentence(self, s):
        return self.tokenize(s.rstrip().lower())

    #t: list of word with sequence
    def bigramProbabilities(self,t,corpus):
        # generate token table with term as key
        bTable = list();
        for term1 in t:
            curr = []
            if term1 in corpus:
                for term2 in t:
                    if term2 in corpus[term1][1]:
                        curr.append(0 if float(corpus[term1][1][term2])/corpus[term1][0]==float(0) else float(corpus[term1][1][term2])/corpus[term1][0])
                    else:
                        curr.append(0)
            else:
                print "not exist"
            bTable.append(curr)
        print pd.DataFrame(bTable, index=t, columns=t)

    def bigramProbabilitiesWithSmoothing(self,t,corpus):
        # generate token table with term as key
        v=len(corpus)
        bTable = list();
        for term1 in t:
            curr = []
            if term1 in corpus:
                for term2 in t:
                    if term2 in corpus[term1][1]:
                        curr.append(float((corpus[term1][1][term2]+1))/(corpus[term1][0]+v))
                    else:
                        curr.append(float(1)/(corpus[term1][0]+v))
            else:
                print "not exist"
            bTable.append(curr)
        print pd.DataFrame(bTable, index=t, columns=t)

    def bigramProbabilitiesWithGoodTuringSmoothing(self,t,corpus):
        pass


    #print
    def output(self):
        pass


#tokenize the data from the file
def tokenize(input):
    pass

#compute bigram count
def bigramCount():
    pass


def main():
    #input s1
    s1="The chief executive said that the company 's profit was going down last year."
    #input s2
    s2="The president said the revenue was good last year."

    utl=util()
    cwd = os.getcwd()
    corpus = cwd + "/Corpus.txt"
    bigramTableCorpus=utl.readFile(corpus)
    bigramTableS1=utl.readSentence(s1)
    bigramTableS2=utl.readSentence(s2)

    # Table with bigram count

    utl.bigramTable(bigramTableS1,bigramTableCorpus)
    utl.bigramTable(bigramTableS2,bigramTableCorpus)
    utl.bigramTableWithSmoothing(bigramTableS1, bigramTableCorpus)
    utl.bigramTableWithSmoothing(bigramTableS2, bigramTableCorpus)
    utl.bigramTableWithGoodTuringSmoothing(bigramTableS1, bigramTableCorpus)
    utl.bigramTableWithGoodTuringSmoothing(bigramTableS2, bigramTableCorpus)

    # Table with bigram probabilities
    utl.bigramProbabilities(bigramTableS1,bigramTableCorpus)
    utl.bigramProbabilities(bigramTableS2, bigramTableCorpus)
    utl.bigramProbabilitiesWithSmoothing(bigramTableS1, bigramTableCorpus)
    utl.bigramProbabilitiesWithSmoothing(bigramTableS2, bigramTableCorpus)
    utl.bigramProbabilitiesWithGoodTuringSmoothing(bigramTableS1, bigramTableCorpus)
    utl.bigramProbabilitiesWithGoodTuringSmoothing(bigramTableS2, bigramTableCorpus)


    # Total probabilities



if __name__ == '__main__':
   main()
