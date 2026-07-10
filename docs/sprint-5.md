# Sprint 5 Review: Transaction Labeling

## Sprint Goal

Build transaction labeling for AI Crypto Ledger Copilot.

By the end of Sprint 5, the backend can save labels on transactions, validate labels, update labels, filter transactions by label, summarize label distribution, and suggest labels from transaction data.

## What I Built

- Added transaction labels.
- Added allowed label validation.
- Added label normalization.
- Added duplicate label removal.
- Added label storage conversion between list and string.
- Added labels to transaction create and response schemas.
- Added a transaction labels update endpoint.
- Added label filtering for transaction lists.
- Added label filtering for transaction summaries.
- Added label distribution in summary metrics.
- Added label options endpoint.
- Added rule-based label suggestions.
- Fixed transaction timestamp schema from string to datetime.
- Added transaction label service checks.

## Core API Endpoints

- `POST /transactions`
- `GET /transactions?label=defi`
- `GET /transactions/summary?label=defi`
- `GET /transactions/labels/options`
- `PATCH /transactions/{transaction_id}/labels`
- `GET /transactions/{transaction_id}/labels/suggestions`

## Supported Labels

- `defi`
- `cex`
- `stablecoin`
- `large_transaction`
- `small_transaction`
- `income`
- `expense`
- `gas`
- `nft`
- `bridge`
- `staking`
- `airdrop`

## Example Label Update

```json
{
  "labels": ["defi", "stablecoin", "large_transaction"]
}
```

## Concepts I Learned

### Label

A label is a tag that adds extra meaning to a transaction.
A transaction can have multiple labels.
Example:

```text
category: swap
labels: defi, stablecoin, large_transaction
```

### Category vs Label

A category is the main transaction type.
A label is extra context.
For example, a transaction can have category swap and labels defi and stablecoin.

### Normalization

Normalization means converting input into a standard format.
Example:

```text
" DeFi " -> "defi"
```

### Validation

Validation means checking whether user input is allowed.
For example, defi is allowed, but bad_label is rejected.

### Storage Conversion
The API uses labels as a list.

```text
["defi", "stablecoin"]
```

The database stores labels as a string.

```text
defi,stablecoin
```

The backend converts between these two formats.

### Query Parameter

A query parameter is a value passed after ? in a URL.
Example:

```text
/transactions?label=defi
```

### Label Suggestion
Label suggestion means the backend recommends labels based on transaction data.
Example rules:

```text
swap can suggest defi
USDC can suggest stablecoin
value_usd >= 10000 can suggest large_transaction
```

## Problems I Encountered

I learned that Python 3.9 does not support the str | None type syntax.
I fixed it by using:

```json
Optional[str]
```

I also learned that SQLAlchemy DateTime fields need Python datetime objects, not plain strings.
I fixed the timestamp schema by changing:

```json
timestamp: Optional[str]
```

to:

```json
timestamp: Optional[datetime]
```

## What I Learned
Labels are different from categories because one transaction can have many labels.
Pydantic schemas define API input and output data shapes.
model_dump() converts a Pydantic model into a Python dictionary.
SQLAlchemy query filter() works like SQL WHERE.
A backend often needs to convert data between database format and API response format.
Small service-layer tests can protect business rules from breaking.