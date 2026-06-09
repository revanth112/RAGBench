from vectordb.registry import (
    VECTOR_STORES
)


class VectorService:

    @staticmethod
    def get_store(
        vector_db
    ):

        return VECTOR_STORES[
            vector_db
        ]