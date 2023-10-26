# import spacy for nlp
import spacy
# import glob in case user enters a file pattern
import glob
# import shutil in case user enters a compressed archive (.zip, .tar, .tgz etc.); this is more general than zipfile
import shutil
# import matplotlib for making graphs
import matplotlib.pyplot as plt
# import wordcloud for making wordclouds
import wordcloud
# import json
import json 
# import re
import re

def get_token_counts(corpus, tags_to_exclude = ['PUNCT', 'SPACE']):
    """Builds a token frequency table.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param tags_to_exclude: (Coarse-grained) part of speech tags to exclude from the results
    :type tags_to_exclude: list[string]
    :returns: a list of pairs (item, frequency)
    :rtype: list
    """
    # make an empty dictionary called token_counts
    token_counts = {}
    # YOUR CODE HERE

    # return the token counts as a list of pairs
    return list(token_counts.items())

def get_entity_counts(corpus, min_freq = 50, tags_to_exclude = ['QUANTITY']):
    """Builds an entity frequency table.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param tags_to_exclude: named entity labels to exclude from the results
    :type tags_to_exclude: list[string]
    :returns: a list of pairs (item, frequency)
    :rtype: list
    """
    # make an empty dictionary called entity_counts
    entity_counts = {}
    # YOUR CODE HERE

    # return the entity counts as a list of pairs
    return list(entity_counts.items())

def get_noun_chunk_counts(corpus, min_freq=5):
    """Builds a noun chunk frequency table.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :returns: a list of pairs (item, frequency)
    :rtype: list
    """
   # make an empty dictionary called chunk_counts
    chunk_counts = {}
    # YOUR CODE HERE

    # return the chunk counts as a list of pairs
    return list(chunk_counts.items())

def reduce_to_top_k(frequencies, top_k=25):
    """Gets the top k most frequent items.

    :param frequencies: a list of pairs (item, frequency)
    :type frequencies: list
    :param top_k: the number you want to keep
    :type top_k: int
    :returns: a list of the top k most frequent items
    :rtype: list
    """
    # sort the frequency table by frequency (least to most frequent) 
    frequencies = sorted(frequencies, key=lambda x: x[1])
    # return the top k of them
    return frequencies[-top_k:]

def load_textfile(file_name, corpus, nlp):
    """Loads a textfile into a corpus. Doesn't need to return corpus since a corpus once made can be modified as it moves around.

    :param file_name: the path to a text file
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    
    :type nlp: spaCy engine
     """
    # YOUR CODE HERE
    pass

    
def load_compressed(file_name, corpus, nlp):
    """Loads a zipfile into a corpus. Doesn't need to return corpus since a corpus once made can be modified as it moves around.

    :param file_name: the path to a zipfile
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
   """
    # YOUR CODE HERE
    pass

    
def load_jsonl(file_name, corpus, nlp):
    """Loads a jsonl file into a corpus. Doesn't need to return corpus since a corpus once made can be modified as it moves around.

    :param file_name: the path to a jsonl file
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
     """
    # YOUR CODE HERE
    pass

def build_corpus(pattern, corpus={}, nlp=spacy.load("en_core_web_sm")):
    """Builds a corpus from a pattern that matches one or more compressed or text files.

    :param pattern: the pattern to match to find files to add to the corpus
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
    :returns: a dictionary mapping document identifiers to document metadata and document NLP output
    :rtype: dict
     """
    # YOUR CODE HERE

    return corpus

def get_metadata_counts(corpus, metadata_key):
    """Gets frequency data for the values of a particular metadata key.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param metadata_key: a key in the metadata dictionary
    :type metadata_key: str
    :returns: a dictionary mapping values of the metadata key to their frequencies
    :rtype: dict
    """
    # make an empty dictionary called metadata_counts
    metadata_counts = {}
    # YOUR CODE HERE

    return list(metadata_counts.items())

def get_basic_statistics(corpus):
    """Prints summary statistics for the input corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # YOUR CODE HERE


def plot_counts(counts, file_name):
    """Makes a bar chart for counts.

    :param counts: a list of item, count tuples
    :type counts: list
    :param file_name: where to save the plot
    :type file_name: string
    """
    plt.barh([x[0] for x in counts], [x[1] for x in counts])
    plt.tight_layout()
    plt.savefig(file_name)
    plt.clf()

def plot_token_frequencies(corpus):
    """Makes a bar chart for the top k most frequent tokens in the corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # YOUR CODE HERE; call plot_counts!
    pass

