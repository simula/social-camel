# social-camel

This is an extension of the example from https://python.langchain.com/en/latest/use_cases/agents/camel_role_playing.html which allows to sandbox two agents
that can give each others intructions to solve a task. 

CAMEL Role-Playing Autonomous Cooperative Agents#
This is a langchain implementation of paper: “CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society”.
Overview:
The rapid advancement of conversational and chat-based language models has led to remarkable progress in complex task-solving. However, their success heavily relies on human input to guide the conversation, which can be challenging and time-consuming. This paper explores the potential of building scalable techniques to facilitate autonomous cooperation among communicative agents and provide insight into their “cognitive” processes. To address the challenges of achieving autonomous cooperation, we propose a novel communicative agent framework named role-playing. Our approach involves using inception prompting to guide chat agents toward task completion while maintaining consistency with human intentions. We showcase how role-playing can be used to generate conversational data for studying the behaviors and capabilities of chat agents, providing a valuable resource for investigating conversational language models. Our contributions include introducing a novel communicative agent framework, offering a scalable approach for studying the cooperative behaviors and capabilities of multi-agent systems, and open-sourcing our library to support research on communicative agents and beyond.
The original implementation: https://github.com/lightaime/camel
Project website: https://www.camel-ai.org/
Arxiv paper: https://arxiv.org/abs/2303.17760

In social-camel two agents discuss a common topic where each of the agents has a different perspective. For example a student and a teacher discussing why 2 and 2 is 4 
where the stuents perspective is that they do not understand this and the teacher has a good understanding and explains it.

This allows for several interesting use cases such as exploring conversations between a doctor or a patient, etc. 

