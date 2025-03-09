"""
Definition of CrewAI tasks for blockchain interactions.
"""
from crewai import Task
from pydantic import BaseModel

class FirstAgentOutput(BaseModel):
    """Schema for the output of the first agent."""
    task: str
    data: dict

def initialize_tasks(task_define_agent, get_agent):
    """
    Initialize all the tasks with their respective agents.
    
    Args:
        task_define_agent: The agent responsible for identifying tasks
        get_agent: The agent responsible for executing blockchain operations
        
    Returns:
        dict: Dictionary of task objects and the get_task for initial task identification
    """
    # Initial task for identifying what the user wants
    get_task = Task(
        description='Identify the task needed to be performed in {text}. Return getAccountInfo is the user wants to send SOL to someone.'
                    'If the user is just conversing and there is no task to be performed, converse with the user like a human and take into consideration {memory} as well',
        expected_output='Give me the name of the task from getAccountInfo, getContractMetadata, getGasPrices, getTransactionDetails, getHealth. Also give the task data from the task_params_map with the populated curly braces if there are any'
                        'Give output with "task" field and "data" field if user is not conversing'
                        'Converse with the user if the user is just conversing and answer him without any additional commentary. Answer like a human. Make no mention that it is a conversational query',
        agent=task_define_agent,
        output_json=FirstAgentOutput
    )

    # Define all blockchain operation tasks
    getContractMetadata = Task(
        description='Fetch metadata details of the program at the given address. Metadata should include owner, lamports, and any associated tags.',
        expected_output='Contract metadata including owner, lamports, space, and other relevant details.',
        context=[get_task],
        agent=get_agent,
    )

    getGasPrices = Task(
        description='Fetch the fees for the message on blockchain.',
        expected_output='All the parameters',
        context=[get_task],
        agent=get_agent,
    )

    getTransactionDetails = Task(
        description='Fetch the details of the transaction with the given ID. Include sender, receiver, amount, timestamp, status, and confirmation count.',
        expected_output='Transaction details including sender, receiver, amount, timestamp, status (confirmed or pending), and confirmation count.',
        context=[get_task],
        agent=get_agent,
    )

    getHealth = Task(
        description='Retrieve the details of the blockchain network. Include current block height, number of transactions per second, and network health status.',
        expected_output='Network information including block height, TPS (transactions per second), and network health status (healthy, degraded, etc.).',
        context=[get_task],
        agent=get_agent,
    )

    getAccountInfo = Task(
        description='Fetch the details of the given address on the blockchain and convert the balance into SOL and check if the SOL is greater than 0.',
        expected_output='Balance, address, space ocucpied by the data, and return true is SOL balance is greather than 0 and false otherwise. Give this output in a sentence form and not json.',
        context=[get_task],
        agent=get_agent,
    )

    requestAirdrop = Task(
        description='Request an airdrop of a specified amount of SOL to the given address. Validate if the request was successful and include the updated balance after the airdrop',
        expected_output='Confirmation of airdrop success, transaction ID, and updated balance in SOL.',
        context=[get_task],
        agent=get_agent,
    )

    getBalance = Task(
        description='Get the balance of the given address and convert it to SOL',
        expected_output='Balance in SOL in a sentence form and not json',
        context=[get_task],
        agent=get_agent,
    )

    getInflationRate = Task(
        description='Fetch the current inflation rate details of the blockchain, including the total, validator, and foundation inflation rates.',
        expected_output='Inflation rate details including total inflation rate, validator inflation rate, and foundation inflation rate in a sentence format.',
        context=[get_task],
        agent=get_agent,
    )

    getSupply = Task(
        description='Retrieve the total supply of SOL on the blockchain. Include circulating and non-circulating supplies and total.',
        expected_output='Supply details including total supply, circulating supply, and non-circulating supply in a sentence format.',
        context=[get_task],
        agent=get_agent,
    )

    getTokenAccountBalance = Task(
        description='Fetch the balance of the token account for the given address. Include the balance in both the smallest unit (lamports) and human-readable format.',
        expected_output='Token account balance including lamports and equivalent human-readable format, decimals and uiAmountString in sentence format.',
        context=[get_task],
        agent=get_agent
    )

    getTokenAccountsByDelegate = Task(
        description='Retrieve all token accounts delegated to the given delegate address. Include account details and associated balances.',
        expected_output='List of token accounts delegated to the address, including account details, balances and delegated amount.',
        context=[get_task],
        agent=get_agent
    )

    getTokenAccountsByOwner = Task(
        description='Retrieve all token accounts owned by the given owner address and given programID. Include account details and associated balances.',
        expected_output='List of token accounts owned by the address, including account details and balances.',
        context=[get_task],
        agent=get_agent
    )

    getTokenLargestAccounts = Task(
        description='Fetch the largest token accounts for the given token mint. Include the account addresses and their respective balances, decimals and uiAmountString.',
        expected_output='List of the largest token accounts for the token mint, including addresses, balances, decimals and uiAmountString.',
        context=[get_task],
        agent=get_agent
    )

    getTokenSupply = Task(
        description='Retrieve the total supply of a specific token for the given token mint address. Include the total supply in lamports and human-readable format.',
        expected_output='Total token supply for the given mint address in lamports and human-readable format. Also give decimals, uiAmountString',
        context=[get_task],
        agent=get_agent
    )

    # Create a task mapping for easy access
    task_map = {
        "getContractMetadata": getContractMetadata,
        "getGasPrices": getGasPrices,
        "getTransactionDetails": getTransactionDetails,
        "getHealth": getHealth,
        "getAccountInfo": getAccountInfo,
        "requestAirdrop": requestAirdrop,
        "getBalance": getBalance,
        "getInflationRate": getInflationRate,
        "getSupply": getSupply,
        "getTokenAccountBalance": getTokenAccountBalance,
        "getTokenAccountsByDelegate": getTokenAccountsByDelegate,
        "getTokenAccountsByOwner": getTokenAccountsByOwner,
        "getTokenLargestAccounts": getTokenLargestAccounts,
        "getTokenSupply": getTokenSupply
    }

    return get_task, task_map