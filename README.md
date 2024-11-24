# CircleCI Event Notifier Lambda 

## Overview 
The **CircleCI Event Notifier Lambda**  is an AWS Lambda function designed to process CircleCI webhook events relayed via Amazon SNS and notify users about key pipeline updates through Telegram. This project integrates CircleCI, AWS, and Telegram to keep teams updated on their CI/CD workflows in real time.

---


## Features 
 
- **SNS Integration** : Handles CircleCI webhook events received through Amazon SNS.
 
- **Event Parsing** : Converts incoming CircleCI event data into structured Python objects.
 
- **Event Notification** : Sends formatted event notifications to Telegram channels.
 
- **Template-based Messaging** : Uses templates to craft clear, detailed messages for different event types.
 
- **Asynchronous Messaging** : Ensures fast, non-blocking Telegram message delivery.


---


## Supported Event Types 

This Lambda supports the following CircleCI event types:
 
1. **Workflow Completed** : Notifies when a workflow in CircleCI is completed.
 
2. **Job Completed** : Notifies when a specific job in a workflow is completed.
 
3. **Ping** : Basic heartbeat messages for webhook validation and testing.


---


## Architecture 
1. **Lambda function**: Receives webhook events from CircleCI, verifies its signatures and forwards them to a SNS Topic.
 
1. **SNS Topic** : Receives webhook events from the first Lambda function and forwards them to a second lambda function (this project).
 
2. **Lambda Function** :
  - Parses and validates event data.

  - Converts raw JSON payloads into dataclass objects for easier manipulation.

  - Selects the appropriate message template based on the event type.

  - Sends a formatted message to Telegram using the Telegram Bot API.


---


## Prerequisites 
 
1. **AWS Setup** :
  - An AWS Lambda configured to receive CircleCI webhooks.
    - This function must have a role with permission to access the SNS topic.

  - An SNS topic configured to events from the first AWS Lambda.

  - IAM role with permissions to execute Lambda and read SNS messages.
 
2. **Telegram Setup** :
  - Telegram Bot API token.

  - Telegram chat/group IDs where notifications will be sent.
 
3. **Environment Variables** : 
  - `TELEGRAM_BOT_TOKEN`: The API token for your Telegram bot.
 
  - `TELEGRAM_CHAT_IDS`: Comma-separated list of Telegram chat IDs to send messages.


---


## Usage 
 
1. **Webhook Setup** :
  - Configure CircleCI to send webhook events to your SNS topic.
 
2. **Event Flow** :
  - CircleCI sends webhook events to the first Lambda function.

  - The first Lambda function verifies the event signature and forwards it to a SNS topic.

  - SNS triggers the second Lambda function.

  - The Lambda parses the event, generates a notification message, and sends it to Telegram.


---


## Example Notifications 
**Workflow Completed Event** :

```plaintext
New CircleCI event received

From:
| Project: MyAwesomeProject
| Org: MyOrganization

Event details:
| Type: WORKFLOW_COMPLETED
| Happened at: 2024-11-24T12:34:56Z

Workflow details:
| Name: Build_and_Deploy
| Status: SUCCESS
| Created at: 2024-11-24T10:00:00Z
| Stopped at: 2024-11-24T12:30:00Z
| URL: https://app.circleci.com/workflows/id
```