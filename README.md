# social-camel

In social-camel two agents discuss a common topic where each of the agents has a different perspective. For example a student and a teacher discussing why 2 and 2 is 4 where the stuents perspective is that they do not understand this and the teacher has a good understanding and explains it. This allows for several interesting use cases such as exploring conversations between a doctor or a patient, etc. 

social-camel is an extension of the example from https://python.langchain.com/en/latest/use_cases/agents/camel_role_playing.html. The ogirinal CAMEL allows to sandbox two agents that can give each others intructions to solve a task. 

## Wrapper for fine tunded openai model
We also provide and example for a wrapper that allows to use fine tuned models (custom_llm_wrapper_openai.py). This can be specifically interesting if one of the conversation participants is an expert in a specific field represented by a fine-tuned mode. 

## Original CAMEL Role-Playing Autonomous Cooperative Agents implementation

Langchain implementation: https://python.langchain.com/en/latest/use_cases/agents/camel_role_playing.html. <br />
The original implementation: https://github.com/lightaime/camel. <br />
Project website: https://www.camel-ai.org/. <br />
Arxiv paper: https://arxiv.org/abs/2303.17760. <br />




