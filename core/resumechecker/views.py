from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .serializer import JobDescriptionSerializer, JobDescription, ResumeSerializer, Resume
from .analyzer import process_resume


# API to get all job descriptions
class JobDescriptionAPI(APIView):
    def get(self, request):
        queryset = JobDescription.objects.all()
        serializer = JobDescriptionSerializer(queryset, many=True)
        return Response({
            'status': True,
            'data': serializer.data
        })


# API to analyze uploaded resume against job description
class AnalyzeResumeAPI(APIView):
    def post(self, request):
        try:
            data = request.data

            # Check if 'job_description' is present
            if not data.get('job_description'):
                return Response({
                    'status': False,
                    'message': 'job description is required!',
                    'data': {}
                })

            # Validate and save resume data (resume file + job_description FK)
            serializer = ResumeSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'errors',
                    'data': serializer.errors
                })

            resume_instance = serializer.save()

            # Extract resume file path
            resume_path = resume_instance.resume.path

            # Get job description text from DB using ID
            job_desc_obj = JobDescription.objects.get(id=data.get('job_description'))
            job_desc_text = job_desc_obj.job_description

            # Process resume using your analyzer
            analysis_data = process_resume(resume_path, job_desc_text)

            return Response({
                'status': True,
                'message': 'resume analyzed',
                'data': analysis_data
            })

        except Exception as e:
            return Response({
                'status': False,
                'message': str(e),
                'data': {}
            })


def frontend_view(request):
    return render(request, 'resumechecker/frontend.html')
