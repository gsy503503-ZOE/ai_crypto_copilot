# Sprint 4 Review: Transaction Ledger Foundation

## Sprint Goal

Build a transaction ledger foundation for AI Crypto Ledger Copilot.

By the end of Sprint 4, the backend can create, list, update, delete, filter, and summarize wallet transaction records.

## What I Built

- Created a SQLAlchemy transaction model.
- Created transaction request and response schemas.
- Added transaction creation and listing endpoints.
- Added wallet and category filters.
- Added transaction detail lookup by id.
- Added transaction note and category update endpoints.
- Added transaction deletion.
- Added category validation and normalization.
- Moved transaction category logic into the service layer.
- Added a transaction summary endpoint.
- Added aggregate metrics:
  - total transaction count
  - total token amount
  - total USD value
  - average USD value
  - largest transaction USD value
  - category distribution
- Added an empty state message for filtered summary results.

## Core API Endpoints

- `POST /transactions`
- `GET /transactions`
- `GET /transactions/{transaction_id}`
- `DELETE /transactions/{transaction_id}`
- `PATCH /transactions/{transaction_id}/note`
- `PATCH /transactions/{transaction_id}/category`
- `GET /transactions/summary`

## Concepts I Learned

### Transaction Ledger

A transaction ledger is a structured record of wallet activity.
It helps users understand what happened in a wallet over time.

### SQLAlchemy Model

A SQLAlchemy model maps a Python class to a database table.
In this sprint, the `Transaction` model represents the `transactions` table.

### Schema

A schema defines the shape of request and response data.
I used Pydantic schemas to define transaction input and output.

### Query Parameter

A query parameter is used to filter API results.
Example:
```text
/transactions?category=swap
```

### Path Parameter

A path parameter is part of the URL path.
Example:
```text
/transactions/1
```
Here, 1 is the transaction id.

### PATCH

PATCH is used to partially update an existing resource.
I used PATCH to update only the note or category of a transaction.

### DELETE

DELETE is used to remove a resource.
I used DELETE to remove a transaction by id.

### Validation

Validation means checking whether user input is acceptable before saving it.
I validated transaction categories to avoid messy data like swapp, Swap, or abc.

### Normalization

Normalization means converting user input into a standard format.
Example:
```text
" Swap " -> "swap"
```

### Aggregation

Aggregation means calculating summary information from many records.
In this sprint, I calculated total value, average value, largest transaction value, and category counts.

### Empty State

An empty state is the response shown when no data matches the selected filters.
It helps the frontend show a clear message to users.

## Problems I Encountered

I learned that opening a PATCH endpoint directly in the browser causes Method Not Allowed, because the browser sends GET by default.
I learned that deleting a transaction removes it from the database, so updating its note later will return Transaction not found.
I learned that different summary URLs return different results because each URL asks a different filtered question.
I learned that route order matters in FastAPI. /summary should be placed before /{transaction_id}.
I learned that input data should be validated before being saved to the database.