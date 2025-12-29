from core.execution_loop import ExecutionLoop
from agents.architect_agent import ArchitectAgent
from agents.deep_agent import DeepAgent
from agents.ai_agent import AIAgent
from agents.reviewer_agent import ReviewerAgent
from agents.tester_agent import TesterAgent
from agents.fixer_agent import FixerAgent

class Orchestrator:
    def __init__(self, project_name, goal):
        self.project_name = project_name
        self.goal = goal

        self.architect = ArchitectAgent()
        self.deep = DeepAgent()
        self.ai = AIAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TesterAgent()
        self.fixer = FixerAgent()

    def run(self):
        ExecutionLoop(
            self.architect,
            self.deep,
            self.ai,
            self.reviewer,
            self.tester,
            self.fixer,
            self.goal
        ).start()
