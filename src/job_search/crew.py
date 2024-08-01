from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.job_search.tools.search import searchtool
import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Uncomment the following line to use an example of a custom tool
# from job_search.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama3-70b-8192"
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

@CrewBase
class JobSearchCrew():
	"""JobSearch crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def Researcher(self)-> Agent:
		return Agent(
		config=self.agents_config['researcher'],
		tools=[
			searchtool.search_internet,
			],
		verbose=True	
		)
	
	@agent
	def Job(self)-> Agent:
		return Agent(
			config=self.agents_config["Job_availability"],
			tools=[searchtool.search_linkedin],
			verbose=True
		)
	
	@agent
	def Project(self)-> Agent:
		return Agent(
			config=self.agents_config["Futuristic_project"],
			tools=[searchtool.project],
			verbose=True
		)
	
	@agent
	def Interview(self)-> Agent:
		return Agent(
			config=self.agents_config["Interview_preparer"],
			tools=[searchtool.search_internet],
			verbose=True
		)
	
	@task
	def research_task(self)-> Task:
		return Task(
			config=self.tasks_config["research"],
			agent=self.Researcher(),
			output_file="skill.md",
		)
	
	@task
	def job_task(self)-> Task:
		return Task(
			config=self.tasks_config["job"],
			agent=self.Job(),
		)
	
	@task
	def project_task(self)-> Task:
		return Task(
			config=self.tasks_config["project"],
			agent=self.Project(),
		)
	
	@task
	def interview_task(self)->Task:
		return Task(
			config=self.tasks_config["interview_pre"],
			agent=self.Interview(),
			output_file="interview_materials.md",
		)


	@crew
	def crew(self)->Crew:
		return Crew(
			agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
		)