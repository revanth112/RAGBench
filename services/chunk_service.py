import uuid
from models.chunk import Chunk
from chunkers.registry import CHUNKERS
print(f"Available chunking strategies: {list(CHUNKERS.keys())}")
class ChunkService:

    @staticmethod
    def create_chunks(document,session_id,chunking_strategy):
        print(f"Creating chunks using strategy: {chunking_strategy}")
        
        chunker = CHUNKERS[chunking_strategy]
        print(chunker)
        print(f"Using chunking strategy: {chunking_strategy}")
        print("Chunking document...")

        raw_chunks = chunker.chunk(document.raw_text)
        print(f"Document chunked into {len(raw_chunks)} raw chunks")
        chunks = []

        for idx, chunk_text in enumerate(raw_chunks):

            chunk = Chunk(
                chunk_id=str(uuid.uuid4()),
                session_id=session_id,
                document_name=document.document_name,
                page_number=0,
                chunk_number=idx + 1,
                chunking_strategy=chunking_strategy,
                text=chunk_text
            )

            chunks.append(chunk)
        
        return chunks