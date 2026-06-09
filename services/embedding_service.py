# from embeddings.registry import EMBEDDERS

# class EmbeddingService:

#     @staticmethod
#     def generate_embeddings(chunks,embedding_model):
#         embedder = EMBEDDERS[embedding_model]

#         vectors = embedder.embed(chunks)

#         return vectors

from embeddings.registry import EMBEDDERS


class EmbeddingService:

    @staticmethod
    def generate_embeddings(
        chunks,
        embedding_model
    ):

        embedder = EMBEDDERS[
            embedding_model
        ]

        return embedder.embed(
            chunks
        )

    @staticmethod
    def generate_query_embedding(
        text,
        embedding_model
    ):

        embedder = EMBEDDERS[
            embedding_model
        ]

        return embedder.embed_query(
            text
        )