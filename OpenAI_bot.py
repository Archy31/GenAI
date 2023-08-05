from langchain import ConversationChain, OpenAI, PromptTemplate, LLMChain
from langchain.memory import ConversationBufferWindowMemory


class ChatBot:
    def __init__(self, lang_lvl: str, input_txt: str) -> None:
        self.lang_lvl = lang_lvl
        self.input_txt = input_txt

        self.OPENAI_KEY = "" # Here must be ChatGPT API token.

        self.templates = """
                Assistant is a large language model trained by OpenAI.

                {history}
                Human: {human_input}
                Assistant:
            """

def messager(self) -> None:
        prompt = PromptTemplate(input_variables=["history", "human_input"], template=self.template)

        chatgpt_chain = LLMChain(
            llm=OpenAI(openai_api_key=self.OPENAI_KEY, temperature=0),
            prompt=prompt,
            verbose=True,
            memory=ConversationBufferWindowMemory(k=2, ai_prefix='BOT'),)
        # Predict a sentence using the chatgpt chain

        output = chatgpt_chain.predict(
            human_input=f"""
                    Please replace complex words 
                    by simple ones for user's level which he selected prevoiusly, 
                    think step by step. Which complex words did you replace in this text? Please send them
                    My language level = {self.lang_level}.
                    '{self.input_text}'            

                """)

        return output

    
