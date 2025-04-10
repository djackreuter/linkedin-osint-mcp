from typing import Any
import json
import httpx
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("linkedin_osint")

load_dotenv()

@mcp.tool()
async def gather_users(company_name: str) -> dict:
    """Perform a google search to gather a list of company employees

    Args:
        company_name: Company name to search for
    """
    users = []
    page = 1

    while True:
        resp = await perform_search(company_name, page)

        if resp.status_code != 200:
            return f"Error fetching results: {resp.text}"

        data = resp.json()
        num_results = len(data["organic"])
        if num_results == 0:
            break

        users.append(parse_results(data))
        page += 1

    return { "users": users, "pages_searched": page }


async def perform_search(company_name: str, page: int) -> Any:
    """Make a request to the Serper API"""
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": f"site:linkedin.com/in \"{company_name}\"",
        "num": 100,
        "page": page
    })

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, headers=headers, data=payload)
            return resp
        except Exception as e:
            return f"Error: {e}"


def parse_results(data: dict) -> list:
    """Parse results and return a list of users"""
    users = []
    for result in data["organic"]:
        users.append(result["title"])
    return users


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
