from crewai import Task

def create_screening_task(agent, jd_text, candidates_data):
    return Task(
        description=f"Evaluate the following candidates against this Job Description:\n\nJD: {jd_text}\n\nCandidates Data:\n{candidates_data}\n\nFor each candidate, assign a score out of 10 and write a brief pro/con summary.",
        expected_output="A list of candidates with their scores (out of 10) and a brief pro/con summary for each.",
        agent=agent
    )

def create_ranking_task(agent):
    return Task(
        description="Review the previous evaluation and rank the candidates from best to worst. Provide a final shortlist of the top candidates.",
        expected_output="A ranked list of the top candidates with detailed reasoning for why they are the best fit.",
        agent=agent
    )

def create_scheduling_task(agent, candidate_info):
    return Task(
        description=f"Schedule an interview for the following approved candidate: {candidate_info}. Extract their name and email, and use the Schedule Interview tool.",
        expected_output="Confirmation of the scheduled interview time.",
        agent=agent
    )

def create_email_task(agent, candidate_info):
    return Task(
        description=f"Draft and send an interview invitation email to the following candidate: {candidate_info}. Mention their scheduled time. Extract their email and use the Send Email tool.",
        expected_output="Confirmation that the email was sent.",
        agent=agent
    )

def create_tracking_task(agent, candidate_info):
    return Task(
        description=f"Update the tracking spreadsheet to mark the following candidate as 'Interview Scheduled': {candidate_info}. Use the Update Tracking Sheet tool.",
        expected_output="Confirmation that the spreadsheet was updated.",
        agent=agent
    )
