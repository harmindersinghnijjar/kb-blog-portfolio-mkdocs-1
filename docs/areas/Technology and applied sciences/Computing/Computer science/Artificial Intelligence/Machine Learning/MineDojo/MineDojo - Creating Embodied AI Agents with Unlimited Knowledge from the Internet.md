Keywords: #embodied-agents #reinforcement-learning #large-pre-training #open-ended-learning #internet-knowledge-base #minecraft #multitask-learning


![[Jim_Fan_10Aug2022_19-19-1.png]]

![[55737.png]]

Have you ever played a video game and thought about how the characters in the game move around and make decisions? Well, there are some special robots called "autonomous agents" that can do similar things in the real world! They can learn how to do different tasks by practicing, just like how you learn new things by practicing.

But right now, these robots can only learn how to do a few specific things really well, like playing a certain video game or solving a certain puzzle. NVIDIA want to make robots that can learn to do lots of different things, just like how you can learn to do lots of different things in real life.

To do this, they used a video game called Minecraft that has lots of different tasks for the robot to learn, like building a house or finding treasure. They also made a big library of information that the robot can learn from, like videos and tutorials.

Then they made a special kind of robot that can learn from all of this information without anyone having to tell it what to do. It can understand what people are saying and use that information to learn how to do different tasks in Minecraft.

The end goal is for other people to be able to use these autonomous agents to make even better robots in the future. It's like building a big toolbox full of tools that anyone can use to make something new and exciting!

##### Generalist Agent
In the field of artificial intelligence, researchers aim to develop machines that can learn and perform a wide range of tasks, similar to human beings. Such machines are called "generalist agents" and the research goals for creating them can be categorized into three main objectives.

![[3. Resources Personal/Images/Jim_Fan_10Aug2022_5-5-1.png]]

1. Open-ended objectives: Firstly, a generalist agent should be given an "open-ended" objective, meaning that it should be capable of figuring out what it needs to do on its own, without being solely reliant on a predetermined set of instructions. Essentially, it is like providing a robot with a task and allowing it to complete it by itself.
2. Massively multitask: Secondly, a generalist agent should be capable of performing multiple tasks simultaneously, a concept referred to as "massively multitasking." Ideally, the agent should also be able to comprehend and execute commands that are given in natural language, much like how we give instructions to our friends.
3. World knowledge: Lastly, the generalist agent should possess "world knowledge," that is, a comprehensive understanding of how the world functions without requiring retraining each time. This would allow the agent to be equipped with a considerable amount of knowledge beforehand, minimizing the resources and time needed for it to learn and adapt.

![[Jim_Fan_10Aug2022_3-3-1 1.png]]

In summary, the ultimate goal for developing a generalist agent is to design a machine that can learn on its own, perform a multitude of tasks simultaneously, and possess significant knowledge of the world.


##### Minecraft 
Minecraft is a widely popular 3D open world game that offers players an opportunity to explore the game's virtual environment and create various structures. Currently, Minecraft has a large player base with over 140 million active players, which surpasses the population of Mexico in number.

![[Jim_Fan_10Aug2022_6-6-1.png]]

MineDojo is a novel research framework for the exploration of embodied artificial intelligence (AI) agents, with the primary objective of facilitating research in the development of generalized agents through foundational models. This framework utilizes the popular game Minecraft as a simulation suite, featuring over 3,000 open-ended and language-prompted tasks, as well as a vast multimodal knowledge base. The three distinct techniques employed by MineDojo for enabling researchers to instruct a computer to perform various tasks include an open-ended environment, foundational models, and an internet-skill knowledge base.

![[Jim_Fan_10Aug2022_8-8-1.png]]

The ultimate goal of the MineDojo framework is to produce machines capable of self-directed learning, simultaneous execution of numerous tasks, and a significant comprehension of the world, commonly referred to as generalist agents. This research framework, therefore, offers a promising avenue for researchers to delve into the creation of embodied AI agents and explore the application of foundational models in such agents' development.

1. Open-ended environment
   ![[Jim_Fan_10Aug2022_9-9-1 2.png]]
2. Foundation model
   ![[Jim_Fan_10Aug2022_28-28-1 1.png]]
3. Internet-skill knowledge base
   ![[Jim_Fan_10Aug2022_17-17-1.png]]

