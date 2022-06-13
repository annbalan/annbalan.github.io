"""Identify the accuracy of the classification into sentences in active and passive voices."""


import spacy
from spacy.matcher import Matcher

from number_percentage import get_matches_number,get_number_sents,get_percent
from main import find_in_file

def main():
    en_filename = "test_en.txt"
    #manually counted sentences
    en_sent_correct = 102
    en_pass_correct = 45
    en_act_correct = 57
    
    #sentences counted by the program
    number, active, passive, example_active, example_passive = find_in_file("en", en_filename)
    en_sent_found = number
    en_act_found = active
    en_pass_found = passive
    
    en_sent_accuracy = int(en_sent_found/en_sent_correct*100)
    en_act_accuracy = int(en_act_found/en_act_correct*100)
    en_pass_accuracy = int(en_pass_found/en_pass_correct*100)
    print(f"Total number of sentences in \"{en_filename}\": {en_sent_correct}, number of sentences found: {en_sent_found}. Accuracy:{en_sent_accuracy}%\n")
    print(f"Total number of sentences in passive: {en_pass_correct}, number of sentences found in passive: {en_pass_found}. Accuracy:{en_pass_accuracy}%")
    print(f"Example of passive voice: {example_passive}\n")
    print(f"Total number of sentences in active: {en_act_correct}, number of sentences found in active: {en_act_found}. Accuracy:{en_act_accuracy}%")
    print(f"Example of active voice: {example_active}\n")

    print(f"*****      *****       *****      *****       *****      *****      *****       *****\n")

    
    de_filename = "test_de.txt"
    #manually counted sentences
    de_sent_correct = 137
    de_pass_correct = 72
    de_act_correct = 65

    #sentences counted by the program
    number, active, passive, example_active, example_passive = find_in_file("de", de_filename)
    de_sent_found = number
    de_act_found = active
    de_pass_found = passive
    
    de_sent_accuracy = int(de_sent_found/de_sent_correct*100)
    de_act_accuracy = int(de_act_found/de_act_correct*100)
    de_pass_accuracy = int(de_pass_found/de_pass_correct*100)
    print(f"Total number of sentences in \"{de_filename}\": {de_sent_correct}, number of sentences found: {de_sent_found}. Accuracy:{de_sent_accuracy}%\n")
    print(f"Total number of sentences in passive: {de_pass_correct}, number of sentences found in passive: {de_pass_found}. Accuracy:{de_pass_accuracy}%")
    print(f"Example of passive voice: {example_passive}\n")
    print(f"Total number of sentences in active: {de_act_correct}, number of sentences found in active: {de_act_found}. Accuracy:{de_act_accuracy}%")
    print(f"Example of active voice: {example_active}\n")

if __name__ == '__main__':
    main()


