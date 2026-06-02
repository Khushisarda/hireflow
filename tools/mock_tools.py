from langchain.tools import tool

@tool("Schedule Interview")
def schedule_interview_tool(candidate_name: str, candidate_email: str) -> str:
    """Useful to schedule an interview on Google Calendar. Returns the scheduled time."""
    print(f"[MOCK CALENDAR] Scheduling interview for {candidate_name}")
    return f"Successfully scheduled interview for {candidate_name} ({candidate_email}) on Next Tuesday at 10:00 AM."

@tool("Send Email")
def send_email_tool(to_email: str, subject: str, body: str) -> str:
    """Useful to send an email via Gmail API."""
    print(f"[MOCK GMAIL] Sending email to {to_email}")
    return f"Successfully sent email to {to_email} with subject '{subject}'."

@tool("Update Tracking Sheet")
def update_tracking_sheet_tool(candidate_name: str, status: str, notes: str) -> str:
    """Useful to update the Google Sheet tracking candidates."""
    print(f"[MOCK SHEETS] Updating sheet for {candidate_name}")
    return f"Updated Google Sheet: Added {candidate_name} with status '{status}'."
