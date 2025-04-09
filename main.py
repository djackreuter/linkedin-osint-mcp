from typing import Any
import json
import requests
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("linkedin_osint")

load_dotenv()

@mcp.tool()
def gather_users(company_name: str) -> list:
    """Perform a google search to gather a list of company employees

    Args:
        company_name: Company name to search for
    """

    url = "https://google.serper.dev/search"
    page = 1

    payload = json.dumps({
        "q": f"site:linkedin.com/in \"{company_name}\"",
        "num": 100,
        "page": page
    })

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code != 200:
        return f"Error fetching results: {resp.text}"

    users = parse_results(resp.json())
    return users


def parse_results(data: dict) -> list:
    users = []
    for result in data["organic"]:
        users.append(result["title"])
    return users


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
