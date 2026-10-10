import os 
from pathlib import Path
# ライブラリ調べておく

# 環境変数のキーを取得
# os.ebvuron['キー名']
os.environ["TEST_DB"] = "test.db"
for p in Path(".").glob("practice_todo.db*"):   # -wal, -shm も含めて消す
    p.unlink()
 
from db/feature-db/todo.py import models as m  # noqa: E402