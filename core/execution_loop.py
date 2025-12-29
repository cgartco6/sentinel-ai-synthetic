class ExecutionLoop:
    def __init__(self, architect, deep, ai, reviewer, tester, fixer, goal):
        self.architect = architect
        self.deep = deep
        self.ai = ai
        self.reviewer = reviewer
        self.tester = tester
        self.fixer = fixer
        self.goal = goal

    def start(self):
        plan = self.architect.design(self.goal)

        while True:
            for task in plan:
                code = self.deep.build(task)
                improved = self.ai.improve(code)

                issues = self.reviewer.review(improved)
                if issues:
                    improved = self.fixer.fix(improved, issues)

                if not self.tester.test(improved):
                    improved = self.fixer.fix(improved, ["runtime failure"])

            if self.reviewer.is_stable():
                break
