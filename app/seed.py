import random
from . import models

"""seed helper"""
category = ['oil painting', 'pencil sketch', 'abstract painting',
            'Watercolor Painting', 'Pastel Painting', 'Acrylic Painting']
names = [
    "Night At Venice",
    "Painting The Dreams",
    "Horses",
    "Tree of Life",
    "The one",
    "Libana",
    "Joy",
    "Kites in City",
    "dancing girl",
    "retro shades",
]
Fauthor = [
    "sailesh",
    "joan",
    "Bodhi",
    "Sybil",
    "Lilith",
    "naga",
    "arshath",
    "Alexander",
    "Hugh",
    "Elon",
    "steve",
]
Sauthor = [
    "smartz",
    "oriel",
    "dharma",
    "rune",
    "juno",
    "lakshmi",
    "Parvesh",
    "Hugo",
    "Jackmnan",
    "Musk",
    "Jobs",
]
products = {
    "name": lambda : names[random.randint(0, len(names)-1)],
    "author": lambda: f"{random.randint(0, len(Fauthor)-1)} {random.randint(0, len(Sauthor)-1)}",
    "description": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore
        distinctio aliquam corporis ratione consectetur quis quidem unde
        mollitia, culpa architecto eveniet voluptate deserunt saepe, atque eum
        laboriosam veritatis iure illum.""",
    "likes":6,
    "price":lambda: random.randint(500, 20000),
    "avg_ratings":lambda: random.randint(1, 5),
    "rating_count": lambda: random.randint(1, 10000),
}


def seeder():
    if(models.Categories.objects.all()):
        models.Categories.objects.all().delete()
    for elem in category:

        c = models.Categories(title=elem)
        c.save()
        for i in range(random.randint(1, 5)):
            p = models.Products(
                category=c,
                title=products["name"](),
                author=products["author"](),
                description=products["description"],
                image_URl="https://source.unsplash.com/collection/8797172",
                price=products["price"](),
                likes=products["price"](),
                avg_ratings = products["avg_ratings"](),
                rating_count = products["rating_count"]()
            )
            p.save()
        
