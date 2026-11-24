# clear

A minimal agent harness: one chat loop, one OpenAI-compatible provider, one tool.

## Setup

```sh
uv sync
uv run python -m clear   # first run asks for model/provider/baseURL/apiKey, writes config.ini, then starts
```

`config.ini` is per-machine and gitignored. Any OpenAI-compatible endpoint works — local llama-server, OpenRouter, OpenAI.

## Layout

```
src/clear/
  __main__.py          entry point: make config if missing, start the loop
  agentloop.py         chat loop + tool-call rounds + caps
  config.py            read/write config.ini
  providers/openai.py  the one provider adapter
  tools/schema.py      tool menu the model sees
  tools/run_command.py runs one command, returns stdout
```

## License

AGPL-3.0
