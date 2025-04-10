# linkedin-osint-mcp

Uses Serper to perform a Google search to gather a list of employees from LinkedIn.

## Usage
* Install [uv](https://github.com/astral-sh/uv)<br>
* Get an API key from [Serper](https://serper.dev/) and add it to `.env` file.<br>
* Configure MCP client:<br>
E.g., Claude Desktop
```
{
    "mcpServers": {
        "linkedin_osint": {
            "command": "uv",
            "args": [
                "--directory",
                "C:\\path\\\\to\\linkedin-osint-mcp",
                "run",
                "main.py"
            ]
        }
    }
}
```

## Example Queries
"Get a list of users that work at Bullworth Academy." // basic<br>
"Get a list of users that work at Bullworth Academy and find as many as you can." // will search through multiple pages<br>
"Find all users that work at Bullworth Academy and format the results as "flast@bullworth.com" and save to a csv file." // format names into emails
