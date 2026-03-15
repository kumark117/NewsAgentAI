echo "# NewsAgentAI" >> README.md

How NewsAgentAI Works:

NewsAgentAI is a lightweight learning AI agent that continuously monitors RSS news feeds and detects emerging topics.

The backend agent fetches articles, extracts topics, and scores them using several signals such as frequency, growth, spread, and persistence.

A monitoring loop updates topic scores over time. Rapid acceleration in topic activity is detected as a "spike", while slower consistent growth appears as a "trend".

The agent also adjusts internal weights over time based on observed topic behavior, allowing the system to gradually improve how it detects meaningful patterns in news activity.

The dashboard polls the backend periodically to display the latest detected spikes, trends, and the current learned weights.