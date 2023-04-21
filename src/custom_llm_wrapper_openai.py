from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import openai

class CustomLLM(LLM):
    
    open_apikey : str
    prompt :str
    
    @property
    def _llm_type(self) -> str:
        return "custom"
    
    def _call(self, message: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        
        #Updating the prompt
        self.prompt = self.prompt + message
        
        #Setting openai key
        openai.api_key = self.open_apikey
        
        #Set the model call parameters according to your need
        response = openai.Completion.create(
            engine="<Model Id for your finetuned model>",
            prompt=self.prompt,
            max_tokens=50,
            n=1,
            temperature=0.15,
            stop=['#']
        )
        return response.choices[0].text.replace("Child: ", "").replace("child: ", "")
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"n": self.n}

    
open_apikey = "<your openAI api key"
prompt = "<Prompt to the model>"

llm = CustomLLM(open_apikey=open_apikey,prompt=prompt)

llm("How are you?")