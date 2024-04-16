import torch
import torch.nn as nn
import pandas as pd
import numpy as np

class CNNmodel(nn.Module):
    def __init__(self):
        super(CNNmodel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=8, kernel_size=5, padding=2)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=8, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(in_channels=8, out_channels=5, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(5*24*24, 1)
        # self.relu = nn.ReLU(),
        # self.sig = nn.Sigmoid()
        
    def forward(self, x):
        x = self.conv1(x)
        x = nn.functional.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = nn.functional.relu(x)
        x = self.pool(x)
        
        x = x.view(-1, 5*24*24)
        x = self.fc1(x)
        # x = self.sig(x)
        x = nn.functional.sigmoid(x)
        return x