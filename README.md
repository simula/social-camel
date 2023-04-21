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

## Example
Example output where a teacher is trying to explain why 2 + 2 = 4 to a student.
```
Teacher: Great, let's get started! So, as a math teacher, I can explain why 2 + 2 equals 4. Would you like me to start with a basic explanation or a more advanced one?

Student: As a very dumb student, I would appreciate it if you could start with a basic explanation.

Teacher: Of course, I'm happy to help! So, when we say "2 + 2", we're essentially asking how many things we have when we combine two groups of two things each.

So, if we have two apples and we add two more apples, we end up with four apples in total. The same goes for any other objects or numbers.

Does that make sense so far?

Student: Yes, I understand the concept of combining two groups of two things to get four things in total. But why does it work that way? Why does 2 + 2 always equal 4?
```
