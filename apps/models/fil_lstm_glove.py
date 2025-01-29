import tensorflow as tf
from tensorflow.keras.regularizers import L2
from tensorflow.keras.layers import Dense, Dropout, LSTM, Bidirectional, Activation, Embedding
from tensorflow.keras import Model, Input, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import Dice
from tensorflow.keras.metrics import BinaryAccuracy, BinaryCrossentropy as bce_metric, F1Score, AUC, Precision, Recall
from tensorflow.keras.initializers import GlorotNormal, GlorotUniform
from tensorflow.keras.optimizers import Adam

import json


def init_embedding_layer(vocab_len, emb_dim, emb_matrix):
    """
    returns an embedding layer

    if emb_dim is provided and emb_matrix is not embedding layer will use
    specified embedding dimensions and the layers weights will be trainable
    """

    emb_layer_dim = emb_dim if emb_matrix == None else emb_matrix.shape[1]
    emb_layer_trainable = True if emb_matrix == None else False
    embedding_layer = Embedding(vocab_len, emb_layer_dim, trainable=emb_layer_trainable, name='embedding-layer')

    if not emb_matrix == None:
        embedding_layer.build((None,))
        embedding_layer.set_weights([emb_matrix])

    return embedding_layer


def load_lstm_model(input_shape, vocab_len, emb_dim=256, emb_matrix=None):
    """
    Define architecture of LSTM model then return for later training

    Takes in also the embedding layer with weights/coefficients set
    to the pre-trained GloVe embeddings
    """
    
    print(f'input shape: {input_shape}')
    model = Sequential(name='fil-name-gender-lstm')

    # shape will m x 4 since 4 is the maximum length of a name
    model.add(Input(shape=(input_shape, ), dtype='int64', name='input-layer'))

    # initialize embedding layer
    embedding_layer = init_embedding_layer(vocab_len, emb_dim=emb_dim, emb_matrix=emb_matrix)
    model.add(embedding_layer)

    # initialize lstm layers
    model.add(Bidirectional(LSTM(units=128, recurrent_dropout=0.2, return_sequences=False)))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.add(Activation(activation="sigmoid"))

    # compile model
    model.compile(
        loss=Dice(),
        optimizer=Adam(learning_rate=0.01),
        metrics=[bce_metric(), BinaryAccuracy(), Precision(), Recall(), F1Score(), AUC()]
    )

    return model