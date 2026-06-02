from crewai import Crew, Process
from agents import get_screener_agent, get_ranker_agent, get_scheduler_agent, get_email_agent, get_tracker_agent
from tasks import create_screening_task, create_ranking_task, create_scheduling_task, create_email_task, create_tracking_task

def run_evaluation_crew(jd_text, candidates_data):
    screener = get_screener_agent()
    ranker = get_ranker_agent()

    task1 = create_screening_task(screener, jd_text, candidates_data)
    task2 = create_ranking_task(ranker)

    crew = Crew(
        agents=[screener, ranker],
        tasks=[task1, task2],
        process=Process.sequential
    )

    result = crew.kickoff()
    return result

def run_post_approval_crew(candidate_info):
    scheduler = get_scheduler_agent()
    email_agent = get_email_agent()
    tracker = get_tracker_agent()

    task1 = create_scheduling_task(scheduler, candidate_info)
    task2 = create_email_task(email_agent, candidate_info)
    task3 = create_tracking_task(tracker, candidate_info)

    crew = Crew(
        agents=[scheduler, email_agent, tracker],
        tasks=[task1, task2, task3],
        process=Process.sequential
    )

    result = crew.kickoff()
    return result
