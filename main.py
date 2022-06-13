"""Identify sentences in active and passive voices, their number and percentage"""

from argparse import ArgumentParser
import spacy
from spacy.matcher import Matcher
from typing import Tuple

from number_percentage import get_matches_number,get_number_sents,get_percent

def load_file(filename:str) -> str:
    """Read a file to be analysed"""
    with open(filename, 'r') as f:
       return f.read()

def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Idendify sentences in active and passive voice")
    parser.add_argument('filename1', type=str, default=None, help="File_1 to be analysed.")
    parser.add_argument('filename2', type=str, default=None, help="File_2 to be analysed.")
    parser.add_argument('--en', action='store_const', const=True, default=False, help="English language")
    parser.add_argument('--de', action='store_const', const=True, default=False, help="German language")
    parser.add_argument('--examples', action='store_const', const=True, default=False, help="Examples")
    return parser

def find_in_file(lang:str, file_in:str)-> Tuple[int,int,int,str, str]:
    nlp = None
    #Load spacy and define the rule for passive and active voices for English and German
    if lang == "en":
        nlp = spacy.load('en_core_web_sm')
        passive_rule = [[{'LEMMA':'be'},{'TAG':'VBN'}],[{'LEMMA':'be'},{'TEXT':{'REGEX':'[A-Za-z]'},'OP':'*'},{'TAG':'VBN'}]]
        active_rule = [[{'DEP': {'IN': ['nsubj','csubj']}},{'TAG':{'IN':['VBD','VBP','VBZ','MD']}},{'TAG':'VB','OP':'*'}], [{'DEP': {'IN': ['nsubj']}},{'TAG':'HVS'},{'TAG':'VBN'}]]
    elif lang == "de":
        nlp = spacy.load('de_core_news_sm')
        passive_rule = [[{'LEMMA':'werden'},{'TEXT':{'REGEX':'[A-Za-z]'},'OP':'*'},{'TAG':'VVPP'}],[{'TAG':'VVPP'},{'LEMMA':'werden'}],[{'LEMMA':'sein'},{'TEXT':{'REGEX':'[A-Za-z]'},'OP':'*'},{'TAG':'VVPP'},{'TEXT':'worden'}]]
        active_rule = [[{'DEP': 'sb'},{'TEXT':{'REGEX':'[A-Za-z]'},'OP':'*'},{'TAG':'VVFIN'}],[{'TAG':'VVFIN'},{'DEP': 'sb'}],[{'DEP':'sb'},{'LEMMA':{'IN':['haben','sein']}},{'TEXT':{'REGEX':'[A-Za-z]'},'OP':'*'},{'TAG':'VVPP'}],[{'TAG':{'IN': ['VVFIN','VMFIN','VAFIN']}},{'TEXT':{'REGEX':'[A-Za-z]'},'OP':'*'},{'TAG':'VVINF'}]]
    
    #Matcher class object
    matcher_passive = Matcher(nlp.vocab)
    matcher_active = Matcher(nlp.vocab)
        
    matcher_passive.add('Passive', passive_rule)
    matcher_active.add('Active', active_rule)
    
    doc_text = nlp(load_file(file_in))
    name = file_in
    #Get total number of sentences in a file 
    number = get_number_sents(doc_text)
    #Sentences in passive
    passive, example_passive = get_matches_number(doc_text, matcher_passive)
    #Sentences in active
    active, example_active = get_matches_number(doc_text, matcher_active)
    
    return number, active, passive, example_active, example_passive


def main():
    #Parse command line arguments
    parser = get_argument_parser()
    args = parser.parse_args()

    if args.en:
        lang = "en"
    else:
        lang = "de"

    
    number, active, passive, example_active, example_passive = find_in_file(lang, args.filename1)
    print(f"Total number of sentences in \"{args.filename1}\": {number}")
    print(f"Sentences in passive: {passive}({get_percent(passive, number)}%)")
    print(f"Sentences in active: {active}({get_percent(active, number)}%)")
    #Show examples of sentences in active and passive voices for the first file
    if args.examples:
        print(f"Example passive: {example_passive}")
        print(f"Example active: {example_active}")
    print("*******************************************************************")

    number, active, passive, example_active, example_passive = find_in_file(lang, args.filename2)
    print(f"Total number of sentences in \"{args.filename2}\": {number}")
    print(f"Sentences in passive: {passive}({get_percent(passive, number)}%)")
    print(f"Sentences in active: {active}({get_percent(active, number)}%)")
    #Show examples of sentences in active and passive voices for the second file
    if args.examples:
        print(f"Example passive: {example_passive}")
        print(f"Example active: {example_active}")
    print("*******************************************************************")

    
if __name__ == '__main__':
    main()
