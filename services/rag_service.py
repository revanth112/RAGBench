from services.retrieval_service import RetrievalService

from services.llm_service import LLMService

from retrieval.prompt_builder import PromptBuilder
import time

class RAGService:

    @staticmethod
    def ask(query,vector_store,embedding_model,llm_name,k=5):

        retrieval_result = (
            RetrievalService.retrieve_context(
                query=query,
                vector_store=vector_store,
                embedding_model=embedding_model,k=k
            )
        )

        prompt = (
            PromptBuilder.build(
                query=query,
                context=retrieval_result["context"]
            )
        )

        answer = (
            LLMService.generate_answer(
                prompt,
                llm_name
            )
        )

        # return {

        #     "answer": answer,
        #     "citations":
        #         retrieval_result[
        #             "citations"
        #         ],
        #     "context":
        #         retrieval_result[
        #             "context"
        #         ]
        # }
        return {

            "run_id": "...",

            "answer": answer,

            "citations":
                retrieval_result[
                    "citations"
                ],
            "context":
                retrieval_result[
                    "context"
                ],
            "chunks": 
                retrieval_result[
                    "chunks"
                ],
            "latency": ...,

            "prompt_tokens": ...,

            "completion_tokens": ...,

            "total_tokens": ...,

            "cost": ...,

            "faithfulness": ...,

            "answer_relevancy": ...
        }