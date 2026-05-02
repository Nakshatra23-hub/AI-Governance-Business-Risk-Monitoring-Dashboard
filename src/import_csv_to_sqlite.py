import pandas as pd
import sqlite3

df = pd.read_csv("AI_Model_Governance_Log.csv")

conn = sqlite3.connect("AIGovernanceDB.db")

df.to_sql("AI_Model_Governance_Log", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")