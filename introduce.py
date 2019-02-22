top_choice = ""
bottom_choice = ""
#// Characters
class Charactors:
    def __init__(self, name, intro, face, relationship):
        self.name = name
        self.intro = intro
        self.face = face
        self.relationship = relationship
your_name = input("What's your name?")
friend_name = input("What is your best friends name?")

Randy = Charactors("Randy Fenoli",
f"Hello! Welcome to Kleinfield, my names Randy Fenoli but you can call me Randy. I own Kleinfield and help fiances like yourself find the dress of their dreams!I'm known as the gown whisperer. ",
f"""
     /\/\/\/
    ( *  * )
     \ ~~ / """
, "Owner of Bridal Salon"  )

Cindy = Charactors("Cindy",
f" Hi there, how are you? My name is Cindy! I'll be your bridal consultant today to help you pick your dress. ",
f"""
    _________
   ||||||||||
   || *  * ||
   (|  <   |) """, "Bridal Consultant")
mom = Charactors("Mom",
f"Awe shes my only daughter and we all know she's daddy's little girl. We need to make sure this dress is perfect so everyone especially her dad and fiance will start crying when they see her.",
f"""
     ///////
    () * * ()
    ()  =  ()""","Mother")



friend = Charactors("friend",
f"My name is {friend_name} and I am {your_name}'s best friend, she can't do anything without me! Especially pick a wedding dress! She will not buy one unless I love it and I will make sure of it!",
f"""
      )))))))))
     ((  @ @ ((
     ))  >   ))  """, "Best Friend")



you = Charactors("Bride",
f"My name is {your_name} and this dress has to be perfect, I want to look at the dress and just know its perfect for me. I also want {friend_name} and my Mom to love it too. This is just as much their wedding as mine.",
f"""
          /\/\/\/
         |0 0 0 0|
         ---------
        (  @  @   )
            =       """, "Bride")

class DressTops:
    def __init__(self, descript, top):
        self.descript = descript
        self.top = top
Strappy = DressTops("An elegant, simple top with thin straps and a belt around the waist",
f"""
          ||      ||
          | \    / |
          |  \  /  |
          |   \/   |
          |        |
          |--------|
          |____@___|  """)

Sleeves = DressTops("A beautiful, modest, long sleeve top adorned with lace flowers.",
f"""
        ______________
       ( *  *        *)
       |* |      * | *|
       |  |  *     | *|
       | *| *      |  |
       |* |    *   |* |
       |  |        |  |
       |* |*  *    | *| """)

Sleeveless = DressTops("A gorgeous sleeveless top with a sweetheart neckline and a large lace belt at the waist.",
 f"""
          (```~~```)
          |        |
          |        |
          |        |
          |^^^^^^^^|
          |________|""")

class DressBottoms:
    def __init__(self, descripti, bottom):
        self.descripti = descripti
        self.bottom = bottom

Ballgown = DressBottoms(" A large fluffy full length skirt with a long flowing train.",
f"""
           ________
          /        \/
         /          \/
        /            \/
       /              \/
      /                \/
     /                  \/
    /                    \/
   /                      \/
  /________________________\/ """)

Short = DressBottoms("A short and bouncy playful skirt, adorned with fun flowers.",
f"""
           ~~~~~~~~
          / *    * \/
         /     *    \/
        /         *  \/
       /  *  *   *    \/
       ~~~~~~~~~~~~~~~~ """)

Pants = DressBottoms("A striking pair of pants.",
f"""
           ________
          /        \/
         /          \/
         |     |    |
         |     |    |
         |     |    |
         |     |    |
         |   /  \   |
         \__/    \__/ """)

print("Randy:")
print(Randy.intro)
print(Randy.face)
input()
print("Randy: Let my introduce you to your consultant")
print(Cindy.intro)
print(Cindy.face)
input()
print("Cindy:So who do you have with you?")
input()
print(you.intro)
print(you.face)
input()
print(mom.intro)
print(mom.face)
input()
print(friend.intro)
print(friend.face)
input()
print("Cindy: Do you have any idea of what type of top you want?")
choice = input("Strappy, Sleeves, or Sleeveless")
if choice == "Strappy":
    print(Strappy.descript)
    top_choice = Strappy
elif choice == "Sleeveless":
    print(Sleeveless.descript)
    top_choice = Sleeveless
elif choice == "Sleeves":
    print(Sleeves.descript)
    top_choice = Sleeves
input()
print("Cindy:What about bottoms?")
choicee = input("Ballgown, Short, or Pants")
if choicee == "Ballgown":
    print(Ballgown.descripti)
    bottom_choice = Ballgown
elif choicee == "Short":
    print(Short.descripti)
    bottom_choice = Short
elif choicee == "Pants":
    print(Pants.descripti)
    bottom_choice = Pants
input()
print(top_choice.top)
print(bottom_choice.bottom)
