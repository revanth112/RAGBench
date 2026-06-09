from chunkers.recursive import RecursiveChunker
from chunkers.semantic import SemanticChunker

CHUNKERS = {
    "recursive": RecursiveChunker(),
    "semantic": SemanticChunker()
}