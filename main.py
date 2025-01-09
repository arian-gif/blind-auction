import art

print(art.logo)
print("WELCOME TO BIDDING CLUB")
bidding ={}
keep_bidding = "yes"
while keep_bidding == "yes":
    name = input("What is your name:\n")
    bid = int(input("What is your bid:\n"))
    bidding[name]= bid
    keep_bidding = input("Are there any other bidders, Type yes or no:\n")
    print("\n" * 20)

max =0
max_name =""
for key in bidding:
    if bidding[key]>max:
        max_name = key
        max = bidding[key]

if max>0:
    print(max_name +" won the auction")