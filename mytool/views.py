from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
	return HttpResponse("hello world")


myhtml = '''
<html>
<h1> my lti tool </h1>
<p> some text </p>

<iframe src="https://www.bing.com" width="500" height="200">
</iframe>

</html>
'''


@csrf_exempt
def lti_launch(request):
	return HttpResponse(myhtml)

	# return HttpResponse("hello this is the lti tool")