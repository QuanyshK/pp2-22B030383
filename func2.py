
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
import random
def good(movies):
    i = random.randint(0, len(movies)-1)
    print(movies[i]["name"])
    if movies[i]["imdb"]>5.5:
        return True
    else:
        return False
print(good(movies))
#
def imdb(movies):
    if movies["imdb"] > 5.5:
        return True
    return False
for i in range(0, len(movies)):
    if(imdb(movies[i])):
        print(movies[i]["name"])
#

def category(movies):
    category1 = []
    cnt = 0
    for i in range(0, len(movies)):
        if movies[i]["category"] not in category1:
            category1.append(movies[i]["category"])
            cnt += 1
    category1.sort()
    for j in range(0, cnt):
        for k in range(0, len(movies)):
            if movies[k]["category"] == category1[j]:
                print(movies[k])
category(movies)
#
def average(movies):
    summ = cnt = 0
    for i in range(0, len(movies)):
        summ += float(movies[i]["imdb"])
        cnt += 1
    print(summ / cnt)
average(movies)
#
def categorya(movies):
    category1 = []
    cnt = summ = 0
    for i in range(0, len(movies)):
        if movies[i]["category"] not in category1:
            category1.append(movies[i]["category"])
            cnt += 1
    count = 0
    for j in range(0, cnt):
        for k in range(0, len(movies)):
            if movies[k]["category"] == category1[j]:
                summ += float(movies[k]["imdb"])
                count += 1
    print(summ / count)
categorya(movies)