def plot_entity_frequencies(corpus):
    """Makes a bar chart for the top k most frequent entities in the corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # YOUR CODE HERE; call plot_counts!
    pass
    
def plot_chunk_frequencies(corpus):
    """Makes a bar chart for the top k most frequent chunks in the corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # YOUR CODE HERE; call plot_counts!
    pass
   
def plot_metadata_frequencies(corpus, key):
    """Makes a bar chart for the frequencies of values of a metadata key in a corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param key: a metadata key
    :type key: str
    """
    # YOUR CODE HERE; call plot_counts!
    pass

def plot_word_cloud(counts, file_name):
    """Plots a word cloud.

    :param counts: a list of item, count tuples
    :type counts: list
    :param file_name: where to save the plot
    :type file_name: string
    """
    try:
        counts = [(x[0].strip(), x[1]) for x in counts]
        # make the word cloud
        wc = wordcloud.WordCloud(width=800, height=400, max_words=200).generate_from_frequencies(dict(counts))
        # plot the word cloud
        plt.figure(figsize=(10, 10))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(file_name)
        plt.clf()
    except Exception as e:
        print('Couldn\'t make wordcloud', file_name, e)

def plot_token_cloud(corpus):
    """Makes a word cloud for the frequencies of tokens in a corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # YOUR CODE HERE; call plot_word_cloud!
    pass

def plot_entity_cloud(corpus):
    """Makes a word cloud for the frequencies of tokens in a corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # YOUR CODE HERE; call plot_word_cloud!
    pass

