from django.shortcuts import render
from rest_framework.decorators import api_view #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework import viewsets, status #type: ignore
from rest_framework.throttling import AnonRateThrottle #type: ignore
from .serializers import ProfileSerializer
from .models import Profile

import datetime, time, requests, json, logging

# Create your views here.
# @api_view()
# def ProfileView(request):
#     cats_api = 'https://catfact.ninja/fact'
#     response = requests.get(cats_api)
#     # fact = json.loads(response.text)['fact']
#     profiles = Profile.objects.all()
#     serializer = ProfileSerializer(profiles, many=True)
#     for i in serializer.data:
#         return Response({
#             'status': 'success',
#             'user': i,
#             'timestamp': datetime.datetime.fromtimestamp(time.time()).isoformat(),
#             # 'fact': fact
#             })

logger = logging.getLogger(__name__)

class ProfileView(viewsets.ViewSet):
    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)

        throttle_classes = [AnonRateThrottle]

        try:
            cats_api = 'https://catfact.ninja/fact'
            logger.debug("Attempting to access external service at '{cats_api}'")
            response = requests.get(cats_api, timeout=5)
            response.raise_for_status()
            logger.info(f"Received requested data: {response.json()}")
            fact = json.loads(response.text)['fact']

            for i in serializer.data:
                return Response({
                    'status': 'success',
                    'user': i,
                    'timestamp': datetime.datetime.fromtimestamp(time.time()),
                    'fact': fact
                    }, status=status.HTTP_200_OK)
            
        except requests.exceptions.Timeout:
            logger.exception(f"Request from '{cats_api}' timed out")
            return Response({
                'detail': 'External request service timed out'
                }, status=status.HTTP_504_GATEWAY_TIMEOUT)
            
        except requests.exceptions.RequestException as e:
            logger.exception(f"Service at '{cats_api}' is unvailable")
            return Response({
                'detail': f'An error occured while connecting to the external service: {e}'
            }, status = status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except requests.exceptions.HTTPError as e:
            logger.exception(f"External service returned an error: {e}")
            return Response({
                'detail': 'External service returned an error',
                'status-code': e.response.status_code
            }, status=e.response.status_code)
            