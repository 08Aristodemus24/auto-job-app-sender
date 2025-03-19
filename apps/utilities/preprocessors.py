import re
import requests
import numpy as np
import pandas as pd
import tqdm
import tensorflow as tf

def preprocess(name: str):
    """
    preprocesses name in the profiles dataframe to remove uneccessary
    strings like CRSP, CHRA, RPm, non-alphanumeric characters, middle initials
    e.g. R., D.C., capitalizes first names middle names and last names,
    """
    temp = name

    # remove other non-alpha numeric chars
    temp = rem_nonalphanum(temp)
    # print(temp)

    # capitalize all strings in profile name
    temp = capitalize(temp)

    # partition full profile name
    temp = partition_full_name(temp)

    # remove all invalid words in partitioned profile names
    temp = filter_valid(temp)
    print(temp)

    return temp

def rem_nonalphanum(name: str):
    return re.sub(r"[^0-9a-zA-ZñÑ.\"]+", ' ', name)

def capitalize(name: str):
    return name.title()

def partition_full_name(name: str):
    """
    splits full linked in profile name into individual strings
    """

    return name.split()

def filter_valid(sequence: list):
    """
    a function that filters only valid names and
    joins only the words that is valid in the profile
    name e.g. ['Christian', 'Cachola', 'Chrp', 'Crsp']
    results only in Christian Cachola
    """

    # filter and remove the words in the sequence
    # included in list of words that are invalid
    filt_sequence = list(filter(lambda word: word not in [
        'Crsp', 
        'Rpm', 
        'Mapsy', 
        'Cssgb',
        'Chra',
        'Mba',
        'Es',
        'Csswb',
        'Cphr',
        'Clssyb',
        'Cssyb',
        'Mdrt',
        'Ceqp',
        'Msp',
        'Chrp'
        'Icyb'], sequence))
    
    # join the filtered words
    temp = " ".join(filt_sequence)

    return temp

def rem_mi(name: str):
    pass

def assign_gender(row, api_key):
    # extract gender if any
    gender = row['gender']
    print(gender)

    # check if null
    if pd.isnull(gender):
        name = row['conn_name']
        response = requests.post(f"https://genderapi.io/api/?key={api_key}&name={name}")
        headers = response.headers
        data = response.json()
        print(data)
        print(headers)
        # data = {}

        # if request gives a request limit reached error
        # thus returning a json without hte gender key, just
        # use an alternative return value of the null value 
        # of the empty cell
        return data.get('gender', gender)
    else:
        return row['gender']



def series_to_1D_array(series):
    """this converts the series or column of a df
    of lists 
    """

    return [item for sublist in series for item in sublist]

def map_value_to_index(unique_tokens: list, inverted=False):
    """
    returns a lookup table mapping each unique value to an integer. 
    This is akin to generating a word to index dictionary where each
    unique word based on their freqeuncy will be mapped from indeces
    1 to |V|.

    args:
        unique_tokens - 
        inverted - 
    """
    char_to_idx = tf.keras.layers.StringLookup(vocabulary=unique_tokens, mask_token=None)
    idx_to_char = tf.keras.layers.StringLookup(vocabulary=char_to_idx.get_vocabulary(), invert=True, mask_token=None)

    return char_to_idx if inverted == False else idx_to_char

def construct_embedding_dict(word_emb_path, word_to_index):
    """
    returns an embedding dictionary populated with all the words and
    their respective vector representations from the file of the 
    pretrained embeddings of GloVe 
    """

    embedding_dict = {}
    with open(word_emb_path, 'r') as file:
        for index, line in enumerate(file):
            # each line consists of: <word> <feature 1> <feature 2> ... <feature d>
            # where d is the 300th feature of the word embedding of that word
            values = line.split()

            # get the word
            word = values[0]

            # if such word exists in our tokenized dictionary
            # then if the reverse is the case that means that 
            # that word exists in the 1.9m word vocab of glove
            if word in word_to_index.keys():
                # get the vector
                vector = np.asarray(values[1:], 'float64')
                
                # build the key and value pair of this word and its vector representation
                embedding_dict[word] = vector
                
                # get embedding vector length which will be constant across all keys
                EMB_VEC_LEN = vector.shape[0]

        file.close()

    return embedding_dict, EMB_VEC_LEN



def construct_embedding_matrix(word_to_index, embedding_dict, EMB_VEC_LEN):
    """
    Constructs the embedding matrix upon finishing the phase of 
    constructing the embedding dictionary. So that reading the GloVe 
    embeddings is only done ones to increase time efficiency
    """

    # oov words (out of vacabulary words) will be mapped to 0 vectors
    # this is why we have a plus one always to the number of our words in 
    # our embedding matrix since that is reserved for an unknown or OOV word
    vocab_len = len(word_to_index) + 1

    # initialize it to 0
    embedding_matrix = np.zeros((vocab_len, EMB_VEC_LEN))

    for word, index in tqdm.tqdm(word_to_index.items()):
        # skip if, if index is already equal to the number of
        # words in our vocab. A break statement if you will
        if index < vocab_len:
            # if word does not exist in the pretrained word embedding itself
            # then return an empty array
            vector = embedding_dict.get(word, [])

            # if in cases vect is indeed otherwise an empty array due 
            # to the word existing in the pretrained word embeddings
            # then place it in our embedding matrix. Otherwise its index
            # where a word does not exist will stay a row of zeros
            if len(vector) > 0:
                embedding_matrix[index] = vector[:EMB_VEC_LEN]

    return embedding_matrix