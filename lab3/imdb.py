# Dictionary of movies

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

def high_score(movies):
    if movies["imdb"] > 5.5:
        print("True")
    else:
        print("False")

#high_score(movies[2])

def mov(movies):
    result=[]
    for movie in movies:
        if movie["imdb"] > 5.5:
            result.append(movie)
    return result

#print(mov(movies))

def category(movies,category):
    result=[]
    for movie in movies:
        if movie["category"]==category:
            result.append(movie["name"])
    return result
    
#print(category(movies,"Romance"))

def avg(movies):
    total=0
    for movie in movies:
        total+=movie["imdb"]
    return total/len(movies)
#print(avg(movies))

def avg_category(movies,category):
    total=0
    count=0
    for movie in movies:
        if movie["category"]==category:
            total+=movie["imdb"]
            count+=1
        if count==0:
            return 0
        return total/count

#print(avg_category(movies,"Thriller"))


