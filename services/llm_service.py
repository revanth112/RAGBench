from llms.registry import LLMS


class LLMService:

    @staticmethod
    def generate_answer(
        prompt,
        llm_name
    ):

        llm = LLMS[
            llm_name
        ]

        return llm.generate(
            prompt
        )