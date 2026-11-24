import subprocess
import json

def run(command):
    args = json.loads(command)
    try:
        result = subprocess.run(args["command"].split(), capture_output=True, text=True, timeout=15)
        return result.stdout
    except subprocess.TimeoutExpired:
        return f'Error: {args} timed out.'
    except Exception as e:
        return f'Error: {str(e)}.'