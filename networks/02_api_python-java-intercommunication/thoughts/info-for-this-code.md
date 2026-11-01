Python: is the main application code.
Java: is the supporting server code.
Communication method: HTTP API.
Address: local host 127.0.0.1 
Data Format: JSON.
Operation specs:
  Python sends 2 numbers, java takes it and sennds back the addition of them.


flowchart LR
    A["Python Client"] -->|"HTTP POST + JSON"| B["Java API Server"]
    B --> C["Java Addition Operation"]
    C --> B
    B -->|"HTTP Response + JSON"| A
    A --> D["Python Displays Result"]


