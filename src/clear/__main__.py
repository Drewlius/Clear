from pathlib import Path
from clear.config import create_config
from clear.agentloop import run

if not Path("config.ini").exists():
    create_config

run()