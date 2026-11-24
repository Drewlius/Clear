from clear.providers.openai import chat
from clear.tools.run_command import run

system_prompt = {"role": "system", "content": "you are an assistant inside of Clear. You have limited access to the system"}
chat_thread = [system_prompt]

while True:
    text = input("User: ")
    if not text:
        break
    user_text = {"role": "user", "content": text}
    chat_thread.append(user_text)
    reply = chat(chat_thread)
    if reply.tool_calls:
        rounds = 0
        while reply.tool_calls and rounds < 5:
            rounds += 1
            chat_thread.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [
                    {
                        "id": c.id,
                        "type": "function",
                        "function": {
                            "name": c.function.name,
                            "arguments": c.function.arguments
                        }
                    }
                    for c in reply.tool_calls
                ],    
            })
            for command in reply.tool_calls:
                print(f'Command: {command.function.name}, Arguments: {command.function.arguments}')
                output = run(command.function.arguments)
                chat_thread.append({"role": "tool", "tool_call_id": command.id, "content": output})
                print(f'Tool Output: {output}')
            reply = chat(chat_thread)
        if reply.tool_calls:
            chat_thread.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [
                    {
                        "id": c.id,
                        "type": "function",
                        "function": {
                            "name": c.function.name,
                            "arguments": c.function.arguments
                        }
                    }
                    for c in reply.tool_calls
                ]
            })
            print("stopped at tool count (5)")
            for command in reply.tool_calls:
                chat_thread.append({"role": "tool", "tool_call_id": command.id, "content": "cancelled: tool cap reached"})
            reply = chat(chat_thread)
    chat_thread.append({"role": "assistant", "content": reply.content or ""})
    print(f'Agent: {reply.content or "(agent returned no text)"}')