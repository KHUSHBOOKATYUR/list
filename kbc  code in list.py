print("******* WELCOME TO KBC GAME *********")
question_list = [
"How many continents are there?", 
"What is the capital of India?", 
"NG mei kaun se course padhaya jaata hai?",
"Who founded microsoft?"
]
options_list = [

    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["Elon musk","Jeff","Mark","Bill gates"]
]
solution_list = [3, 4, 1,2]
answer_list=[
    ["1.Four","3.seven"],
    ["2.bhopal","4.Delhi"],
    ["1.softwere Engineering","3.Agriculture"],
    ["2.Jeff","4.Bill gates"]]
print("******KAUN BANEGA CROREPATI  (KBC)*******")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a+=1
    num=input("Do You Wamt 5050 LifeLine:- ")
    if num=="yes":
        print("accept")
        if count<1:
            print(answer_list[b])
            num1=int(input("enter the answer:- "))
            if num1==solution_list[i]:
                s+=1
                print("Your answer is correct")
                print("YOU WIN Rs/",s)
            else:
                print("incorrect answer")
                print("YOU WIN Rs/",s)
                break
            count+=2000
        else:
            print("you already use lifeline")
            num2=int(input("enter the your answer:- "))
            if num2==solution_list[i]:
                print("Congrats your answer is right")
                s+=10
                print("YOU WIN Rs/",s)
            else:
                print("your answer is wrong")
                print("YOU WIN Rs/",s)
                break
    else:
        pass
        k=int(input("enter your answer-"))
        if k==solution_list[i]:

            cx
            print("right answer")
            s+=1000
            print("you win Rs/",s)
        else:
            print("no chance")
            print("your answer is wrong")
            print("you win rs/",s)
    i+=1
print("congratulations.....your participated in KBC game")
print("you win Rs/",s)
print("Thanks for particapting..........")
