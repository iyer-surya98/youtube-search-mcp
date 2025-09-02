# youtube-search-mcp

A local MCP server implementation that allows Claude Desktop to search for YouTube videos.

This project provides a simple MCP-compatible server that receives search queries and returns YouTube video results using the [youtube-search](https://github.com/joetats/youtube_search) library.

---

## Table of Contents

- [youtube-search-mcp](#youtube-search-mcp)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Using uv](#using-uv)
    - [Using pip](#using-pip)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Links](#links)
  - [License](#license)

---

## Features

- Local MCP server for YouTube search
- Integrates with Claude Desktop
- Uses youtube-search-python library for video search (no API key required)
- Clean, streamlined JSON response format
- Searches YouTube directly without rate limits

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) is optional but highly recommended for package management
- youtube-search-python package

## Installation

### Using uv
```sh
uv sync
```
### Using pip
Create a virtual environment, activate it, then run:
```sh
pip install -e .
```

## Configuration

No API key or additional configuration required! The server uses the youtube-search-python library which scrapes YouTube search results directly.

## Usage

Start the MCP server using `uv`:
```sh
uv run server.py
```
Or, if using pip:
```sh
.venv\Scripts\activate
python server.py
```

Then, configure Claude Desktop to use your local MCP server by adding the following to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "youtube-search": {
      "command": "uv",
      "args": [
        "--directory",
        "path\\to\\youtube-search-mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```

Or if using pip:
```json
{
  "mcpServers": {
    "youtube-search": {
      "command": "path\\to\\venv\\Scripts\\python.exe",
      "args": ["server.py"],
      "cwd": "path\\to\\youtube-search-mcp"
    }
  }
}
```

## Links
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Claude Desktop](https://claude.ai/download)
- [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)
- [uv](https://docs.astral.sh/uv)

## License
MIT License. See LICENSE for details.