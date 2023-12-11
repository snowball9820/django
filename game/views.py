from django.shortcuts import render
# from django.http import HttpResoponse
import fopenaiAPI1
import audioplay
import ThreadAPI


# Create your views here.

tour_assistant_id = 'asst_TnG0mButeYqtGKKgTZ5hmbFj'
TOUR_ASSISTANT_ID = tour_assistant_id  # or a hard-coded ID like "asst-..."

def gamepage(request):
    if request.method=='POST':
        user_input=request.POST.get('user_input','')
        ans=fopenaiAPI1.qna(user_input)
        return render(request,'GPTinput.html',{'Data':ans})

    return render(request, 'GPTinput.html')

def threadtest(request):
    thread1, run1=ThreadAPI.create_thread_and_run(
        #"부산에서 관광할 만한 다섯곳을 추천해주세요"
        )
    run1=ThreadAPI.wait_on_run(run1, thread1)

    if request.method=='POST':
        user_input=request.POST.get('user_input','')

        run2=ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread1, user_input)
        run2=ThreadAPI.wait_on_run(run2, thread1)
        ans=ThreadAPI.get_response(thread1)

        return render(request,'GPTinput2.html',{'Data':ans})

    return render(request, 'GPTinput2.html')

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

