from tools.filesystem import write_file

class DeepAgent:
    def build(self, task):
        write_file(task["path"], task["code"])
        return task
