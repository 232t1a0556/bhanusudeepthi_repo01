score=0
q=[
  ["Capital of India?","Delhi","Mumbai","Chennai","Kolakata","1"],
  ["Red Planet?","Earth","Mars","Jupiter","Saturn","2"],
  ["Language for web?","C","Java","C++","Python","2"]
]
for i in q:
    print(f"\n{i[0]}\n 1.{i[1]} 2.{i[2]} 3.{i[3]} 4.{i[4]}")
    ans=input("Choice :")
    if ans==i[5]:
        print("Correct..!")
        score+=1
    else:
        print("Wrong")
print(f"\nScore:{score}/{len(q)}")