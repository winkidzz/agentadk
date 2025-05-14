from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import requests
import re

# DuckDuckGo Lite HTML scraping tool

def ddg_lite_search(query: str, num_results: int = 5) -> dict:
    """Scrape DuckDuckGo Lite HTML results and return a dict with results, links, and the full HTML."""
    url = "https://lite.duckduckgo.com/lite/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    data = {"q": query}
    resp = requests.post(url, headers=headers, data=data)
    html = resp.text
    # Match both single and double quotes for class attribute
    results = re.findall(r'<a rel=[\'\"]nofollow[\'\"] href="([^"]+)" class=[\'\"]result-link[\'\"]>([^<]+)</a>', html)
    output = []
    links = []
    for link, title in results[:num_results]:
        output.append({"title": title, "link": link})
        links.append(link)
    return {
        "results": output,
        "links": links,
        "html": html
    }

root_agent = LlmAgent(
    name="clinical_agent",
    model=LiteLlm(model="ollama/gemma3:27b", endpoint="http://localhost:11434"),
    description="A local reasoning agent using Gemma 3:27B via Ollama",
    instruction="You are a clinical reasoning agent. Answer questions using your medical knowledge.",
    tools=[ddg_lite_search ],
)

# Example usage for streaming response and direct tool test
if __name__ == "__main__":
    prompt = "Barack Obama"
    print("\nDirect DuckDuckGo Lite tool call result:")
    ddg_result = ddg_lite_search(prompt)
    for i, r in enumerate(ddg_result["results"], 1):
        print(f"{i}. {r['title']}: {r['link']}")
    print(f"\nAll links: {ddg_result['links']}")
    print(f"\nFirst 1000 chars of HTML:\n{ddg_result['html'][:1000]}")
    print("\nDirect Playwright tool call result:")
