from vllm import LLM, SamplingParams

class HospitalNarrator:

    def __init__(self):
        self.llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.2")

    def explain(self, state, risk):
        prompt = f"""
        Hospital State:
        ER={state['er']}, ICU={state['icu']}, General={state['general']}
        Surge Risk={risk}

        Explain hospital situation in simple terms for admin dashboard.
        """

        outputs = self.llm.generate([prompt], SamplingParams(max_tokens=80))
        return outputs[0].outputs[0].text
