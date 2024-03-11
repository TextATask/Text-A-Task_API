<!--
title: 'AWS Serverless HTTP API with DynamoDB store'
description: 'HTTP API for Text-A-Task application modeled from https://github.com/serverless/examples/blob/v3/aws-python-http-api-with-dynamodb/README.md'
layout: Doc
framework: v1
platform: AWS
language: Python
-->


# Description of Text-A-Task MVP

As a User I will receive a text in the morning asking me to send back a list of daily tasks. This text will also contain tasks that were not completed the previous day with a reminder that they are on the schedule. When I text back tasks in a list, I will receive a confirmation stating the tasks were saved. Throughout the day, I can send texts to indicate that tasks are complete. I will receive confirmation that the task has been marked as complete. Once that text is sent I will receive a confirmation. In the evening a task completion report for the day will be sent. Any tasks not completed will be rolled over into the next days tasks.


## Use-cases

- API for a Text-A-Task serverless event driven application.


## Structure

This service has a separate directory for all the task operations. For each operation exactly one file exists e.g. `tasks/delete.py`. In each of these files there is exactly one function defined.

Full Text-A-Task architecture:

https://www.figma.com/file/0XWykz2q57tGUbxA3Jz8sa/TextATask--serverlessTextTaskScheduler?type=whiteboard&node-id=0-1&t=M1f9nhM76kqdkC2E-0

## Setup

```bash
npm install -g serverless
```

## Deploy

In order to deploy the endpoint simply run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: serverless-http-api-dynamodb
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks
  GET - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks
  GET - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/{id}
  DELETE - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/{id}
  PATCH - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/{id}/complete
  GET - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/incomplete
  GET - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/updatedToday
functions:
  create: Text-A-Task-API-dev-create
  list: Text-A-Task-API-dev-list
  get: Text-A-Task-API-dev-get
  delete: Text-A-Task-API-dev-delete
  complete: Text-A-Task-API-dev-complete
  all_incomplete: Text-A-Task-API-dev-all_incomplete
  all_updated_today: Text-A-Task-API-dev-all_updated_today
```

## Usage

The following endpoints can be called to interact with tasks:

### Create a Task

```bash
POST https://XXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks
JSON body: { "text": "Example Text" }
```

Example output:

```bash
{"id": "930452", "text": "Example Text", "incomplete": "1710188034.9766896", "updatedAt": "1710188034.9766896", "createdAt": "1710188034.9766896"}
```

### List all Tasks

```bash
GET https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks
```

Example output:
```bash
[{"createdAt": "1710182225.8791468", "text": "Check for updated tasks", "id": "831618", "updatedAt": 1710182249521}, {"createdAt": "1710183077.8419538", "text": "Check for updated tasks attempt 3", "id": "973336", "updatedAt": 1710183087}, {"createdAt": "1708547810.9842713", "text": "Review if complete task works", "id": "915046", "updatedAt": 1708549537921}, {"createdAt": "1710182639.9228485", "text": "Check for updated tasks attempt 2", "id": "644512", "updatedAt": 1710182928}, {"createdAt": "1708550605.1830018", "text": "Verify if all_incomplete function works", "id": "351684", "updatedAt": 1710182981}]
```

### Get a Task

```bash
# Replace the <id> part with a real id from your tasks table
GET https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/{id}
```

Example Result:
```bash
{"createdAt": "1710182225.8791468", "text": "Check for updated tasks", "id": "831618", "updatedAt": 1710182249521}
```

### Delete a Task

```bash
# Replace the <id> part with a real id from your tasks table
DELETE https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/{id}
```

No output

### Complete a task

```bash
# Replace the <id> part with a real id from your todos table
PATCH https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/{id}/complete
```

Example Result:

```bash
# Note the absense of the incomplete attribute
{"createdAt": "1710183077.8419538", "text": "Check for updated tasks attempt 3", "id": "973336", "updatedAt": 1710183087}
```

### Get all incomplete Tasks

```bash
GET https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/incomplete
```

Example Result:

```bash
[{"createdAt": "1708550605.1830018", "text": "Verify if all_incomplete function works", "id": "351684", "updatedAt": "1708550605.1830018", "incomplete": "1708550605.1830018"}]
```

### Get Tasks updated today

```bash
https://XXXXXXXXXXX.execute-api.us-east-1.amazonaws.com/tasks/updatedToday
```

Example Result:
```bash
[{"createdAt": "1710183077.8419538", "text": "Check for updated tasks attempt 3", "id": "973336", "updatedAt": 1710183087}, {"createdAt": "1710182639.9228485", "text": "Check for updated tasks attempt 2", "id": "644512", "updatedAt": 1710182928}, {"createdAt": "1708550605.1830018", "text": "Verify if all_incomplete function works", "id": "351684", "updatedAt": 1710182981}]
```

## Credits

API based off examples from:
- https://github.com/serverless/examples/tree/v3/aws-python-http-api-with-dynamodb
- https://github.com/awsdocs/aws-doc-sdk-examples
