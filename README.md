🎙️ Professor Pharaoh: A Multimodal Kids' History Podcast
Professor Pharaoh is an interactive, AI-driven "Creative Storyteller" agent built for the 2026 Gemini Live Agent Challenge. It transforms historical education into a dynamic experience by generating real-time podcast scripts interleaved with AI-generated historical visuals.

🌟 Key Features
Interleaved Multimodal Output: Seamlessly blends storytelling with visual aids.

Agentic Direction: The agent autonomously decides when to "show" an image based on the narrative flow.

Kid-Friendly Persona: Uses a specialized system prompt to ensure educational yet exciting content.

Real-time Streaming: Leverages Gemini 2.5 Flash for low-latency, "live" feeling interactions.

🛠️ Tech Stack
LLM: Gemini 2.5 Flash (Text Generation & Image Orchestration)

Visuals: Imagen 3 / Gemini Multimodal

SDK: Google GenAI Python SDK

Cloud: Google Cloud Platform (Cloud Run & Vertex AI)

Environment: VS Code Interactive Window (Jupyter)

🏗️ Architecture
The agent follows a Reactive Interleaving pattern:

User Input: Child asks about a topic (e.g., "How were pyramids built?").

Streaming Brain: Gemini 2.5 Flash begins streaming the script.

Pattern Matcher: A local observer identifies custom [IMAGE: ...] tags in the stream.

Multimodal Trigger: The observer calls the Image Generation module.

Inline Display: The visual is rendered directly alongside the text.

🚀 Getting Started
Prerequisites
Python 3.11+

Google AI Studio API Key (or Google Cloud Project ID)

VS Code with the Jupyter extension

Installation
Clone the repo:

Bash
git clone https://github.com/your-username/pharaoh-podcast-agent.git
cd pharaoh-podcast-agent
Install dependencies:

Bash
pip install google-genai pillow ipython
Set your API Key:

Create a .env file or export your key:

Bash
export GOOGLE_API_KEY="your_api_key_here"
Running the Demo
Open podcast_agent.py in VS Code.

Right-click anywhere and select "Run Current File in Interactive Window".

Watch the podcast stream and the images appear!

☁️ Google Cloud Deployment
This project is configured for deployment on Google Cloud Run.

Proof of Deployment: [Link to your recording/screenshot in your repo]

Service Account: Uses Vertex AI User permissions for secure API access.
