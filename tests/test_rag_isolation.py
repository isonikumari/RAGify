from core.vector_store import build_vector_store


def test_transcripts_are_isolated_in_vector_store():
    transcript_one = "Alice: Hello everyone. Bob: We will launch next Monday."
    transcript_two = "Carol: The budget is 50000 dollars."

    store_one = build_vector_store(transcript_one)
    store_two = build_vector_store(transcript_two)

    docs_one = "\n".join(store_one.get(include=["documents"])["documents"])
    docs_two = "\n".join(store_two.get(include=["documents"])["documents"])

    assert "launch next monday" in docs_one.lower()
    assert "budget is 50000 dollars" in docs_two.lower()
    assert "launch next monday" not in docs_two.lower()
