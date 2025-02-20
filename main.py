from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Banco de dados simulado
crm_data = []
notifications = []
logs = []

# Modelos de dados
class CRMEntry(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    notes: str

class Notification(BaseModel):
    id: int
    message: str
    timestamp: str

class LogEntry(BaseModel):
    id: int
    event: str
    details: str
    timestamp: str

# Rotas da API
@app.get("/")
def read_root():
    return {"message": "Zapify Backend API Running"}

# CRM Endpoints
@app.get("/crm")
def get_crm():
    return crm_data

@app.post("/crm")
def add_crm_entry(entry: CRMEntry):
    crm_data.append(entry.dict())
    return {"message": "Entry added", "data": entry}

# Notificações Endpoints
@app.get("/notifications")
def get_notifications():
    return notifications

@app.post("/notifications")
def add_notification(notification: Notification):
    notifications.append(notification.dict())
    return {"message": "Notification added", "data": notification}

# Logs Endpoints
@app.get("/logs")
def get_logs():
    return logs

@app.post("/logs")
def add_log(log_entry: LogEntry):
    logs.append(log_entry.dict())
    return {"message": "Log added", "data": log_entry}

# Iniciar servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
