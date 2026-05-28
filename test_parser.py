import os
import sys
from app.services.parser import DocumentParser

def run_test(pdf_path: str):
    if not os.path.exists(pdf_path):
        print(f"Error: Target file '{pdf_path}' not found.")
        sys.exit(1)

    with open(pdf_path, "rb") as f:
        file_bytes = f.read()

    print("Initializing parser...")
    parser = DocumentParser(chunk_size=500, chunk_overlap=50)

    print(f"Extracting and chunking '{pdf_path}'...")
    chunks = parser.process_document(file_bytes)

    print(f"\n--- SUCCESS: Shipped {len(chunks)} chunks ---")
    for i, chunk in enumerate(chunks[:3]):  # Preview first 3 chunks
        print(f"\nChunk {i} | Page {chunk['page_number']} | Tokens {chunk['token_count']}")
        print("-" * 40)
        print(chunk['text_content'][:200] + "...\n")

if __name__ == "__main__":
    # Provide a sample PDF path here
    sample_pdf = "sample_contract.pdf" 
    run_test(sample_pdf)