import hashlib
import os
from datetime import datetime

RAW_FILE = r"C:\Users\maged.ibrahim\Desktop\my\Me\Chat_001.txt"
CHUNKS_DIR = r"C:\Users\maged.ibrahim\.gemini\antigravity\brain\301cdd38-94a5-485d-a15d-5764291dec2e\scratch\chunks"
MANIFEST_FILE = r"C:\Users\maged.ibrahim\.gemini\antigravity\brain\301cdd38-94a5-485d-a15d-5764291dec2e\SOURCE_MANIFEST.md"

os.makedirs(CHUNKS_DIR, exist_ok=True)

def sha256_file(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def sha256_content(content):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(content.encode('utf-8'))
    return sha256_hash.hexdigest()

# 1. Stage -1: Immutable Ingestion
if not os.path.exists(RAW_FILE):
    print(f"Error: {RAW_FILE} not found.")
    exit(1)

raw_hash = sha256_file(RAW_FILE)

# 2. Stage 1: Deterministic Segmentation
with open(RAW_FILE, "r", encoding="utf-8", errors="replace") as f:
    text = f.read()

# Fallback chunking: Splitting by double newline (paragraph boundary)
paragraphs = text.split('\n\n')

chunks = []
current_chunk_text = ""
MAX_CHARS = 20000

for p in paragraphs:
    if len(current_chunk_text) + len(p) > MAX_CHARS and len(current_chunk_text) > 0:
        chunks.append(current_chunk_text.strip())
        current_chunk_text = p + "\n\n"
    else:
        current_chunk_text += p + "\n\n"

if current_chunk_text.strip():
    chunks.append(current_chunk_text.strip())

# Save chunks and generate Dual Hashes
manifest_lines = [
    "# SOURCE_MANIFEST (Stage -1 & 1)",
    f"**Date:** {datetime.utcnow().isoformat()}Z",
    f"**Protocol Version:** 2.3",
    f"**AI Model:** Antigravity",
    f"**Operator:** Maged (Steward)",
    f"**Raw File Source:** S001",
    f"**Raw File Path:** `{RAW_FILE}`",
    f"**Raw File Hash (SHA-256):** `{raw_hash}`",
    f"**Total Chunks:** {len(chunks)}",
    "",
    "## Dual Hash Ledger",
    "| Chunk ID | Chunk Filename | Chunk Hash (SHA-256) | Raw File Hash |",
    "| -------- | -------------- | -------------------- | ------------- |"
]

for i, chunk_content in enumerate(chunks):
    chunk_id = f"S001-C{i+1:03d}"
    chunk_filename = f"{chunk_id}.txt"
    chunk_path = os.path.join(CHUNKS_DIR, chunk_filename)
    
    with open(chunk_path, "w", encoding="utf-8") as f:
        f.write(chunk_content)
        
    chunk_hash = sha256_content(chunk_content)
    manifest_lines.append(f"| {chunk_id} | {chunk_filename} | `{chunk_hash}` | `{raw_hash}` |")

# Ensure artifact directory exists for manifest
os.makedirs(os.path.dirname(MANIFEST_FILE), exist_ok=True)
with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(manifest_lines))

print(f"Archivist Mode Complete. Generated {len(chunks)} chunks.")
print(f"Raw Hash: {raw_hash}")
print(f"Manifest written to {MANIFEST_FILE}")
