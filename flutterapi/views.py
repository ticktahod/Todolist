from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

# GET Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() # ดึงข้อมูลจาก Todolist ใน models มาทั้งหมด
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# POST Data(Save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)  

# update Data
@api_view(['PUT'])
def update_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# DELETE Data
@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)

        

data = [
    {
        "title":"IZ*ONE",
        "subtitle":"ประวัติของวง",
        "image_url":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/izone1.png",
        "detail":"IZ*ONE (Korean: 아이즈원, Japanese: アイズワン, pronounced as Eyes One) was a South Korean-Japanese girl group formed by CJ E&M through the 2018 Mnet reality competition television show Produce 48.\n\nThe group was managed by Stone Music subsidiary Off the Record and Swing Entertainment as a sub-agency in South Korea, and AKS in Japan.\n\nThe name combines the words 'IZ' (Pronounced as Eyes) which symbolizes the number '12' and 'ONE' which means '1' referring to the fact that the twelve members together will be one in the group. The asterisk (*) between 'IZ' and 'ONE' symbolizes the astrological signs of the zodiac.",
        "image_etc":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/izone2.jpg"
    },
    {
        "title":"Members",
        "subtitle":"ประวัติสมาชิกเเต่ละคน",
        "image_url":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/member1.png",
        "detail":"The group was composed of twelve members, chosen by live votes: Jang Won Young, Miyawaki Sakura, Jo Yu Ri, Choi Ye Na, An Yu Jin, Yabuki Nako, Kwon Eun Bi, Kang Hye Won, Honda Hitomi, Kim Chae Won, Kim Min Ju and Lee Chae Yeon.",
        "image_etc":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/member2.jpg"
    },
    {
        "title":"Songs",
        "subtitle":"เพลงและอัลบั้ม",
        "image_url":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/song1.jpg",
        "detail":"Produce 48 Formation and Debut with COLOR*IZ (2018)\n\nThe group debuted in Korea on October 29, 2018 with their debut mini album,'COLOR*IZ' featuring the title track 'La Vie en Rose' (라비앙로즈). The physical album was released in two versions, a color version and a rose version. The album peaked at #2 on Gaon Album Chart and sold 225,000 units.\nThe early success subsequently hailed them as the New Artist of the Year at several awards shows, including Golden Disc Awards and Seoul Music Awards.\n\n\nJapanese Debut and Comeback with HEART*IZ (2019)\n\nThe group made their Japanese debut on February 6, 2019 with 'Suki to Iwasetai' Peaking at number 2 on Oricon Singles Chart and with over 250,000 unit sales, the single was certified Platinum by the Recording Industry Association of Japan (RIAJ)\n\nThe group's second Korean mini album, 'HEART*IZ', was released on April 1st, 2019 and featured the title track 'Violeta' The physical album was released in two versions, a Violeta version and a Sapphire version, as well as a random clear sleeve (1 of 13 for each version).\nIZ*ONE later made their first Japanese comeback with the single Buenos Aires, shortly followed by their third single Vampire.\n\n\nProduce 48's vote manipulation, BLOOM*IZ, Oneiric Diary, Twelve and One-Reeler / Act IV (2020)\n\nIZ*ONE's return was scheduled for November 11, 2019, but was postponed after Produce 48 director An Joon Young admitted to manipulating the program's ratings. The group has since been on an indefinite hiatus.\n\nOn 23 January 2020, in a statement, Mnet responded 'respecting the views of members and fans who hope that IZ*ONE's activities will return to normal, Mnet and the agencies of IZ*ONE members have decided that their activities will resume. IZ*ONE is expected to resume activities in February, and details, including the exact schedule, will be announced soon'.\nIn early 2020 Off the Record announced that IZ*ONE would continue as a twelve member group with the release of BLOOM*IZ in February 2020 and its title track, FIESTA.\n\nOn May 19, IZ*ONE shared through a post in the group's Official Fancafe that they had finished recording the MV two days earlier and that their next comeback would be on June 15th with their third mini album, Oneiric Diary and its title track, Secret Story of the Swan. The album trailer was released on May 31, 2020 through Stone Music's official Youtube channel. The MV was postponed to June 16 but the performace video and album was released on June 15, the original release date.\n\nOn August 16, Stone Music announced IZ*ONE's first online solo concert, 'Oneiric Theater', to be held on September 13th.\n\nOn October 21, the group released their first Japanese studio album, Twelve, with its title track, Beware. Beware's MV was released on October 7, 2020.\n\nOn November 17, it was confirmed that the group would be releasing a Korean comeback on December. The comeback, One-Reeler / Act IV, was released with its title track, Panorama, on December 7, 2020.",
        "image_etc":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/song2.jpg"
    },
    {
        "title":"Events",
        "subtitle":"งานและรายการต่างๆ",
        "image_url":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/event1-2.jpg",
        "detail":"IG และ Twitter", 
        "image_etc":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/events2.jpg"
    },
    {
        "title":"Follow",
        "subtitle":"ติดตามความเคลื่อนไหว",
        "image_url":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/follow1.jpg",
        "detail":"IG และ Twitter", 
        "image_etc":"https://raw.githubusercontent.com/ticktahod/BasicAPI/main/follow2.jpg"
    }
    
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})
