from typing import List
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    BaseMessage,
)


class Agent:
    def __init__(
        self, system_message: BaseMessage, model: ChatOpenAI, name: str
    ) -> None:
        self.system_message = system_message
        self.model = model
        self.name = name
        self.init_messages()

    def reset(self) -> None:
        self.init_messages()

    def init_messages(self) -> None:
        self.stored_messages = [self.system_message]

    def update_messages(self, message: BaseMessage) -> List[BaseMessage]:
        self.stored_messages.append(message)
        return self.stored_messages

    def step(self, input_message: HumanMessage) -> AIMessage:
        messages = self.update_messages(input_message)
        output_message = self.model(messages)
        self.update_messages(output_message)
        return output_message


class Simulation:
    def __init__(
        self,
        agents: List[Agent]
    ) -> None:
        self.agents = agents

    def run_simulation(self, chat_turn_limit: int = 30) -> None:
        self.reset_agents()
        msg = self.agents[0].system_message
        n = 0
        while n < chat_turn_limit:
            n += 1
            for agent in self.agents:
                msg = HumanMessage(content=agent.step(msg).content)
                print(f"{agent.name}: {msg.content}\n")

    def reset_agents(self) -> None:
        for agent in self.agents:
            agent.reset()


def create_agents(task: str, temperature: float = 0.2) -> List[Agent]:
    teacher_system_message = SystemMessage(
        content=f"""Never forget you are a Teacher and I am a Student. Never flip roles!
        We share a common interest in having a conversation.
        You must help me to keep the conversation going.
        Here is the topic of our conversation: {task} and my perspective I am a very smart math teacher. Never forget our topic!

        You can ask and answer questions depending on the context of the conversation."""
    )

    student_system_message = SystemMessage(
        content=f"""Never forget you are a Student and I am a Teacher. Never flip roles!.
        We share a common interest in having a conversation.
        I must help you to keep the conversation going.
        Here is the topic of our conversation: {task} and my perspective I am a very dumb student who has problems to understand simple arithmatic. Never forget our topic!

        I can ask and answer questions depending on the context of the conversation."""
    )

    return [
        Agent(teacher_system_message, ChatOpenAI(temperature=temperature), "Teacher"),
        Agent(student_system_message, ChatOpenAI(temperature=temperature), "Student"),
    ]


def main() -> None:
    task = "Make the student understand why 2 + 2 equals 4"
    agents = create_agents(task)

    simulation = Simulation(agents)
    simulation.run_simulation()


if __name__ == "__main__":
    main()
