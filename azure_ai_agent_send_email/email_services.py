#!/usr/bin/env python3
import os
from azure.communication.email import EmailClient
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MESSAGE = {
    "content": {
        "subject": "This is test",
        "plainText": "Testing out the Email Client",
        "html": "<html><h1>Testing out the Email Client</h1></html>"
    },
    "recipients": {
        "to": [
            {
                "address": os.environ["RECIPIENT_EMAIL"],
                "displayName": os.environ["RECIPIENT_EMAIL"]
            }
        ]
    },
    "senderAddress": os.environ["SENDER_EMAIL"]
}

POLLER_WAIT_TIME = 10


def azure_send_email(subject: str, body: str) -> dict:
    """
    Sends an email using Azure Communication Services EmailClient.

    This function builds the email message from a default template, modifying only the
    'subject' field in the content section. The plainText and other parameters remain unchanged.

    Parameters:
        subject (str): The email subject to override.
        body (str): The content of the email.

    Returns:
        dict: A dictionary containing the operation result:
              - On success: {"operationId": <operation_id>, "status": "Succeeded", "message": <success_message>}
              - On failure: {"error": <error_message>}

    Example:
        >>> response = azure_send_email("Hello World")
        >>> print(response)
    """
    try:
        message = DEFAULT_MESSAGE.copy()
        message["content"] = DEFAULT_MESSAGE["content"].copy()

        message["content"]["subject"] = subject
        message["content"]["html"] = "<html><h1>" + body + "</h1></html>"

        email_client = EmailClient.from_connection_string(
            os.getenv("EMAIL_COMMUNICATION_SERVICES_STRING")
        )

        poller = email_client.begin_send(message)
        time_elapsed = 0

        while not poller.done():
            print("Email send poller status: " + poller.status())
            poller.wait(POLLER_WAIT_TIME)
            time_elapsed += POLLER_WAIT_TIME

            if time_elapsed > 18 * POLLER_WAIT_TIME:
                raise RuntimeError("Polling timed out.")

        result = poller.result()
        if result["status"] == "Succeeded":
            success_message = f"Successfully sent the email (operation id: {result['id']})"
            print(success_message)
            return {"operationId": result["id"], "status": result["status"], "message": success_message}
        else:
            error_msg = str(result.get("error", "Unknown error occurred"))
            raise RuntimeError(error_msg)

    except Exception as ex:
        error_str = f"An error occurred: {ex}"
        print(error_str)
        return {"error": error_str}


if __name__ == '__main__':
    response = azure_send_email(subject="Hello World", html="This is a test email to check the functionality.")
    print(response)
