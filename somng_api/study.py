from pydantic import BaseModel





event = {"name": "Amin", "study": True, "work": False, "price": 50}
if "__getitem__" in dir(event):
    print("Found")
for var, value in event.items():
    print("Var ", var)
    print("value ", value)

    # setattr(event_db, var, value) if value else None
