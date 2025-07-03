import uuid
import time
from datetime import datetime, UTC

def get_random_string_and_log():
    random_string = str(uuid.uuid4())
    
    while True:
        timestamp = datetime.now(UTC).isoformat()
        print(f"{timestamp}: {random_string}")
        time.sleep(5)

if __name__ == "__main__":
    get_random_string_and_log()