from nltk import tokenize

def sent_tokenizer(paragraph):
    sentences = tokenize.sent_tokenize(paragraph)
    return sentences