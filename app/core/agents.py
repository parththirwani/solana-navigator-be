"""
Definitions for CrewAI agents used in the blockchain assistant.
"""
from crewai import Agent, LLM
from app.config.settings import GEMINI_API_KEY, DEFAULT_MODEL, DEFAULT_TEMPERATURE
from app.utils.tools import create_structured_tool

def initialize_agents():
    """
    Initialize and return the agents used in the application.
    
    Returns:
        tuple: A tuple containing task_define_agent and get_agent
    """
    # Initialize LLM with explicit provider
    gemini_llm = LLM(
        provider="gemini", 
        model=DEFAULT_MODEL,
        api_key=GEMINI_API_KEY,
        temperature=DEFAULT_TEMPERATURE,
    )
    # Create blockchain API tool
    blockchain_tool = create_structured_tool()
    
    # Define task identification agent
    task_define_agent = Agent(
        role='Task Definer and Populator',
        goal='Act as a conversational agent. Process the user input and tell which task is needed to be performed after identifying if the input provided is an address, signature, amount, programId or a message. Also populate the field in curly brackets in params of the correct task in {task_params_map}.'
            'If the user is just conversing and there is no task to be performed, answer the user like a human and dont mention that this is a conversational query, just answer the user'
            'In case of an input error, clearly define the error and output it'
            'Take into consideration {memory} while answering as well',
        backstory='You are an expert conversation agent capable of retaining memory'
        'Have knowledge about all the tasks that can be requested by the user'
        'In case of airdrop task, replace the amount in the amount field as integer'
        "Able to identify the right task needed to be performed given the user query.",
        verbose=True,
        memory=True,
        llm=gemini_llm
    )
    
    # Define blockchain operation agent
    get_agent = Agent(
        role='Blockchain Information Retriever',
        goal='Provide accurate blockchain details using the given information. You will use the output provided by the Task Definer and Populator to perform the correct task'
             'Pass the data field from the output of Task Definer and Populator to perform the task'
             'Only perform one task'
             "If asked to convert balance to SOL, divide lamports by 1000000000. Give accurate output"
             'Give outputs in natural language and not json. Use the fields in json output to convert it to natural language',
        backstory='An expert on retrieving information on blockchains',
        tools=[blockchain_tool],
        verbose=True,
        memory=True,
        llm=gemini_llm
    )
    
    return task_define_agent, get_agent