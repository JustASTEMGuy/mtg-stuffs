import urllib.request
from PIL import Image
import scrython as scr

class getCard:

    #Card properties
    def __init__(self):
        self.rCard = None
        self.myimageCard = None
        self.myimageName = None
        self.rinp = 0
        self.myCardList = []
        self.tempCard = scr.cards
        self.cimage = None
        self.search = None

    #Print and Check for Cards
    def check(self, query):
        self.search = self.tempCard.Search(q=query, order="name")
        tempList = self.search.data()
        for i in range(len(tempList)):   #tempList --> list []
            cardnames = tempList[i]    #cardnames --> dictionaries {}
            r = i + 1
            print(str(r) + ".", cardnames["name"], cardnames["type_line"])

        imchoice = str(input("Get Image? (Y/N)\n"))   #Choice for Getting Image --> Choose index
        if imchoice == "Y" or imchoice == "y":
            self.rinp = int(input("Type in the index that you want the image: "))
            self.rinp = self.rinp - 1
            if self.rinp in range(len(tempList)):
                self.myimageCard = tempList[self.rinp]
                self.myimageName = self.myimageCard["name"]
                fCard.getImage()
            else:
                print("Index does not exists...")
                pass
        else:
            pass

    def getImage(self):
        self.cimage = self.tempCard.Named(exact=self.myimageName)
        imagesize = str(input("Image size (small, medium, large): "))
        imageurl = str(self.cimage.image_uris(image_type=imagesize))
        urllib.request.urlretrieve(imageurl, "card.png")
        imageshow = Image.open("card.png")
        imageshow.show()

    def getRandomCard(self):
        self.rCard = scr.cards.Random()
        print(self.rCard.name())
        imageurl = str(self.rCard.image_uris(image_type="large"))
        urllib.request.urlretrieve(imageurl, "card.png")
        choice = str(input("Need the image? (Y/N): "))
        if choice == "Y" or choice == "y":
            imageshow = Image.open("card.png")
            imageshow.show()
        else:
            print("Suit yourself.")
            pass

fCard = getCard()
while True:
    inp = str(input("Please enter your card name ('Stop' to stop, 'Random' to get a random card.): "))
    if inp != "Stop" and inp != "Random":
        fCard.check(inp)

    elif inp == "Random":
        fCard.getRandomCard()

    else:
        print("Bye!")
        break

#It's not perfect but it works
