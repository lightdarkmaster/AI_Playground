import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from transformers import AutoModelForCausalLM, AutoTokenizer

class LLMTrainingDataset(Dataset):
    def __init__(self, data, model_name):
        self.data = data
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        example = self.data[idx]
        input_ids = self.tokenizer.encode(example['input_text'], 
                                            add_special_tokens=True, 
                                            max_length=512, 
                                            padding='max_length', 
                                            truncation=True, 
                                            return_attention_mask=True, 
                                            return_tensors='pt')
        labels = torch.tensor(example['labels'])
        return input_ids, labels


def train(model, device, train_loader, optimizer, epoch):
    model.train()
    total_loss = 0
    for batch_idx, (input_ids, labels) in enumerate(train_loader):
        input_ids = input_ids.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()
        outputs = model(input_ids=input_ids, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print('Epoch {}: Loss = {:.4f}'.format(epoch, total_loss / len(train_loader)))
    
    
def train_lm(model, device, data, model_name, batch_size, epochs):
    dataset = LLMTrainingDataset(data, model_name)
    train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    optimizer = optim.Adam(model.parameters(), lr=1e-5)
    for epoch in range(epochs):
        train(model, device, train_loader, optimizer, epoch)
    print('Training complete')
    
def evaluate(model, device, data, model_name, batch_size):
    dataset = LLMTrainingDataset(data, model_name)
    eval_loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for batch_idx, (input_ids, labels) in enumerate(eval_loader):
            input_ids = input_ids.to(device)
            labels = labels.to(device)
            outputs = model(input_ids=input_ids, labels=labels)
            loss = outputs.loss
            total_loss += loss.item()
    avg_loss = total_loss / len(eval_loader)
    print('Evaluation loss = {:.4f}'.format(avg_loss))
    return avg_loss

