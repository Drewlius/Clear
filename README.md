[![wakatime](https://wakatime.com/badge/github/Drewlius/Clear.svg)](https://wakatime.com/badge/github/Drewlius/Clear)

# Clear 

A minimal agent harness: one chat loop, one OpenAI-compatible provider, one tool.

## Setup

requires uv and python

from the top level of the cloned repo (AKA, the root)

```sh
git clone https://github.com/Drewlius/Clear
cd Clear
uv sync
uv run python -m clear   # first run asks for model/provider/baseURL/apiKey, writes config.ini, then starts
```

Any OpenAI-compatible API endpoint works, for now. more to come.
`baseURL` must begin with `http://` and end with `/v1`.

## Layout

```
src/clear/
  __main__.py          entry point: checks for config.ini writes if missing, start the loop
  agentloop.py         chat loop + tool-call rounds
  config.py            read/write config.ini
  providers/openai.py  the one provider adapter for now more to come
  tools/schema.py      available tools for the agent
  tools/run_command.py runs one command, returns the result
```

## License

AGPL-3.0
