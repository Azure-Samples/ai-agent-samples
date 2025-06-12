# Azure AI Agent & Custom Email Service Sample

This repository demonstrates how to integrate the Azure AI Agent service with a custom email sending function. The notebook registers a custom function tool (`send_email`) that wraps an email service and is automatically called during the agent run.

## Overview

This sample project shows how to:
- Create and configure an Azure AI Agent with a custom tool.
- Register a custom email sending function (`send_email`) that wraps the Azure Communication Services EmailClient.
- Execute an agent run that triggers the custom tool call and sends an email.
- Monitor the agent run status and display conversation messages.

## Prerequisites

Before running the samples, ensure that you have the following:
- **Python 3.9+** installed.
- An [Azure AI Foundry] project with:
  - A valid **PROJECT_CONNECTION_STRING**.
  - A **MODEL_DEPLOYMENT_NAME** for the AI model.
- An [Azure Communication Services](https://azure.microsoft.com/en-us/services/communication-services/) resource with a configured (Email Communication Service domain)[https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/create-email-communication-resource?pivots=platform-azp].
- Environment variables set up as described below.

## Environment Variables

Set the following environment variables with your own values either in your system or in a `.env` file:

### For Azure AI Agents:
- `PROJECT_CONNECTION_STRING`: Connection string from your Azure AI Foundry project.
- `MODEL_DEPLOYMENT_NAME`: Deployment name of your AI model.

### For Email Service:
- `EMAIL_COMMUNICATION_SERVICES_STRING`: Connection string for Azure Communication Services.
- `RECIPIENT_EMAIL`: The recipient email address.
- `SENDER_EMAIL`: The sender's email address (typically the one configured in your Azure Communication Services email resource).

## Installation

Install the required packages using pip:

```bash
pip install azure-ai-agents azure-identity azure-communication-email python-dotenv
```

## Project structure
├── README.md
├── notebook.ipynb         # Updated notebook demonstrating the custom function tool and email sending process.
├── email_services.py      # Python module containing the azure_send_email function and default email MESSAGE.
└── .env                   # (Optional) File to store environment variables.

## Instructions

### Running the Notebook

1. Open the notebook (`azure_agent.ipynb`) in Jupyter Notebook or VS Code.
2. Ensure your environment variables are set as described in the README.
3. Execute the notebook cells sequentially. The notebook will:
   - Create an Azure AI Agent with instructions that reference the custom `send_email` tool.
   - Start a conversation thread and post a user message instructing the assistant to send an email with a specific subject and content.
   - Trigger an agent run that polls for tool call requirements.
   - When the run requires a tool call, the custom email function (`send_email_function`) is executed, which calls the `azure_send_email` service.
   - Display the status of the run and all conversation messages.
   - Finally, clean up by deleting the created agent.

### Running the Python Script Directly

1. Open a terminal in the project directory.
2. Run the email service script:
   ```bash
   python email_services.py
   ```

This will execute the azure_send_email function using the default message and print the result to the console.

##License
MIT License