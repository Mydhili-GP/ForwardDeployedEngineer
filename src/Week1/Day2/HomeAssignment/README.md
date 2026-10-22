# Invoice Management API

A simple REST API built with **FastAPI** that performs CRUD (Create, Read, Update, Delete) operations on invoices. Data is stored in a local JSON file, so no database setup is needed.

---

## Features

- View all invoices or a single invoice by its number
- Create a new invoice
- Update an existing invoice
- Delete an invoice
- Automatic request validation using Pydantic
- Auto-generated interactive API docs (Swagger UI)

---

## Tech Stack

- Python 3.9+
- FastAPI
- Pydantic
- Uvicorn (ASGI server)

---

## Project Structure

```
HomeAssignment/
├── main.py                    # App entry point, registers all routers
├── data_model.py              # Pydantic model (InvoiceBaseModel)
├── Fetch_data_fromjson.py     # load() and writeData() helpers for the JSON file
├── Request/
│   ├── get_request.py         # GET endpoints
│   ├── post_request.py        # POST endpoint
│   ├── put_request.py         # PUT endpoint
│   └── delete_request.py      # DELETE endpoint
└── data/
    └── Invoices.json          # JSON file acting as the database
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

### 4. Configure the data file path

In `Fetch_data_fromjson.py`, update the file path so it points to `Invoices.json` on your machine.

### 5. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Documentation

Once the server is running, open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/get_request` | Get all invoices |
| GET | `/get_request/{invoice_id}` | Get a single invoice by its number |
| POST | `/invoices` | Create a new invoice |
| PUT | `/invoices/{invoice_id}` | Replace an existing invoice |
| DELETE | `/invoices/{invoice_id}` | Delete an invoice |

---

## Data Model

```json
{
    "invoice_number": "INC-001",
    "date": "2026-10-01",
    "paymentStatus": "Paid",
    "name": "Arjun Kumar"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `invoice_number` | string | Unique invoice identifier |
| `date` | string | Invoice date (YYYY-MM-DD) |
| `paymentStatus` | string | e.g. `Paid` or `Pending` |
| `name` | string | Customer name |

---

## Example Requests

**Create an invoice**

```bash
curl -X POST "http://127.0.0.1:8000/invoices" \
  -H "Content-Type: application/json" \
  -d '{"invoice_number": "INC-008", "date": "2026-10-20", "paymentStatus": "Pending", "name": "Anita Rao"}'
```

**Get all invoices**

```bash
curl "http://127.0.0.1:8000/get_request"
```

**Update an invoice**

```bash
curl -X PUT "http://127.0.0.1:8000/invoices/INC-008" \
  -H "Content-Type: application/json" \
  -d '{"invoice_number": "INC-008", "date": "2026-10-21", "paymentStatus": "Paid", "name": "Anita Rao"}'
```

**Delete an invoice**

```bash
curl -X DELETE "http://127.0.0.1:8000/invoices/INC-008"
```

---

## Known Issues

This is a learning project, and a few things are worth improving:

- **Inconsistent key names:** the JSON file and some endpoints use `invoiceNumber`, while the model and others use `invoice_number`. This causes some records to be unfindable by certain endpoints.
- **Not-found responses return HTTP 200** in PUT and DELETE instead of 404.
- **No duplicate check** when creating invoices.
- **Hardcoded absolute file path** in `Fetch_data_fromjson.py`.
- **No concurrency safety** for simultaneous file writes.
- `date` and `paymentStatus` are not validated beyond being strings.

---

## Future Improvements

- Unify the invoice key name across the data, model, and all routes
- Return proper 404 errors for missing invoices
- Validate dates and restrict `paymentStatus` to allowed values
- Prevent duplicate invoice numbers
- Replace the JSON file with a real database (SQLite / PostgreSQL)
- Add automated tests

---

## License

This project is for learning purposes. Add a license of your choice if you plan to share it.
