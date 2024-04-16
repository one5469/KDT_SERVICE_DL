import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from konlpy.tag import Okt

class SentenceClassifier(nn.Module):
    def __init__(
            self,
            n_vocab,
            hidden_dim,
            embedding_dim,
            n_class,
            n_layers,
            dropout=0.5,
            bidirectional=True,
            model_type='lstm'
    ):
        super().__init__()

        self.embedding = nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=embedding_dim,
            padding_idx=0
        )
        if model_type == 'rnn':
            self.model = nn.RNN(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectiional=bidirectional,
                dropout=dropout,
                batch_first=True
            )
        elif model_type == 'lstm':
            self.model = nn.LSTM(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True
            )

        if bidirectional:
            self.classifier = nn.Linear(hidden_dim*2, n_class)
        else:
            self.classifier = nn.Linear(hidden_dim, n_class)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        output, _ = self.model(embeddings)
        last_output = output[:, -1, :]
        last_output = self.dropout(last_output)
        logits = self.classifier(last_output)
        return logits

model = torch.load('./second_model.pth', map_location=torch.device('cpu'))
VOCAB = pd.read_csv('./VOCAB.csv').set_index('0').to_dict()["1"]
okt = Okt()
MAX_LENGTH = 55
encoder = {'두한': 0,
 '김영태': 1,
 '최동열': 2,
 '나레이션': 3,
 '유진산': 4,
 '조병옥': 5,
 '개코': 6,
 '신영균': 7,
 '문영철': 8,
 '정진영': 9,
 '이정재': 10,
 '김관철': 11,
 '이화룡': 12,
 '이승만': 13,
 '이기붕': 14,
 '시라소니': 15,
 '임화수': 16,
 '곽영주': 17,
 '눈물': 18,
 '김기홍': 19,
 '이석재': 20,
 '유지광': 21,
 '정대발': 22}
decoder = { v:k for k, v in encoder.items() }

# msg = input('대사를 입력하시게 : ')
msg = '누구인가 누가 기침소리를 내었어'

def modelPredict(msg):
    tokens = okt.morphs(msg)

    if len(tokens) > MAX_LENGTH:
        tokens = tokens[:MAX_LENGTH]
    else:
        while len(tokens) < MAX_LENGTH:
            tokens.append('<PAD>')

    for idx in range(len(tokens)):
        token = tokens[idx]
        try:      
            code = VOCAB[token]
        except KeyError:
            code = VOCAB['<UNK>']
        tokens[idx] = code

    # print(torch.tensor(tokens))
    # print(torch.tensor(tokens).shape)
    predict = model(torch.tensor(tokens).unsqueeze(dim=0))
    # print(predict)
    # print(predict.shape)
    code = predict.argmax(dim=1).item()

    print(code, decoder[code])