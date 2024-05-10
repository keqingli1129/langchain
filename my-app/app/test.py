class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

import torch

def train(self, model, train_loader, criterion, optimizer, device):
    """
    Trains the model using the given parameters.

    Parameters:
    model (torch.nn.Module): The model to train.
    train_loader (torch.utils.data.DataLoader): The DataLoader for the training data.
    criterion (torch.nn.Module): The loss function.
    optimizer (torch.optim.Optimizer): The optimizer.
    device (torch.device): The device to run the training on (e.g., 'cpu', 'cuda').

    Returns:
    tuple: The loss and accuracy for the epoch, respectively.
    """
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    
    for data, target in train_loader:
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item() * data.size(0)
        _, predicted = torch.max(output.data, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()
        
    epoch_loss = running_loss / len(train_loader.dataset)
    epoch_acc = 100 * correct / total
    return epoch_loss, epoch_acc
