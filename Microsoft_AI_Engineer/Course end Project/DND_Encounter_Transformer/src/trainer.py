import torch
import torch.nn as nn

def train_model(model, train_inputs, train_labels, epochs=5, learning_rate=0.001):
    # Define loss function and optimizer
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        model.train()  # Set model to training mode

        # Forward pass
        outputs = model(train_inputs)
        loss = loss_fn(outputs, train_labels)

        # Accuracy calculation (for monitoring)
        predictions = torch.argmax(outputs, dim=1)
        accuracy = (predictions == train_labels).float().mean()

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(
            f"Epoch {epoch+1}/{epochs}," 
            f"Loss: {loss.item():.4f}, "
            f"Accuracy: {accuracy.item():.4f}")