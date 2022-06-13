import spacy
from typing import Tuple

def get_matches_number(doc_text:str, matcher:str)-> Tuple[int,str]:
    """Find sentences that match the criteria of the passive or active rule"""
    matches = 0
    example = None
    for sent in doc_text.sents:
        m = matcher(sent)
        if len(m) > 0:
            matches += 1
            if example is None:
                example = sent
    return matches, example

def get_number_sents(doc_text:str)-> int:
    """Calculate the total number of sentences for a file."""
    return len(list(doc_text.sents))

def get_percent(num:int, all:int) -> int:
    """Calculate the percentage  of the sentences that were classified as passive or active ones"""
    return int((num / all) * 100)


