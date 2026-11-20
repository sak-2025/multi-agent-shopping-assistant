from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="catalog_agent"
    description=""
    model="gemini-3.1-flash-lite",
    insteuction=""
)