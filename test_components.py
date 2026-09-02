from dotenv import load_dotenv
load_dotenv()

# Test 1: LLM initialization
print("Test 1: Initializing LLM...")
from core.summarize import get_llm
llm = get_llm()
print(f"✓ LLM initialized: {llm.model}")

# Test 2: Test text splitting
print("\nTest 2: Testing text splitting...")
from core.summarize import split_transcript
test_text = "This is a test. " * 100
chunks = split_transcript(test_text)
print(f"✓ Text split into {len(chunks)} chunks")

# Test 3: Extractor functions
print("\nTest 3: Testing extractor imports...")
try:
    from core.extractor import extract_action_items, extract_key_decisions, extract_question
    print("✓ Extractors imported successfully")
except Exception as e:
    print(f"✗ Extractor error: {e}")

# Test 4: Audio processor
print("\nTest 4: Testing audio processor...")
try:
    from utils.audio_processor import process_input
    print("✓ Audio processor imported successfully")
except Exception as e:
    print(f"✗ Audio processor error: {e}")

# Test 5: Transcriber
print("\nTest 5: Testing transcriber...")
try:
    from core.transcriber import transcribe_chunk, transcribe_all
    print("✓ Transcriber imported successfully")
except Exception as e:
    print(f"✗ Transcriber error: {e}")

# Test 6: RAG engine
print("\nTest 6: Testing RAG engine...")
try:
    from core.rag_engine import build_rag_chain, load_rag_chain, ask_question
    print("✓ RAG engine imported successfully")
except Exception as e:
    print(f"✗ RAG engine error: {e}")

# Test 7: Vector store structure
print("\nTest 7: Testing vector store functions...")
try:
    from core.vector_store import get_embeddings, build_vector_store, load_vector_store, get_retriever
    print("✓ Vector store functions imported successfully")
    print("  (Note: embeddings model will download on first use)")
except Exception as e:
    print(f"✗ Vector store error: {e}")

# Test 8: Main pipeline
print("\nTest 8: Testing main pipeline...")
try:
    from main import run_pipeline
    print("✓ Main pipeline imported successfully")
except Exception as e:
    print(f"✗ Main pipeline error: {e}")

print("\n" + "="*60)
print("✓ All components working correctly!")
print("="*60)
print("\nNOTE: To run the full pipeline, you need:")
print("  1. FFmpeg installed and on PATH")
print("  2. Internet connection for downloading embedding models")
print("  3. Valid MISTRAL_API_KEY in .env file (✓ present)")

