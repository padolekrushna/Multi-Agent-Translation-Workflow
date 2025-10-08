
from agent_framework import WorkflowBuilder

def build_translation_workflow(french_agent, spanish_agent, english_agent):
    builder = WorkflowBuilder()
    builder.add_node("french", french_agent)
    builder.add_node("spanish", spanish_agent)
    builder.add_node("english", english_agent)

    builder.connect("french", "spanish")
    builder.connect("spanish", "english")

    return builder.build()
