# Identification of sentences in active and passive voices.

In my program I tried to compare the number of sentences written in passive with the ones in active voice in news articles and literature.These two genres of texts  were chosen because they are supposed to have relatively high percentage of sentences in passive. 

## Usage

Using text files "newsarticles_en.txt" and  "dune_en.txt" you can compare the number of sentences in passive and active voices for English. There is a flag "--en" which you have to choose in order to specify the language:

	§python3 main.py newsarticles_en.txt dune_en.txt --en

If you want to see an example for active and passive voice you can use an optional flag  "--examples" which will provide you with some sentences from the texts:

 	§python3 main.py newsarticles_en.txt dune_en.txt --en --examples

As for German, it is necessary to use other texts:"newsarticles_de.txt" and "die_verwandlung_de.txt"
Use the `--de` flag to specify this language:

    §python main.py newsarticles_de.txt die_verwandlung_de.txt --de

As it was mentioned before in order to see some example add the flag "--examples":

    §python main.py newsarticles_de.txt die_verwandlung.txt --de --examples


## Classification accuracy
To run the program that contains tests for the classification accuracy, it is necessary to write in the console(the texts for the tests "test_en.txt" and "test_de.txt" must be located in the same directory):

	§python3 test_number_percentage.py
  
### Packages
It is important to have installed spacy packages for English: 

`§python -m spacy download en_core_web_sm`

and for German:
`§python -m spacy download de_core_news_sm`





