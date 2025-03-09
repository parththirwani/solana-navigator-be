"""
Task parameter templates for Solana blockchain API calls.
"""

TASK_PARAMS_MAP = {
    "getAccountInfo": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [
                "{address}",
                {"encoding": "base64"}
            ]
        }
    },
    "getContractMetadata": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getProgramAccounts",
            "params": [
                "{address}",
                {
                    "filters": [
                        {
                            "dataSize": 17
                        },
                        {
                            "memcmp": {
                                "offset": 4,
                                "bytes": "3Mc6vR"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "getGasPrices": {
        "data": {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "getFeeForMessage",
            "params": [
                "{message}",
                {
                    "commitment": "processed"
                }
            ]
        }
    },
    "getTransactionDetails": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTransaction",
            "params": [
                "{signature}",
                {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}
            ]
        }
    },
    "getHealth": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getHealth"
        }
    },
    "requestAirdrop": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "requestAirdrop",
            "params": [
                "{address}",
                "{amount}"
            ]
        }
    },
    "getBalance": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [
                "{address}"
            ]
        }
    },
    "getInflationRate": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getInflationRate"
        }
    },
    "getSupply": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getSupply"
        }
    },
    "getTokenAccountBalance": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenAccountBalance",
            "params": [
                "{tokenAccountPubkey}"
            ]
        }
    },
    "getTokenAccountsByDelegate": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenAccountsByDelegate",
            "params": [
                "{address}",
                {
                    "programId": "{programId}"
                },
                {
                    "encoding": "jsonParsed"
                }
            ]
        }
    },
    "getTokenAccountsByOwner": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenAccountsByOwner",
            "params": [
                "{address}",
                {
                    "programId": "{programId}"
                },
                {
                    "encoding": "jsonParsed"
                }
            ]
        }
    },
    "getTokenLargestAccounts": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenLargestAccounts",
            "params": [
                "{address}"
            ]
        }
    },
    "getTokenSupply": {
        "data": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenSupply",
            "params": [
                "{address}"
            ]
        }
    }
}