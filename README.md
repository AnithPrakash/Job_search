# JobSearch Crew

## 1.Description

The Crew AI Project is designed to support job applicants by leveraging advanced AI technologies to identify and enhance key skills, streamline project management, highlight critical interview points, and discover job opportunities. This comprehensive approach aims to empower individuals in their job search and career advancement

## 2.Output of the application

![Screenshot 2024-08-01 204617](https://github.com/user-attachments/assets/e9150dbe-7c28-4e10-9ef8-76ff399beabe)

This help to find the right opportunity for you

## 3. Process 

![Screenshot 2024-08-01 203929](https://github.com/user-attachments/assets/aa1d0d2e-abd9-4460-8085-9aaa7d543780)


## 4. Key points 

*  Led a team of 4 AI agents using CrewAI to automate key Job opportunity, boosting overall efficiency
*  Constructed custom AI agents for About job, key points, job opportunity, and Interview Key Points, increasing productivity by 25%
*  Designed a flexible configuration system for quick adjustments and scaling of agents, enhancing system performance.


## About CrewAI 

Welcome to the JobSearch Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/job_search/config/agents.yaml` to define your agents
- Modify `src/job_search/config/tasks.yaml` to define your tasks
- Modify `src/job_search/crew.py` to add your own logic, tools and specific args
- Modify `src/job_search/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run job_search
```

This command initializes the job_search Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The job_search Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the JobSearch Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
