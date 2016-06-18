#_*_ coding: utf-8 _*_

users = [
	{"id":0, "name":"Hero"},
	{"id":1, "name":"Dunn"},
	{"id":2 , "name":"Sue"},
	{"id":3,  "name":"Chi"},
	{"id":4 , "name":"Thor"},
	{"id":5 , "name":"Clive"},
	{"id":6 , "name":"Hicks"},
	{"id":7 , "name":"Devin"},
	{"id":8 , "name":"Kate"},
	{"id":9 , "name":"Klein"}
]

friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),
(7,8),(8,9)]

for user in users:
	user["friends"] = []

for i,j in friendships:
	users[i]["friends"].append(users[j])
	users[j]["friends"].append(users[i])

#친구의 친구들을 리턴한다.
def friends_of_friend_ids_bad(user):
	return [foaf["id"] for friend in user["friends"] 
	                                for foaf in friend["friends"]]

print "user[0]에게 추천해 줄 사람들의 id(본인의 id도 포함되어있음) : ",friends_of_friend_ids_bad(users[0])

print [friend["id"] for friend in users[0]["friends"]] #0번 사용자의 친구들을 리턴한다.
print [friend["id"] for friend in users[1]["friends"]] #1번 사용자의 친구들을 리턴한다.
print [friend["id"] for friend in users[2]["friends"]] #2번 사용자의 친구들을 리턴한다.



