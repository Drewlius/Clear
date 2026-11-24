tool_schema = [
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Run a command and return its output",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "The Command to run"}
                },
                "required": ["command"] 
            }
        }
    }
]

def tooling():
    return tool_schema