# Invoice API (FastAPI)

A simple CRUD REST API for managing invoices, built with FastAPI. Invoice data is stored in a JSON file.

## Project Structure

```
FDEWeek1Day2HomeAssignment/
├── apis_creation/
│   ├── main.py                 # App entry point, registers all routers
│   ├── get_Invoices.py         # GET    /get-invoices
│   ├── post_invoices.py        # POST   /post-invoices
│   ├── put_invoices.py         # PUT    /put-invoices/{invoice_id}
│   ├── delete_invoices.py      # DELETE /delete-invoice/{invoice_id}
│   └── utilis/
│       ├── data_model.py       # Pydantic model for an invoice
│       └── readDataFromJson.py # Read/write helpers for the JSON file
└── data/
    └── InvoiceDataFile.json    # Invoice data storage
```

## Setup

### 1. Prerequisites

- Python 3.9 or newer
- pip

### 2. Create and activate a virtual environment

```powershell
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

(or `pip install -r requirements.txt` if your project has one)

### 4. Prepare the data file

Make sure `data/InvoiceDataFile.json` exists and contains a JSON **list** of invoices:

```json
[
    {
        "id": 101,
        "name": "John Doe",
        "amount": 2500.5,
        "status": "pending"
    }
]
```

If you are starting fresh, the file can simply contain `[]`.

## Run the Server

The data file path in `readDataFromJson.py` is relative (`../data/InvoiceDataFile.json`), so the server **must be started from inside the `apis_creation` folder**:

```bash
cd src/FDE_Week1_Day2/FDEWeek1Day2HomeAssignment/apis_creation
uvicorn main:app --reload
```

The API is now available at `http://127.0.0.1:8000`.

### Interactive documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Note: `/docs` goes directly after the host. It is not placed after an endpoint name (for example, `/post-invoices/docs` returns "Not Found").

## Invoice Model

| Field    | Type   | Description                     |
|----------|--------|---------------------------------|
| `id`     | int    | Unique invoice id               |
| `name`   | string | Customer name                   |
| `amount` | float  | Invoice amount                  |
| `status` | string | Status, e.g. `paid`, `pending`  |

## API Endpoints

| Method | Endpoint                          | Description                  | Request body |
|--------|-----------------------------------|------------------------------|--------------|
| GET    | `/get-invoices`                   | Get all invoices             | None         |
| POST   | `/post-invoices`                  | Create a new invoice         | Invoice JSON |
| PUT    | `/put-invoices/{invoice_id}`      | Update an existing invoice   | Invoice JSON |
| DELETE | `/delete-invoice/{invoice_id}`    | Delete an invoice by id      | None         |

### Status codes

| Code | Meaning                                            |
|------|----------------------------------------------------|
| 200  | Request succeeded                                  |
| 404  | Invoice id not found (PUT and DELETE)              |
| 422  | Invalid request body (missing or wrong-typed field)|
| 500  | Server error (check the terminal traceback)        |

## Sample Requests and Responses

### 1. Get all invoices

**Request**

```
GET http://127.0.0.1:8000/get-invoices
```

**Response** `200 OK`

```json
[
    {
        "id": 101,
        "name": "John Doe",
        "amount": 2500.5,
        "status": "pending"
    },
    {
        "id": 112,
        "name": "Mydhili Doe",
        "amount": 15000.0,
        "status": "paid"
    }
]
```

### 2. Create an invoice

**Request**

```
POST http://127.0.0.1:8000/post-invoices
Content-Type: application/json
```

```json
{
    "id": 112,
    "name": "Mydhili Doe",
    "amount": 15000.0,
    "status": "paid"
}
```

**Response** `200 OK`

```json
{
    "id": 112,
    "name": "Mydhili Doe",
    "amount": 15000.0,
    "status": "paid"
}
```

### 3. Update an invoice

**Request**

```
PUT http://127.0.0.1:8000/put-invoices/112
Content-Type: application/json
```

```json
{
    "id": 112,
    "name": "Mydhili Updated",
    "amount": 20000.0,
    "status": "pending"
}
```

**Response** `200 OK`

```json
{
    "id": 112,
    "name": "Mydhili Updated",
    "amount": 20000.0,
    "status": "pending"
}
```

The `id` in the URL decides which invoice is updated; the invoice's id itself is never changed.

**Response when the id does not exist** `404 Not Found`

```json
{
    "detail": "Invoice not found"
}
```

### 4. Delete an invoice

**Request**

```
DELETE http://127.0.0.1:8000/delete-invoice/112
```

**Response** `200 OK`

```json
{
    "message": "Invoice 112 deleted"
}
```

**Response when the id does not exist** `404 Not Found`

```json
{
    "detail": "Invoice not found"
}
```

## Testing with curl

```bash
# Get all
curl http://127.0.0.1:8000/get-invoices

# Create
curl -X POST http://127.0.0.1:8000/post-invoices \
  -H "Content-Type: application/json" \
  -d '{"id": 112, "name": "Mydhili Doe", "amount": 15000.0, "status": "paid"}'

# Update
curl -X PUT http://127.0.0.1:8000/put-invoices/112 \
  -H "Content-Type: application/json" \
  -d '{"id": 112, "name": "Mydhili Updated", "amount": 20000.0, "status": "pending"}'

# Delete
curl -X DELETE http://127.0.0.1:8000/delete-invoice/112
```

## Troubleshooting

| Problem | Likely cause and fix |
|---------|----------------------|
| `FileNotFoundError` for `InvoiceDataFile.json` | Server was not started from inside `apis_creation`, or the file name/location is wrong. |
| `ModuleNotFoundError` | A file or folder name does not match its import (check spelling and capitalization, e.g. `utilis`). |
| `AttributeError: 'FastAPI' object has no attribute '_contains_router'` | A router file uses `FastAPI()` instead of `APIRouter()`. Only `main.py` should use `FastAPI()`. |
| POST returns `null` | The endpoint returned the result of `list.append()`, which is `None`. Return the new invoice dict instead. |
| `/docs` shows "Not Found" | Use `http://127.0.0.1:8000/docs`, with nothing between the port and `/docs`. |
| `json.JSONDecodeError` | `InvoiceDataFile.json` is empty or not valid JSON. Use `[]` for an empty list. |
