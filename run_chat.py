from dotenv import load_dotenv
from master_agent import MasterAgent

load_dotenv()

if __name__ == "__main__":
    master = MasterAgent()
    master.start_chat()