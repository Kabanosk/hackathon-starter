# Usage of the model folder

## Database class
The database class is a class that is used to interact with the database using connections.

## Usage
To use it import it in any file and create an instance of the class

```python
from src.model.utils import Database

db = Database()
conn = db.create_connection()
```

Then you can use the `conn` object to interact with the database using:
```python
from src.model.utils import Database

db = Database()
conn = db.create_connection()

conn.execute("SELECT * FROM table")
conn.execute("INSERT INTO table VALUES (value1, value2)")
```
