from chunkers.base import BaseChunker

class SemanticChunker(BaseChunker):

    def chunk(self, text: str):

        paragraphs = text.split("\n\n")

        return [
            p.strip()
            for p in paragraphs
            if p.strip()
        ]