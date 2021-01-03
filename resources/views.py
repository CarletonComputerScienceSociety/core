from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import JobPosting
from .serializers import JobPostingSerializer, JobPostingCreateSerializer

@csrf_exempt
def JobPostingList(request):
    """
    List all job postings, or create a new job posting.
    """
    if request.method == 'GET':
        job_postings = JobPosting.objects.filter(status='p')
        serializer = JobPostingSerializer(job_postings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['status'] = 's' # status must be suggested as this will be coming from students and must be approved by an admin first
        serializer = JobPostingCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def JobPostingDetails(request, pk):
    """
    Retrieve, update or delete a job posting.
    """
    try:
        job_posting = JobPosting.objects.get(pk=pk)
    except JobPosting.DoesNotExist:
        return HttpResponse(status=500)

    if request.method == 'GET':
        serializer = JobPostingSerializer(job_posting)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        # serializer = JobPostingSerializer(job_posting, data=data)
        # if serializer.is_valid():
        #    serializer.save()
        #    return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return HttpResponse(status=404)

    elif request.method == 'DELETE':
        # job_posting.delete()
        # return HttpResponse(status=204)
        return HttpResponse(status=404)