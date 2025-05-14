from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

root_agent = LlmAgent(
    name="clinical_agent",
    model=LiteLlm(model="ollama/gemma3:27b", endpoint="http://localhost:11434"),
    description="A local reasoning agent using Gemma 3:27B via Ollama",
    instruction="You are a clinical reasoning agent. Answer questions using your medical knowledge.",
    tools=[],
) 