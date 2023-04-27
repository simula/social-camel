# social-camel

In social-camel two agents discuss a common topic where each of the agents has a different perspective. For example a student and a teacher discussing why 2 and 2 is 4 where the stuents perspective is that they do not understand this and the teacher has a good understanding and explains it. This allows for several interesting use cases such as exploring conversations between a doctor or a patient, etc. 

social-camel is an extension of the example from https://python.langchain.com/en/latest/use_cases/agents/camel_role_playing.html. The ogirinal CAMEL allows to sandbox two agents that can give each others intructions to solve a task. 

## Three or more agents support
three_agents_example.ipynb contains an updated version that implements a shared memory for the conversation flow. This allows to let several agents interact together. In the provided example a teacher and a student are involved that dicuss a topic. The third agent is an observer that provides input when it thinks it is necessay for the conversation. 

## Wrapper for fine-tuned openai model
We also provide and example for a wrapper that allows to use fine tuned models (custom_llm_wrapper_openai.py). This can be specifically interesting if one of the conversation participants is an expert in a specific field represented by a fine-tuned mode. 

## Original CAMEL Role-Playing Autonomous Cooperative Agents implementation

Langchain implementation: https://python.langchain.com/en/latest/use_cases/agents/camel_role_playing.html. <br />
The original implementation: https://github.com/lightaime/camel. <br />
Project website: https://www.camel-ai.org/. <br />
Arxiv paper: https://arxiv.org/abs/2303.17760. <br />


## Three agents example
Example output where a teacher is trying to explain why red is red to a student and an observer is helping.
```
Teacher: Hello, Student. Today we will be discussing the concept of why red is red. Red is a color that is perceived by our eyes when light of a certain wavelength is reflected off an object and enters our eyes. This wavelength is around 620-750 nanometers, which is longer than other colors like blue or green. This is why we see red as a distinct color. 

Additionally, the perception of color is also influenced by our brain's interpretation of the signals sent by our eyes. Our brain processes the information received from our eyes and assigns a color to it based on our past experiences and cultural influences. This is why different cultures may have different associations with the color red. 

Do you have any questions about this concept?

Student: Thank you for explaining that to me, Teacher. I have a question. You mentioned that the perception of color is influenced by our brain's interpretation of the signals sent by our eyes. Does that mean that different people can see the same object as different colors? For example, can one person see a red apple as green while another person sees it as red?

Observer: As an observer, I would like to add that while it is possible for different people to perceive colors differently, it is not common for someone to see a red apple as green. This is because the perception of color is based on the wavelengths of light that are reflected by an object and absorbed by our eyes. However, there are some conditions such as color blindness or color vision deficiencies that can affect how someone perceives colors. It is important to note that these conditions are not a matter of opinion or personal preference, but rather a physiological difference in how the eyes and brain process color information.

Teacher: Thank you for adding that, Observer. You are correct that color perception can be affected by conditions such as color blindness or color vision deficiencies. These conditions can cause someone to have difficulty distinguishing between certain colors or perceiving them differently than someone with normal color vision. It is important to be aware of these conditions and to make accommodations when necessary to ensure that everyone can fully participate in activities that involve color perception.

Student: Thank you for your response, Teacher. However, I think I may have confused you with my question. I was actually asking if two people with normal color vision can see the same object as different colors due to their brain's interpretation of the signals sent by their eyes.

Observer: As an observer, I can clarify that it is possible for two people with normal color vision to perceive the same object as slightly different colors due to variations in their individual color perception. This is because the perception of color is subjective and can be influenced by factors such as lighting conditions, background colors, and personal experiences. However, the differences in perception are usually minor and do not result in one person seeing a red apple as green while another sees it as red.

Teacher: Thank you for clarifying, Observer. You are correct that variations in individual color perception can cause two people to perceive the same object as slightly different colors. However, as you mentioned, these differences are usually minor and do not result in one person seeing a red apple as green while another sees it as red. It is important to keep in mind that while color perception can be influenced by individual factors, the underlying physical properties of color remain the same.

Student: Thank you for your explanation, Teacher. I think I understand the concept better now. So, if I understand correctly, the color red is a result of the reflection of light of a certain wavelength, and our brain interprets this information to create the perception of the color red. Is that correct?

Observer: As an observer, I can confirm that your understanding is correct. The color red is a result of light with a certain wavelength being reflected by an object and then absorbed by our eyes. Our brain then interprets this information to create the perception of the color red. The wavelength of light that we perceive as red is around 620-750 nanometers.

Teacher: Thank you for confirming, Observer. It's important to understand the physical properties of color in order to fully appreciate and comprehend the world around us. Do you have any other questions or comments on the topic of why red is red?

Student: Thank you for your explanation, Teacher. I don't have any further questions at the moment, but I appreciate your help in understanding this concept.

Observer: As an observer, you're welcome. It was my pleasure to help clarify the concept for you. If you have any further questions in the future, please don't hesitate to ask.

Teacher: Thank you, Observer. I appreciate your willingness to help and provide additional information. If any further questions or comments arise, I will be sure to reach out.
```

## Two agents example
Example output where a teacher is trying to explain why 2 + 2 = 4 to a student.
```
Teacher: Great, let's get started! So, as a math teacher, I can explain why 2 + 2 equals 4. Would you like me to start with a basic explanation or a more advanced one?

Student: As a very dumb student, I would appreciate it if you could start with a basic explanation.

Teacher: Of course, I'm happy to help! So, when we say "2 + 2", we're essentially asking how many things we have when we combine two groups of two things each.

So, if we have two apples and we add two more apples, we end up with four apples in total. The same goes for any other objects or numbers.

Does that make sense so far?

Student: Yes, I understand the concept of combining two groups of two things to get four things in total. But why does it work that way? Why does 2 + 2 always equal 4?
```
