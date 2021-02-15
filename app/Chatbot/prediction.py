from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from keras.models import load_model
import numpy as np
import random
import pickle
import json
import os.path
from .utils import ChatbotHelper


class Chatbot:
    def __init__(self, name):
        self.name=name
        self.__intents=[]
        self.__tokenizer=None
        self.__model=None
        self.vocab_size=0
        self.max_lenght=15

        #init the model
        self.__load_data()
        self.__load_model()

    #load the saved trained model
    def __load_model(self):
        
        #load training params
        with open('./app/Chatbot/models/params.json', 'r') as f:
            params=json.load(f)
            self.max_lenght=params["MAX_LEN"]
            self.vocab_size=params["VOC_SIZE"]
            f.close()
        
        #load the tokenizer
        with open('./app/Chatbot/models/tokenizer.pickle', 'rb') as handle:
            self.__tokenizer = pickle.load(handle)
        
        #load the trained model
        self.__model = tf.keras.models.load_model('./app/Chatbot/models/chatbot_model.h5')

    #Function to load chat training data
    def __load_data(self):
        with open(os.path.dirname(__file__) + '/../Chatbot/data/training_data.json', 'r') as f:
            self.intents = json.load(f)
            f.close()
    
    def predict_response(self,message):
        if len(str(message)) > 1:
            #accepted predicted threshold
            threshold = 0.7
            sent = ChatbotHelper.clean_sentence(message)
            sequence = self.__tokenizer.texts_to_sequences([sent])
            padded_sequence = pad_sequences(sequence, maxlen=self.max_lenght)

            prediction = self.__model.predict(padded_sequence)[0]
    
            # if none of the categories has a categories has a probability > threshold
            # return default
            if prediction[np.argmax(prediction)] < threshold:
                body_intent = "no_answer"
                body_response = "Sorry, but I did not understand"
            else:
                intent = self.intents["intents"][np.argmax(prediction)]
                tag = intent["tag"]
                body_intent = tag
                body_response = random.choice(intent["responses"])

            

            return body_intent,body_response
        else:
            return "",""

    def get_response(self,intent):
        doc=[doc for doc in self.intents["intents"] if doc["tag"]==intent]
        return doc[0]["responses"][0]
    