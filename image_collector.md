# Card Searching + Image (Algorithm)
A small card searcher that uses Scryfall API. It's not perfect but it's just a fun little project I made. 
Current issue is that I'm unable to code a page navigator.

## Modules

> [!NOTE]
> Do make sure you've installed the following modules.
- urllib
- Pillow
- Scrython
  
```
import urllib.request
from PIL import Image
import scrython as scr

```

## Card's Class
It's stingy to be honest, as the structure itself seems weird to me, especially the getImage() part where it doesn't work with the randomize function.
```
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
```

## Main Loop
>[!WARNING]
> Do note that if your query isn't in any card's name, it'll just pop out an error. <sub>(Still working on that but I ultimately couldn't figure it out)</sub>
```
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

```
Overall, it's a fun project that I thought about a while back ago. 

This is probably my first project that I create without any tutorials and full on referring only documentations. 

I do plan to integrate it with a GUI like TKInter but I'll probably just going for other new projects. If you see this, you can give it a try, it's not much, and to other beginner devs out there, wish y'all continue to tinker with new projects and so on.

Happy trails.

## Documentation / Sources
1. **[Scryfall API](https://scryfall.com/docs/api)**

    - API Documentation for getting infos of MTG's Cards.
  
2. **[Scrython](https://github.com/NandaScott/Scrython)** 

    - A wrapper for Scryfall's API. (Appreciated this a lot ngl)

3. **[Pillow Module](https://pillow.readthedocs.io/en/stable/)**

   - Used for getting Image datas.
  
4. **[urllib](https://github.com/python/cpython/tree/3.12/Lib/urllib/)**

   - Used to request and process Scryfall's URL into an image.
