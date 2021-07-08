from pydantic import BaseModel
from typing import Any

event = {"name": "Amin", "study": True, "work": False, "price": 50}
event_db: dict[Any, Any] = {}

if "__getitem__" in dir(event):
    print("Found")
for var, value in event.items():
    print("Var ", var)
    print("value ", value)
    setattr(event_db, var, value) if value else None

    # setattr(event_db, var, value) if value else None

print(event_db)
