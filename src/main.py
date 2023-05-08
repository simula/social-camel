import argparse
import json
from typing import List
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    BaseMessage,
)


class Memory:
    def __init__(self) -> None:
        self.memory = []

    def store(self, item):
        self.memory.append(item)

    def get_memory(self):
        return SystemMessage(
            content=".".join([memory.content for memory in self.memory])
        )


class Agent:
    def __init__(
        self,
        system_message: BaseMessage,
        model: ChatOpenAI,
        name: str,
        memory: Memory = None,
    ) -> None:
        self.system_message = system_message
        self.model = model
        self.name = name
        self.memory = memory
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
        self.memory.store(output_message)
        return output_message


class Simulation:
    def __init__(self, agents: List[Agent], observer: Agent = None) -> None:
        self.agents = agents
        self.observer = observer

    def run_simulation(self, chat_turn_limit: int = 30) -> None:
        self.reset_agents()
        msg = self.agents[0].system_message
        n = 0
        while n < chat_turn_limit:
            n += 1
            observer_msg = HumanMessage(
                content=self.observer.step(self.observer.memory.get_memory()).content
            )
            print("[Observer]: Next is %s" % observer_msg.content)

            next_speaker = observer_msg.content

            for agent in self.agents:
                if agent.name == next_speaker:
                    msg = HumanMessage(content=agent.step(msg).content)
                    print(f"[{agent.name}]: {msg.content}\n")
                    break

    def reset_agents(self) -> None:
        for agent in self.agents:
            agent.reset()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a simulation with the given task."
    )

    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="The number of agents for the simulation.",
    )

    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = json.load(f)

    agents = []
    shared_memory = Memory()

    observer = Agent(
        SystemMessage(content=config["observer"]["system_message"]),
        ChatOpenAI(
            temperature=config["observer"]["temperature"],
            model_name=config["observer"]["modelName"],
        ),
        memory=shared_memory,
        name=config["observer"]["name"],
    )

    for agent_config in config["agents"]:
        agent = Agent(
            SystemMessage(content=agent_config["system_message"]),
            ChatOpenAI(
                temperature=agent_config["temperature"],
                model_name=agent_config["modelName"],
            ),
            memory=shared_memory,
            name=agent_config["name"],
        )
        agents.append(agent)

    simulation = Simulation(agents=agents, observer=observer)
    simulation.run_simulation(chat_turn_limit=config["turnLimit"])


if __name__ == "__main__":
    main()