#### Open-ended environment

![[Jim_Fan_10Aug2022_9-9-1 2.png]]

##### Versatile simulator:
A versatile simulator in machine learning is like a pretend world that computers can use to practice doing things, just like you might use a play kitchen or a toy car to practice cooking or driving. The simulator can create many different situations, so the computer can learn how to do lots of different things. 

In the case of MineDojo, it uses a versatile simulator to create over 3,000 different tasks for the computer to practice on, which helps it get really good at those tasks. 

![[Jim_Fan_10Aug2022_10-10-1.png]]

###### Programmatic tasks:
Out of the total 3,000 tasks, around half are programmatic tasks. These are tasks which have groundtruth success conditions. 

![[Jim_Fan_10Aug2022_11-11-1.png]]

###### Creative tasks:
The other half are creative tasks, these are free-formed and open-ended. 

![[Jim_Fan_10Aug2022_12-12-1.png]]

##### Large pre-training model:

In addition to the versatile simulator and foundation model, MineDojo also uses a large pre-training model that incorporates internet-scale data to improve the agent's ability to learn and adapt. This model leverages the vast amount of information available on the internet, including text, images, and videos, to teach the agent about a wide range of topics.

##### Multitask learning:

The pre-training model also allows the agent to learn multiple tasks simultaneously, a technique known as "multitask learning." This means that the agent can learn to perform several different tasks at once, rather than focusing on one task at a time. This approach is more efficient and effective because it allows the agent to share common knowledge across tasks, leading to faster learning and better performance.

##### Reinforcement learning:

Finally, MineDojo uses reinforcement learning to fine-tune the agent's performance on specific tasks. Reinforcement learning is a type of machine learning that involves training the agent through trial and error, rewarding it when it performs well and punishing it when it performs poorly. This approach helps the agent improve its performance over time, making it better equipped to handle a wide range of tasks.

Overall, MineDojo represents a major step forward in the development of embodied, generalized agents. By leveraging the power of Minecraft, a versatile simulator, a foundation model, a large pre-training model, multitask learning, and reinforcement learning, researchers are making significant progress toward creating machines that can learn and perform a wide range of tasks on their own.

#### Foundation model

##### Steps towards a generalist agent:

![[Jim_Fan_10Aug2022_28-28-1 1.png]]

The team has developed MineCLIP, a contrastive video-language model that connects natural language subtitles to associated video segments. This model serves as a basic reward function for an AI agent that can learn a variety of skills to a certain degree. The team views MineCLIP as a promising tool for teaching AI agents, but they recognize that more work is needed to improve the technology.

![[Jim_Fan_10Aug2022_30-30-1.png]]

It behaves similarly to how [[OpenAI's Clip]] learns to associate video and the text that describes the content. MineClip can then be repurposed to be a language conditioning model. In this way, it becomes integrated in the reward function for the agent. 

![[Jim_Fan_10Aug2022_31-31-1.png]]


#### Internet-scale knowledge base

![[Pasted image 20230219202653.png]]

##### YouTube videos and transcripts
Minecraft is one of the most streamed video games on YouTube. The NVIDIA team was able to collect more than 700,000 videos with two billion words in transcripts which provided rich learning material of human strategies and creativity. The time-aligned transcripts enable the agent to ground free-form natural language in video pixels and learn the semantics of diverse activities without laborious human labeling.

![[Jim_Fan_10Aug2022_20-20-1.png]]

##### Minecraft Wiki
There is a Minecraft specific Wikipedia that explains every entity and mechanism in the game. The NVIDIA team scraped 7,000 Wikipedia pages with interleaving multimodal data. 

###### Examples:

1. Gallery of Minecraft monsters:
![[Jim_Fan_10Aug2022_21-21-1.png]]

2. Crafting recipes:
 ![[Jim_Fan_10Aug2022_22-22-1.png]]  
![[Jim_Fan_10Aug2022_23-23-1.png]]

![[Jim_Fan_10Aug2022_24-24-1.png]]

##### Reddit
The Minecraft subreddit is an active forum. Players showcase their creations and also ask questions for help. 

![[Jim_Fan_10Aug2022_25-25-1.png]]![[Jim_Fan_10Aug2022_26-26-1.png]]
![[Jim_Fan_10Aug2022_27-27-1.png]]


