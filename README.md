Legacy Modernization using fake DB2 data

Python replacing the UI layer
COBOL logic being “exposed”
Ready for later connection to z/OS Connect


Project Structure

fastapi-legacy-app/
│
├── app.py              ← main FastAPI app
├── models.py           ← data models (like copybook)
├── service.py          ← business logic (simulated COBOL)
├── database.py         ← fake DB2 data
└── requirements.txt
