from retrieval.retriever import Retriever

from retrieval.metadata_filter import MetadataFilter

from retrieval.citation_builder import CitationBuilder

from retrieval.context_builder import ContextBuilder


class RetrievalService:

    @staticmethod
    def retrieve_context(
        query,
        vector_store,
        embedding_model,
        k=5,
        document_name=None,
        page_number=None
    ):

        retriever = Retriever(
            vector_store,
            embedding_model
        )

        chunks = retriever.retrieve(
            query=query,
            k=k
        )

        chunks = MetadataFilter.apply(
            chunks,
            document_name=document_name,
            page_number=page_number
        )

        citations = (
            CitationBuilder.build(
                chunks
            )
        )

        context = (
            ContextBuilder.build(
                chunks
            )
        )

        return {
            "chunks": chunks,
            "citations": citations,
            "context": context
        }