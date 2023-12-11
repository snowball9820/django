from django.shortcuts import render
# from django.http import HttpResoponse
import fopenaiAPI1
import audioplay
import ThreadAPI


# Create your views here.

tour_assistant_id = 'asst_Uk29P8rZJo2fcYLHzUNxRVU6'
TOUR_ASSISTANT_ID = tour_assistant_id  # or a hard-coded ID like "asst-..."

def gamepage(request):
    if request.method=='POST':
        user_input=request.POST.get('user_input','')
        ans=fopenaiAPI1.qna(user_input)
        return render(request,'GPTinput.html',{'Data':ans})

    return render(request, 'GPTinput.html')

# def threadtest(request):
#     thread1, run1=ThreadAPI.create_thread_and_run(
#         "부산에서 관광할 만한 다섯곳을 추천해주세요"
#         )
#     run1=ThreadAPI.wait_on_run(run1, thread1)

#     if request.method=='POST':
#         user_input=request.POST.get('user_input','')

#         run2=ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread1, user_input)
#         run2=ThreadAPI.wait_on_run(run2, thread1)
#         ans=ThreadAPI.get_response(thread1)

#         return render(request,'GPTinput2.html',{'Data':ans})

#     return render(request, 'GPTinput2.html')

#이게 실행되는 함수
# def threadtest(request):
#     # 기존 스레드와 실행 객체를 저장할 변수
#     thread = None
#     run = None

#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '')

#         # 처음 요청이거나 스레드가 없을 경우 새 스레드 생성
#         if not thread or not run:
#             thread, run = ThreadAPI.create_thread_and_run(
#                 "부산에서 관광할 만한 다섯곳을 추천해주세요"
#             )
#             run = ThreadAPI.wait_on_run(run, thread)

#         # 이전 질문을 기억하여 새 질문에 추가
#         response = ThreadAPI.get_response(thread)
#         if response and isinstance(response, list) and len(response) > 0:
#             previous_question = response[-1].content[0].text.value
#         else:
#          # 적절한 오류 처리 또는 대체 로직
#         # previous_question = ThreadAPI.get_response(thread)[-1].content[0].text.value
#          user_input = f"{previous_question} {user_input}"

#         # 새 질문 보내기
#         run = ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread, user_input)
#         run = ThreadAPI.wait_on_run(run, thread)

#         # 답변과 이전 질문, 현재 질문을 템플릿에 전달
#         ans = ThreadAPI.get_response(thread)
#         return render(request, 'GPTinput2.html', {
#             'Data': ans,
#             'previous_question': previous_question,
#             'current_question': user_input,
#         })

#     # 처음 접속 시 새 스레드 생성
#     thread, run = ThreadAPI.create_thread_and_run(
#         "부산에서 관광할 만한 다섯곳을 추천해주세요"
#     )
#     run = ThreadAPI.wait_on_run(run, thread)

#     # 빈 답변과 빈 질문을 템플릿에 전달
#     ans = ThreadAPI.get_response(thread)
#     return render(request, 'GPTinput2.html', {
#         'Data': ans,
#         'previous_question': '',
#         'current_question': '',
#     })

#성공입니다....눈물납니다...

def threadtest(request):
    # 기존 스레드와 실행 객체를 저장할 변수
    thread = None
    run = None
    previous_question = ''  # 여기에서 previous_question 초기화

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        # 처음 요청이거나 스레드가 없을 경우 새 스레드 생성
        if not thread or not run:
            thread, run = ThreadAPI.create_thread_and_run(
                "부산에서 관광할 만한 다섯곳을 추천해주세요"
            )
            run = ThreadAPI.wait_on_run(run, thread)

        # 이전 질문을 기억하여 새 질문에 추가
        response = ThreadAPI.get_response(thread)
        if response and isinstance(response, list) and len(response) > 0:
            previous_question = response[-1].content[0].text.value
            user_input = f"{previous_question} {user_input}"  # 여기로 이동

        # 새 질문 보내기
        run = ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread, user_input)
        run = ThreadAPI.wait_on_run(run, thread)

        # 답변과 이전 질문, 현재 질문을 템플릿에 전달
        ans = ThreadAPI.get_response(thread)
        return render(request, 'GPTinput2.html', {
            'Data': ans,
            'previous_question': previous_question,
            'current_question': user_input,
        })

    # 처음 접속 시 새 스레드 생성
    else:
        thread, run = ThreadAPI.create_thread_and_run(
            "부산에서 관광할 만한 다섯곳을 추천해주세요"
        )
        run = ThreadAPI.wait_on_run(run, thread)

        # 빈 답변과 빈 질문을 템플릿에 전달
        ans = ThreadAPI.get_response(thread)
        return render(request, 'GPTinput2.html', {
            'Data': ans,
            'previous_question': previous_question,
            'current_question': '',
        })



def datatest(request):
    context = {'Person1':'설렁탕', 'Person2': '비빔밥', 'Person3': '삼겹살'}
    return render(request, 'datatest.html', context)

def fortest(request):
    lst1 = ['banana', 'apple', 'orange']
    context = {'Person1':'설렁탕', 'Person2': '비빔밥', 'Person3': lst1}
    return render(request, 'fortest.html', context)

def mediatest(request):
    audioplay.play()
    lst1 = {'banana', 'apple', 'orange'}
    context = {'Person1':'설렁탕', 'Person2': '비빔밥', 'Person3': lst1}
    return render(request, 'fortest.html', context)