def plot_chunk_cloud(corpus):
    """Makes a word cloud for the frequencies of tokens in a corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # YOUR CODE HERE; call plot_word_cloud!
    pass

def render_doc_markdown(file_name, doc):
    """Render a document as markdown. From project 2a. 

    :param file_name: the file name for the document
    :type corpus: str
    :param doc: the spaCy doc made from the text in the document
    :type doc: spacy doc
    """
    # define 'text' and set the title to be the document key (file name)
    text = '# ' + file_name + '\n\n'
    # walk over the tokens in the document
    for token in doc:
        # if the token is a noun, add it to 'text' and make it boldface (HTML: <b> at the start, </b> at the end)
        if token.pos_ == 'NOUN':
            text = text + '<b>' + token.text + '</b>'
        # otherwise, if it's a verb, add it to 'text' and make it italicized (HTML: <i> at the start, </i> at the end)
        elif token.pos_ == 'VERB':
            text = text + '</i>' + token.text + '<i>'
        # otherwise, just add it to 'text'!
        else:
            text = text + token.text
        # add any whitespace following the token using attribute whitespace_
        text = text + token.whitespace_
    # open an output file, named after the document with _text.md appended
    with open(file_name + '_text.md', 'w') as outf:
        # write 'text'
        outf.write(text)

def render_doc_table(file_name, doc):
    """Render a document's token and entity annotations as a table. From project 2a. 

    :param file_name: the file name for the document
    :type corpus: str
    :param doc: the spaCy doc made from the text in the document
    :type doc: spacy doc
    """
    # Make the tokens table
    tokens_table = "| Tokens | Lemmas | Coarse | Fine | Shapes | Morphology |\n| ------ | ------ | ------ | ---- | ------ | ---------- | \n"
    # walk over the tokens in the document
    for token in doc:
        # if the token's part of speech is not 'SPACE'
        if token.pos_ != 'SPACE':
            # add the the text, lemma, coarse- and fine-grained parts of speech, word shape and morphology for this token to `tokens_table`
            tokens_table  = tokens_table + "| " + token.text + " | " + token.lemma_ + " | " + token.pos_ + " | " + token.tag_ + " | " + token.shape_ + " | " + re.sub(r'\|', '#', str(token.morph)) + " |\n"
    # Make the entities table
    entities_table = "| Text | Type |\n| ---- | ---- |\n"
    # walk over the entities in the document
    for entity in doc.ents:
        # add the text and label for this entity to 'entities_table'
        entities_table = entities_table + "| " + entity.text + " | " + entity.label_ + " |\n"
    # open an output file, named after the document with _table.md appended
    with open(file_name + '_table.md', 'w') as outf:
        # write 'tokens_table'
        outf.write(tokens_table)
        outf.write('\n')
        # write 'entities_table'
        outf.write(entities_table)

def render_doc_statistics(file_name, doc):
    """Render a document's token and entity counts as a table. From project 2a. 

    :param file_name: the file name for the document
    :type corpus: str
    :param doc: the spaCy doc made from the text in the document
    :type doc: spacy doc
    """
    # make a dictionary for the statistics
    stats = {}
    # walk over the tokens in the document
    for token in doc:
        # if the token's part of speech is not 'SPACE'
        if token.pos_ != 'SPACE':
            # add the token and its part of speech tag ('pos_') to 'stats' (check if it is in 'stats' first!)
            if token.text + token.pos_ not in stats:
                stats[token.text + token.pos_] = 0
            # increment its count
            stats[token.text + token.pos_] = stats[token.text + token.pos_] + 1
    # walk over the entities in the document
    for entity in doc.ents:
        # add the entity and its label ('label_') to 'stat's (check if it is in 'stat's first!)
        if entity.text + entity.label_ not in stats:
            stats[entity.text + entity.label_] = 0
        # increment its count
        stats[entity.text + entity.label_] = stats[entity.text + entity.label_] + 1
    # open an output file, named after the document with _stats.md appended
    with open(file_name + '_stats.md', 'w') as outf:
        # write the header for a table of tokens/entities and counts
        outf.write('| Token/Entity | Count |\n | ------------ | ----- |\n')
        # print the key and count for each entry in 'stats'
        for key in sorted(stats.keys()):
            outf.write('| ' + key + ' | ' + str(stats[key]) + ' |\n')

def main():
    """The main function. 
      First we ask the user for a pattern. 
      Then, we build a corpus. 
      Then, we let the user choose whether they want corpus statistics, plots of corpus wordcounts, or a wordcloud for the corpus.
    """
    # ask the user to input a zip file, jsonl file or pattern
    pattern = str(input("Please input a pattern:\n"))
    print(f'Loading %s, this may take awhile!' % pattern)
    # build the corpus from the pattern (instead of None)
    corpus = build_corpus(pattern)
    # keep going til the user quits with Ctrl-C
    while True:
        goal_type = ''
        # until the goal_type is 'corpus' or 'doc'
        while goal_type not in ['corpus', 'doc']:
            goal_type = input('Please choose \'corpus\' or \'doc\':  ')
        # set the goal to something that doesn't exist
        goal = ''
        if goal_type == 'corpus':
            # until the goal is 'statistics', 'wordcount' or 'wordcloud'
            while goal not in ['statistics', 'count', 'cloud']:
                # ask the user for a value for 'goal' from 'statistics', 'count' or 'cloud'
                goal = input('Type \'statistics\' if you want basic corpus statistics, \'count\' if you want token and entity counts, \'cloud\' if you want a wordcloud:  ')
                # if the goal is 'statistics'
                if goal == 'statistics': # get basic corpus statistics
                    get_basic_statistics(corpus)
                elif goal == 'count': # plot token, entity and chunk counts as well as publication year and page count plots
                    plot_token_frequencies(corpus)
                    plot_entity_frequencies(corpus)
                    plot_chunk_frequencies(corpus)
                    plot_metadata_frequencies(corpus, 'publicationYear')
                    plot_metadata_frequencies(corpus, 'pageCount')
                elif goal == 'cloud': # make token, entity and chunk wordclouds
                    plot_token_cloud(corpus)
                    plot_chunk_cloud(corpus)
                    plot_entity_cloud(corpus)
        else: # goal_type is 'doc'
            doc_id = ''
            while doc_id not in corpus:
                doc_id = input('Choose a document id from ' + str(corpus.keys()) + ':  ')
            while goal not in ['markdown', 'table', 'statistics']:
                goal = input('Type \'statistics\' if you want basic document statistics, \'markdown\' if you want markdown, \'table\' if you want a table:  ')
                # if the goal is 'statistics'
                if goal == 'statistics': # get basic corpus statistics
                    render_doc_statistics(doc_id, corpus[doc_id]['doc'])
                elif goal == 'markdown': # plot token, entity and chunk counts as well as publication year and page count plots
                    render_doc_markdown(doc_id, corpus[doc_id]['doc'])
                elif goal == 'table': # make token, entity and chunk wordclouds
                    render_doc_table(doc_id, corpus[doc_id]['doc'])

# this says, if executing this on the command line like python spacy-on-corpus.py, run main()    
if __name__ == "__main__":
    main()