from matplotlib import pyplot

import json
import os.path
import tensorflow as tf
import numpy as np
import random
import sys
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import layers

import pickle
from .utils import ChatbotHelper


class Chatbot:

    def __init__(self, num_epochs):

        self.intents = []
        self.intent_list = []
        self.label_list = []
        self.padded_vectors = []
        self.labels_vectors = []
        self.vocab_size = 0
        self.max_lenght = 10
        self.num_categories = 0
        self.num_epochs = num_epochs
        self.history = None

        # it will be added to word_index and used to replace out-of-vocabulary words
        # during text_to_sequence calls
        self._oov_tok = "<OOV>"
        # Initiate the tokenizer with Out Of Vocabulary intent, any word not in vocabulary list will represented as oov,
        # also delete all punctuation !"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n
        self._tokenizer = Tokenizer(oov_token=self._oov_tok)

    # Function to load chat training data

    def __load_data(self):
        with open(os.path.dirname(__file__) + '/../Chatbot/data/training_data.json', 'r') as f:
            self.intents = json.load(f)
            f.close()

    # function to build the vocabularies dictionary and the vectors of words
    def __build_WordsBag(self):
        # load training data
        self.__load_data()
        # Gather and Tokenize Intents, Labels to One-Hot presentation
        # build the sentences list with related tag
        for index, intent in enumerate(self.intents['intents']):
            self.intent_list += intent["patterns"]
            num_patterns = len(intent["patterns"])
            # Get the label for each sentece as number, if there are 5 patterns, all pattern will have the same tag (same number)
            self.label_list += [index] * num_patterns

        # clean sentences in intent list
        self.intent_list = [ChatbotHelper.clean_sentence(
            s) for s in self.intent_list]

        # build the dictionary word_index, give each word an index based on word frequency,
        # the lower index means high freuency, the blood in our example appears 18 times, so it takes the index=2
        self._tokenizer.fit_on_texts(self.intent_list)
        word_index = self._tokenizer.word_index

        # convert each sentence into vector of their vocabs index in word_index
        sequences = self._tokenizer.texts_to_sequences(self.intent_list)

        # Get the max length sentence, because we have to know the input length of seq-to-seq encoder
        #self.max_length = len(max(sequences, key=len))
        self.vocab_size = len(word_index)
        # This will make all sequences vectors with the same length
        # example hi there will be represented as [36,24], after padding the vector length should be the same as max_length [0,0,.....,36,24]
        self.padded_vectors = pad_sequences(sequences, maxlen=self.max_lenght)
        #self.padded_length = len(self.padded_vectors[0])

        # convert labels to vectors
        self.labels_vectors = tf.keras.utils.to_categorical(
            self.label_list, dtype=int)
        self.num_categories = len(self.labels_vectors[0])

    # Create the model

    def __create_model(self):
        # Embeding Layers: convert each index (word) into vector of 16 number
        # https://www.youtube.com/watch?v=TsXR7_vtusQ

        # private instance model
        self.__model = tf.keras.Sequential(
            [
                layers.Embedding(self.vocab_size + 1, 16, input_length=self.max_lenght),
                layers.Flatten(),
                layers.Dense(128, activation="relu"),
                layers.Dropout(0.5),
                layers.Dense(64, activation="relu"),
                layers.Dropout(0.5),
                layers.Dense(self.num_categories, activation="softmax"),
            ]
        )

        # compile the model
        self.__model.compile(loss="categorical_crossentropy",
                             optimizer="adam", metrics=["accuracy"])

        # fit the model
        self.history = self.__model.fit(
            self.padded_vectors, self.labels_vectors, epochs=self.num_epochs, verbose=1)

        # Evaluate the model
        #self.scores = self.__model.evaluate(self.padded_vectors, self.labels_vectors, verbose=1)

        # Save the model to loaded later, by using this method,
        # you don't need to re-compile the model when loaded it later
        self.__model.save("./app/Chatbot/models/chatbot_model.h5")

        # to save the fitted tokenizer
        with open('./app/Chatbot/models/tokenizer.pickle', 'wb') as handle:
            pickle.dump(self._tokenizer, handle,
                        protocol=pickle.HIGHEST_PROTOCOL)

        params = {
            'VOC_SIZE': self.vocab_size,
            'MAX_LEN': self.max_lenght
        }

        with open('./app/Chatbot/models/params.json', 'w') as json_file:
            json.dump(params, json_file)

    def plot(self):
        if self.history is not None:
            pyplot.plot(
                self.history.history['accuracy'], label='train', scaley=False)
            pyplot.legend()
            pyplot.show()
        else:
            print("you must train the bot first")

    def train(self):
        self.__build_WordsBag()
        self.__create_model()
        print("Training done")
