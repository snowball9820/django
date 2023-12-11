from openai import OpenAI
import time

client = OpenAI(api_key = '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')


#https://platform.openai.com/assistants 이 사이트에서 Assistant 관리
tour_assistant_id = 'asst_Uk29P8rZJo2fcYLHzUNxRVU6'
TOUR_ASSISTANT_ID = tour_assistant_id  # or a hard-coded ID like "asst-..."

#최초 thread를 만들고 메시지를 연결한 후 답을 구한다 
def create_thread_and_run(user_input):
    thread = client.beta.threads.create()
    run = submit_message(TOUR_ASSISTANT_ID, thread, user_input)
    return thread, run


#해당 메시지를 대화 thread에 연결시키고 메시지의 답을 구한다.
def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

#현재 thread의 메시지 전체를 출력한다
def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")


# Pretty printing helper
def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()


#답을 가져올 때까지 기다리는 함수
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

thread1, run1 = create_thread_and_run(
    "부산에서 관광할 만한 다섯곳 추천해주세요"
)
run1 = wait_on_run(run1, thread1)
pretty_print(get_response(thread1))

run2 = submit_message(TOUR_ASSISTANT_ID, thread1, "첫번째 장소를 추천한 이유는?")
run2 = wait_on_run(run2, thread1)
pretty_print(get_response(thread1))