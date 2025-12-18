import random

def encrypt_text(text):
    if not text:
        return None, None

    key_shift = random.randint(1, 100)
    key_seed = random.randint(1, 10000)
    
    keys = {'shift': key_shift, 'seed': key_seed}

    layer1 = [ord(char) + key_shift for char in text]

    rng = random.Random(key_seed)
    
    indices = list(range(len(layer1)))
    rng.shuffle(indices)
    
    layer2 = [layer1[i] for i in indices]

    layer3 = [255 - val for val in layer2]

    ciphertext = " ".join(hex(x) for x in layer3)
    
    return ciphertext, keys

def decrypt_text(ciphertext, keys):
    if not ciphertext or not keys:
        return "Error: Missing data"

    try:
        encrypted_vals = [int(x, 16) for x in ciphertext.split()]
        
        key_shift = keys['shift']
        key_seed = keys['seed']

        layer2_reversed = [255 - val for val in encrypted_vals]

        rng = random.Random(key_seed)
        
        indices = list(range(len(layer2_reversed)))
        rng.shuffle(indices)
        
        layer1_reversed = [0] * len(layer2_reversed)
        for i, original_index in enumerate(indices):
            layer1_reversed[original_index] = layer2_reversed[i]

        plaintext = "".join(chr(val - key_shift) for val in layer1_reversed)

        return plaintext

    except Exception as e:
        return f"Decryption Failed: {e}"
