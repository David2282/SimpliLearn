import torch
import torch.nn as nn

class TransformerClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, num_heads, hidden_dim, num_classes, max_length):
        super().__init__()

        # 1. Turns token ID's into vectors
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

        # 2. Give the model position awareness
        self.position_embedding = nn.Embedding(max_length, embedding_dim)

        # 3. Transformer encoder block will go here
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embedding_dim,
            nhead=num_heads,
            dim_feedforward=hidden_dim,
            batch_first=True

        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=1)

        # 4. Final classification layer
        self.classifier = nn.Linear(embedding_dim, num_classes)
    
    def forward(self, input_ids):
        # Token embeddings
        token_embeddings = self.embedding(input_ids)

        # Position indecies: 0, 1, 2, 3...
        sequence_length = input_ids.size(1)
        positions = torch.arange(sequence_length, device=input_ids.device)

        # Position embeddings
        position_embeddings = self.position_embedding(positions)

        # Combine token and position embeddings
        x = token_embeddings + position_embeddings

        # Pass through transformer encoder
        x = self.encoder(x)

        # Collapse token vectors into one sentence vector (e.g., by taking the mean)
        x = x.mean(dim=1)

        # Final classification scores
        logits = self.classifier(x)
        return logits
        