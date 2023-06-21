import torch
from transformers import AutoTokenizer, AutoModel

from sklearn.feature_extraction.text import TfidfVectorizer


class W2V_PHOBERT:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
        self.model = AutoModel.from_pretrained("vinai/phobert-base", output_hidden_states=True)

    def t2v(self, text):
        # tokenize
        tokenized = self.tokenizer.encode(text)

        # convert to tensor
        tokens_tensor = torch.tensor([tokenized])

        # get last layer hidden states
        with torch.no_grad():
            outputs = self.model(tokens_tensor)
            hidden_states = outputs[2]

        # get last layer
        last_layer = hidden_states[-1][0]

        # get vector
        vec = torch.mean(last_layer, dim=0)
        vec = vec.numpy().reshape(1, -1)

        return vec
    
class W2V_TFIDF:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def t2v(self, documents):
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        return tfidf_matrix.toarray()