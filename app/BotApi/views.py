import shutil
import os
from bs4 import BeautifulSoup

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UsersBot
from .serializers import UserSerializer

class GetUsersApi(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        search = self.kwargs['search']
        type_search = self.kwargs['type']
        queryset = Response({'message': 'NOT FOUND'})

        if type_search == 'name':
            queryset = UsersBot.objects.filter(name=search)
        elif type_search == 'surname':
            queryset = UsersBot.objects.filter(surname=search)
        elif type_search == 'age':
            queryset = UsersBot.objects.filter(age=search)
        elif type_search == 'city':
            queryset = UsersBot.objects.filter(city=search)
        elif type_search == 'id_vk':
            queryset = UsersBot.objects.filter(id_vk=search)
        elif type_search == 'instagram_id':
            queryset = UsersBot.objects.filter(instagram_id=search)
        return queryset

@api_view()
def StartGetParse(request):
    print('Start Get Parse HTML Files...')
    try:
        base_dir_html_render = 'renderHTML'
        move_dir_html_renderer = 'rendererHTML'
        list_html = os.listdir(base_dir_html_render)
        # print(os.listdir(base_dir_html_render))
        for i in list_html:
            with open(base_dir_html_render+'/'+i, "r", encoding='utf-8') as f:
                index = f.read()
                
                # Парсим HTML File
                Parse = BeautifulSoup(index, "html.parser")
                result = Parse.findAll("li")

                # Получаем все содержание нужной информации
                a = [link.text for link in result]
                # print(a)

                result = [] # Массив со всеми данными пользователя
                number_file = '' # Номер файла
                for j in range(len(i)): # Тут мы перебираем название файла, чтобы получить его ID
                    try:
                        b = int(i[j])
                        number_file += i[j]
                    except:
                        break
                result.append(number_file)

                for j in range(len(a)):
                    split_parse = a[j].split()
                    result.append(split_parse[1])
                    if j == 0: # Чтобы Фамилию и Имя добавить в массив RESULT
                        result.append(split_parse[0])
                

                # В массиве идет так:
                # [0] - ID Файла
                # [1] - Имя
                # [2] - Фамилия
                # [3] - Возраст
                # [4] - Город
                # [5] - ID VK
                # [6] - ID Instagram
                # print(result)
                
                # Сохраняем в БД
                save = UsersBot(id_files=result[0],
                                      name=result[1],
                                      surname=result[2],
                                      age=result[3],
                                      city=result[4],
                                      id_vk=result[5],
                                      instagram_id=result[6])
                save.save()

            shutil.move(base_dir_html_render+'/'+i, move_dir_html_renderer+'/'+result[0]+'.html')

        print('Stop Get Parse HTML Files - SUCCESS')
        return Response({"message": "OK"})
    except:
        print('Stop Get Parse HTML Files - ERROR')
        return Response({"message": "FAIL"})