import os
from tqdm import tqdm
from itertools import combinations
from constants import safe_result

def list_files_in_folder(folder_path: str):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

def get_wordlists(path: str):
    with open(path, 'r') as file:
        file_contents = file.read()
        return file_contents

def computing_length(input):
    r = 0
    for i in input:
        r += sum(1 for _ in combinations(range(len(i)), 2))
    return r

def has_meaning_partly(inp: dict):
    file_paths = list_files_in_folder('./src/wordlists')
    text = inp['ciphertext']['text']
    method = inp['method']
    for i in file_paths:
        wordlist = get_wordlists(i).lower().split()
        r = []
        combination_bar = tqdm(total=computing_length(text), desc=f"Processing combinations --> {method}", leave=False)
        for tx in text:
            tx = tx.lower()
            for x, y in combinations(range(len(tx)), 2):
                part_word = tx[x:y]
                if part_word in wordlist and len(part_word) > 3:
                    r.append((True, part_word, i, tx))
                combination_bar.update(1)
            
            if len(r) >= len(tx) / safe_result:
                combination_bar.close()
                return {'valid': True, 'values': r, 'method': method}
        combination_bar.close()
    return {'valid': False, 'values': r, 'method': method}
