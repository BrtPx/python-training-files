""" for loops"""
companions = ["rose", "donna", "martha", "pond", "river"]

for companion in companions[1:3]:
    print(companion)

for companion in companions:
    if companion == "river":
        print(f"{companion} is the Doctor's wife")
        break
    print(companion)
