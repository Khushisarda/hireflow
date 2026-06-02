from crewai import Agent
from tools.mock_tools import schedule_interview_tool, send_email_tool, update_tracking_sheet_tool

def get_screener_agent():
    return Agent(
        role="Resume Screener",
        goal="Extract text from resumes and evaluate candidates against the Job Description.",
        backstory="You are an expert technical recruiter who can quickly spot if a candidate meets the requirements based on their resume.",
        verbose=True,
        allow_delegation=False
    )

def get_ranker_agent():
    return Agent(
        role="Candidate Ranker",
        goal="Review the evaluation of all candidates and rank them, selecting the best ones.",
        backstory="You are a Hiring Manager who strictly evaluates candidate profiles to find the top talent.",
        verbose=True,
        allow_delegation=False
    )

def get_scheduler_agent():
    return Agent(
        role="Interview Scheduler",
        goal="Schedule interviews for approved candidates on the Google Calendar.",
        backstory="You are a recruitment coordinator who efficiently schedules interviews.",
        verbose=True,
        allow_delegation=False,
        tools=[schedule_interview_tool]
    )

def get_email_agent():
    return Agent(
        role="Email Communicator",
        goal="Send personalized interview invitations to candidates.",
        backstory="You are a professional HR associate whose emails are always polite, clear, and welcoming.",
        verbose=True,
        allow_delegation=False,
        tools=[send_email_tool]
    )

def get_tracker_agent():
    return Agent(
        role="ATS Tracker",
        goal="Log candidate progress and scheduled interview times in the tracking spreadsheet.",
        backstory="You are a meticulous HR data entry specialist who keeps the ATS (Applicant Tracking System) spreadsheet up to date.",
        verbose=True,
        allow_delegation=False,
        tools=[update_tracking_sheet_tool]
    )
