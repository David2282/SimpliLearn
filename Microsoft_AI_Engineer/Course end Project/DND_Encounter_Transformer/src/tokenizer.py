
def tokenize(text):
    text = text.lower()
    text = text.strip()
    return text.split()


def build_vocab(texts):
    vocab = {}
    for text in texts:
        tokens = tokenize(text)
        
        for token in tokens:
            if token not in vocab:
                vocab[token] = len(vocab)

    return vocab


def encode_text(text, vocab):
    tokens = tokenize(text)
    return [vocab.get(token, 0) for token in tokens]


def encode_texts(texts, vocab):
    return [encode_text(text, vocab) for text in texts]


def pad_sequences(sequences, max_length):
    padded_sequences = []
    for seq in sequences:
        if len(seq) < max_length:
            padded_seq = seq + [0] * (max_length - len(seq))
        else:
            padded_seq = seq[:max_length]
        padded_sequences.append(padded_seq)
    return padded_sequences


#Unit test for tokenize function

# if __name__ == "__main__":
#     sample_texts = [
#         "A group of 3 Goblins confronts a party",
#         "A group of 1 Dragon confronts a party"
#     ]

#     vocab = build_vocab(sample_texts)
#     encoded = encode_texts(sample_texts, vocab)

#     max_length = max(len(seq) for seq in encoded)
#     padded = pad_sequences(encoded, max_length)

#     print(vocab)
#     print(encoded)
#     print(padded)