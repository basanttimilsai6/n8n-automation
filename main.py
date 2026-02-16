from pathlib import Path
from fastapi import FastAPI
from git import Repo
import random

app = FastAPI()

PROJECT_PATH = Path(__file__).parent.resolve()


@app.get("/update")
def auto():
    # Create or update test.txt inside project folder
    file_path = PROJECT_PATH / "test.txt"

    with open(file_path, "w") as f:
        f.write(str(random.randint(1, 100)))

    repo = Repo(PROJECT_PATH)

    commit_message = "Auto commit from automation"

    # git add .
    repo.git.add(".")

    # git commit -m "message"
    repo.index.commit(commit_message)

    # git push origin main
    repo.git.push("origin", "main")

    return {"status": "Code updated and pushed"}
