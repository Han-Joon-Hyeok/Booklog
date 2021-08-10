# from django.shortcuts import render

# # Create your views here.

# ========= 기존에 코드가 재대로 실행이 안되었던 부분입니다.(기존작업물 업로드) ==========

from django.shortcuts import render
from .models import Follow, MyUser, Like ### 이 부분 수정 필요 ###
 
from django.http import JsonResponse
from django.views import View
import json
# Create your views here.

class FollowView(View) :
    @login_decorator
    def post(self, request) :
        data = json.loads(request.body)
        try:
            follower = request.user.id
            following = data['following']

            follower_id = MyUser.objects.get(id=follower)
            following_id = MyUser.objects.get(id=following)

            if not follower : 
                return JsonResponse({"message":"INVALID_ID"}, status=400)
            if not following :
                return JsonResponse({"message":"INVALID_APPROACH"})
            
            #Unfollow
            if Follow.objects.filter(follower=follower_id, following=following_id).exists():
                Follow.objects.filter(follower=follower_id, following=following_id).delete
                return JsonResponse({"message":"DELETE_SUCCESS"}, status=200)

            #Follow
            Follow.objects.create(
                follower=follower_id,
                following=following_id
            )
            return JsonResponse({"message":"CREATE_SUCCESS"}, status=200)

        except KeyError :
            return JsonResponse({'message':"KEY_ERROR"}, status=400)

class LikeView(View) :
    @login_decorator
    def get(self, request) :
        try:
            likes = Like.objects.all()
            like_list = []

            for like in likes :
                like_list.append(
                    {
                        "like_username" : request.myuser.username, 
                        "posting" : like.posting.id, 
                        "liked_at" : like.liked_at
                    }
                )
                return JsonResponse({'data': like_list}, status=200)

        except KeyError :
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

    @login_decorator
    def post(self, request) :
        data = json.loads(request.body)

        try:
            user_id = data.get(request.user, None)
            posting_id = data.get("posting", None)

            if MyUser.objects.filter(id=user_id).exists() :
                like_username = MyUser.objects.get(id=user_id)
                if Posting.objects.filter(id=posting_id).exists():
                    posting = Posting.objects.get(id=posting_id)

                    Like.objects.create(
                        like_username=like_username,
                        posting = posting,
                    )   
                    return JsonResponse({"message":"SUCCESS"}, status=200)
                return JsonResponse({"message":"INVALID_POST"}, status=400)
            return JsonResponse({"message":"INVALID_USER"}, status=400)
            
        except KeyError :
            return JsonResponse({"message":"KEY_ERROR"}, status=400)