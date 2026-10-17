import pandas as pd
from datetime import datetime
import uuid

file_path = "Password_Reset_Requests.xlsx"

# Force all columns to text
df = pd.read_excel(file_path, dtype=str)

# Replace blank values
df = df.fillna("")

for index, row in df.iterrows():

    if row["TicketID"].strip() == "":

        ticket_id = "PR-" + str(uuid.uuid4())[:8].upper()

        issue_type = str(row["IssueType"]).strip()

        if issue_type == "MFA Issue":
            assigned_to = "Security Team"
            priority = "High"
        elif issue_type == "Other":
            assigned_to = "Level 2 Support"
            priority = "Medium"
        else:
            assigned_to = "Level 1 Support"
            priority = "Low"

        df.loc[index, "TicketID"] = ticket_id
        df.loc[index, "Status"] = "New"
        df.loc[index, "TicketState"] = "Open"
        df.loc[index, "AssignedTo"] = assigned_to
        df.loc[index, "CreatedDate"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.loc[index, "Priority"] = priority
        df.loc[index, "SubmitDate"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.loc[index, "CreatedDate"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Created {ticket_id} -> {assigned_to}")

df.to_excel(file_path, index=False)

print("Ticket processing complete.")
