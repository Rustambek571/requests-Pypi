# ex1

# import requests
#
# link = 'https://reqres.in/api/users/'
# k = requests.get(link)
#
# m = k.json()
# for k in m:
#     for key in k:
#         print(key)
#     print('\n')

#ex2

# import requests
#
# havola = 'http://api.weatherapi.com/v1'
# r = requests.get(havola + '/current.json', params={'key':'f32b2cd7fe364abd8d8182803230603', 'q': 'Tashkent'})
#
# m = r.json()
# for i in m:
#     for d in i:
#         print(d)
#     print('\n')