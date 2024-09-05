from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from instagram.tools.search import SearchTools
#from langchain_groq import ChatGroq

@CrewBase #accesses the agent and task config files. 
class InstagramCrew():
	"""Instagram crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent #agent decorator
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			tool=[
				SearchTools.search_internet,
				SearchTools.search_instagram,
				SearchTools.open_page,
			],
			verbose=True,
		)

	@agent
	def content_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config["content_strategist"], 
			verbose=True,
		)
	
	@agent
	def visual_creator(self) -> Agent:
		return Agent(
			config=self.agents_config["visual_creator"], 
			verbose=True,
			allow_delegation=False, #don't need to interact with other agents. one task only. 
		)
	
	@agent
	def copywriter(self) -> Agent:
		return Agent(
			config=self.agents_config["copywriter"], 
			verbose=True,
		)
	
	@task
	def market_research(self) -> Task:
		return Task(
			config = self.tasks_config["market_research"],
			agent=self.market_researcher(),
			#output_file="market_research.md",
		)

	@task
	def content_strategy_task(self) -> Task:
		return Task(
			config = self.tasks_config["content_strategy"],
			agent = self.content_strategist(),
			#output_file="content-stratgy.md"
		)

	@task
	def visual_content_creation_task(self) -> Task:
		return Task(
			config=self.tasks_config["visual_content_creation"],
			agent=self.visual_creator(),
			#output_file="visual-content.md"
		)

	@task
	def copywriting_task(self) -> Task:
		return Task(
			config=self.tasks_config["copywriting"],
			agent=self.copywriter(),
		)

	@task
	def report_final_content_strategy(self) -> Task:
		return Task(
			config=self.tasks_config["report_final_content_strategy"],
			agent=self.content_strategist(),
			output_file="final-content-strategy.md"
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Instagram crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # in case you want the crewai to manage the agents/tasks
		)