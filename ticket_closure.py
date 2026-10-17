import pandas as pd
from datetime import datetime

file_path = "Password_Reset_Requests.xlsx"

df = pd.read_excel(file_path, dtype=str)
df = df.fillna("")

for index, row in df.iterrows():

    status = row["Status"].strip()
    print("Ticket:", row["TicketID"])
    print("Status:", status)
    print("ResolvedDate:", row["ResolvedDate"])
    print("----------------")

    if status == "Resolved" and row["ResolvedDate"].strip() == "":

        resolved_date = datetime.now()

        df.loc[index, "ResolvedDate"] = resolved_date.strftime("%Y-%m-%d %H:%M:%S")

        created_date = datetime.strptime(
            row["CreatedDate"],
            "%Y-%m-%d %H:%M:%S"
        )

        resolution_hours = round(
            (resolved_date - created_date).total_seconds() / 3600,
            2
        )

        df.loc[index, "ResolutionTimeHours"] = str(resolution_hours)
        df.loc[index, "TicketState"] = "Closed"

        print(
            f"Closed {row['TicketID']} "
            f"in {resolution_hours} hours"
        )

df.to_excel(file_path, index=False)

print("Closure processing complete.")
