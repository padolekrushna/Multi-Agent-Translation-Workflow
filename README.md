#Build a workflow with three agents:

French Translator Agent – Translates English to French.
Spanish Translator Agent – Translates French to Spanish.
English Translator Agent – Translates Spanish back to English.

#This will help you understand:

Agent creation
Workflow orchestration
Streaming outputs
Azure integration
Agent-to-agent communication

maf_translation_project/
│
├── main.py
├── agents/
│   ├── french_agent.py
│   ├── spanish_agent.py
│   └── english_agent.py
├── workflow/
│   └── translation_workflow.py
├── utils/
│   └── azure_client.py
└── README.md
