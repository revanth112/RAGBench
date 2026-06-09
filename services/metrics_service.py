from config.model_costs import MODEL_COSTS

class MetricsService:
    @staticmethod
    def calculate_cost(llm_name,prompt_tokens,completion_tokens):

        pricing = MODEL_COSTS[llm_name]

        input_cost = (prompt_tokens / 1000) * pricing["input"]

        output_cost = (completion_tokens / 1000) * pricing["output"]

        return round(input_cost + output_cost,6)