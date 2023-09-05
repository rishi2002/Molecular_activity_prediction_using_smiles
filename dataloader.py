from torch.utils.data import Dataset, DataLoader
import numpy as np
import torch

class smilesDataset(Dataset):
    def __init__(self, smiles_list, metadata): 
        self.smiles_list = smiles_list
        self.metadata = metadata
    def __len__(self): 
        return len(self.smiles_list)
    def __getitem__(self, idx):
        features = torch.tensor(self.smiles_list[idx], dtype=torch.float32)        
        AlogP = float(self.metadata['AlogP'].iloc[idx])
        Std_val = float(self.metadata['Standard Value'].iloc[idx])        
        labels = torch.tensor([Std_val, AlogP], dtype=torch.float32)
        return features, labels

    
class LR_Dataset(Dataset):
    def __init__(self, smiles_list, metadata): 
        self.smiles_list = smiles_list
        self.metadata = metadata
    def __len__(self): 
        return len(self.smiles_list)
    def __getitem__(self, idx):
        features = torch.tensor(self.smiles_list[idx], dtype=torch.float32).view(-1)
        AlogP = float(self.metadata['AlogP'].iloc[idx])
        Std_val = float(self.metadata['Standard Value'].iloc[idx])        
        labels = torch.tensor([Std_val, AlogP], dtype=torch.float32)
        return features, labels