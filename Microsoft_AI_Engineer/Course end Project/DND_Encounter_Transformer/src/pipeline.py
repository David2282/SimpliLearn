from src.preprocessor import load_data, preprocess_data
from src.tokenizer import build_vocab, encode_texts, pad_sequences
import torch
from src.model import TransformerClassifier
from src.trainer import train_model

# Full Procesess: Load data, preprocess, build vocab, encode, pad sequences, and print results


def run_pipeline():
    
    train_df, test_df = load_data()
 
    X_train, y_train, X_test, y_test = preprocess_data(train_df, test_df)

    vocab = build_vocab(X_train)
    encoded_train = encode_texts(X_train, vocab)
    encoded_test = encode_texts(X_test, vocab)
    max_length = max(max(len(seq) for seq in encoded_train), max(len(seq) for seq in encoded_test))

    padded_train = pad_sequences(encoded_train, max_length)
    padded_test = pad_sequences(encoded_test, max_length)
    input_tensor = torch.tensor(padded_train, dtype=torch.long)
    train_inputs = torch.tensor(padded_train, dtype=torch.long)
    train_labels = torch.tensor(y_train.values, dtype=torch.long)
    
    print("Vocab size:", len(vocab))
    print("Max Token ID:", train_inputs.max().item())
    print("Min Token ID:", train_inputs.min().item())
    
    model = TransformerClassifier(
        vocab_size=len(vocab),
        embedding_dim=64,
        num_heads=4,
        hidden_dim=256,
        num_classes=len(set(y_train)),
        max_length=max_length
    )

    sample_batch = input_tensor[:8]

    outputs = model(sample_batch)

   

    train_model(
        model = model,
        train_inputs = train_inputs,
        train_labels = train_labels,
        epochs = 5,
        learning_rate = 0.001
    )

    print("Data loaded and preprocessed successfully.")
    print("Train rows:", len(X_train))
    print("Test rows:", len(X_test))
    
    print("Max length:", max_length)
    print("First padded sample:", padded_train[0])
    print("First label:", y_train.iloc[0])
    print("Model output shape:", outputs.shape)
    print("Model output sample:", outputs[:2])
    print("Train Inputs shape:", train_inputs.shape)
    print("Train Labels shape:", train_labels.shape)

if __name__ == "__main__":
    run_pipeline()