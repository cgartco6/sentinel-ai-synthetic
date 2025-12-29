from agents.sentinel_rebuilder_agent import SentinelRebuilderAgent

class SentinelBinding:
    def __init__(self, sentinel_path):
        self.sentinel_path = sentinel_path
        self.rebuilder = SentinelRebuilderAgent()

    def run(self):
        print("🔗 Binding Synthetic Engine to Sentinel Repo")
        self.rebuilder.rebuild(self.sentinel_path)
        print("✅ Sentinel repo structurally stabilized")
