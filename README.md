# University-Chatbot

## Overview
The University Bot is an intelligent chatbot built using AWS Lex and other AWS services. It helps users manage their banking needs through natural language conversations.

## Features
- Marks
- Attendance Tracker
- Voice Interactions
- AI Responses

## Technologies Used
- AWS Lex
- AWS Lambda
- AWS DynamoDB
- AWS S3
- Python

![image](https://github.com/user-attachments/assets/edf8a795-ead4-4d81-ac85-5ba58d202c9c)

## Setup Instructions

### Prerequisites
- An AWS account
- AWS CLI installed and configured
- Basic knowledge of AWS services

### Step 1: Create an AWS Lex Bot
1. Sign in to the AWS Management Console and open the Amazon Lex console.
2. Create a Bot:
   - Click on `Create bot`.
   - Choose `Create from scratch`.
   - Enter the bot name (e.g., `University Chatbot`).
   - Choose the language (e.g., `English (US)`).
   - Set up a session timeout (e.g., 5 minutes).
   - Choose `None` for the IAM role (Amazon Lex will create a service role for you).
   - Click `Next`.
3. Define an Intent:
   - Click on `Add intent`.
   - Choose `Create intent`.
   - Enter an intent name (e.g., `CheckAttendance`).
   - Add sample utterances such as "What is my Attencd" or "Check my Marks".
4. Configure Slots (if needed).
5. Set the fulfillment to be done by an AWS Lambda function.
6. Save and Build the bot.

### Step 2: Create an AWS Lambda Function
1. Open the AWS Lambda console.
2. Create a Lambda Function:
   - Click on `Create function`.
   - Choose `Author from scratch`.
   - Enter the function name (e.g., `AttendanceMarksFunction`).
   - Choose the runtime (e.g., `Python 3.12`).
   - Create a new role with basic Lambda permissions.
3. Add Code to Lambda Function:
   - Copy the code from the `Lambda_function.py` directory of this repository and paste it into the Lambda function code editor.
4. Deploy the Lambda Function.
5. Add Permissions to Lambda Function to be invoked by your Lex bot.

### Step 3: Connect Lex Bot to Lambda Function
1. Return to the Lex Console.
2. Open the intent (e.g., `TimeTable`).
3. Scroll to `Fulfillment`.
4. Choose `AWS Lambda function`.
5. Select your Lambda function (e.g., `University Chatbot`).
6. Save and Build the bot again.

### Step 4: Set Up DynamoDB (Optional)
1. Open the DynamoDB console.
2. Create a Table:
   - Click `Create table`.
   - Enter the table name (e.g., `UniversityBotData`).
   - Define the primary key (e.g., `UserId`).
   - Click `Create`.
3. Modify Lambda Function to Use DynamoDB as needed.

### Step 5: Testing the Bot
1. Return to the Lex Console.
2. Use the `Test Bot` window to interact with your bot and test various intents.
3. Deploy the Bot by integrating it with platforms like Facebook Messenger, Slack, or a custom application.

##Final Chatbot

![image](https://github.com/user-attachments/assets/301f7551-784d-4284-8b5c-0fb6e07e24c1)


To integrate the Banker Bot with an existing webpage or deploy it as a standalone website, we will use the [AWS Lex Web UI repository](https://github.com/aws-samples/aws-lex-web-ui/tree/master).

For a more detailed and step-by-step guide, follow this [AWS Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/94f60d43-15b7-45f4-bbbc-17889ae64ea0/).
