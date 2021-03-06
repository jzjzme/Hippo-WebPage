from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



# Flask app
app = Flask(__name__)



# Load config
app.config.from_object('server.serversettings')



# Plugins and extensions
db = SQLAlchemy(app)



# App contents
from server.models import *
from server.api import *
from server.servefront import *



from server.models.food import *



# Create db
db.create_all()



# Dummy data
mission = Neighborhood(name='Mission')
marina = Neighborhood(name='Marina')
l_haight = Neighborhood(name='Lower Haight')
r_hill = Neighborhood(name='Russian Hill')

lim_rot = Restaurant(name='Limon Rotisserie', neighborhood=mission)
blue_barn = Restaurant(name='Blue Barn', neighborhood=marina)
herbivore = Restaurant(name='Herbivore', neighborhood=l_haight)
ele_sushi = Restaurant(name='Elephant Sushi', neighborhood=r_hill)
roam_burger = Restaurant(name='Roam Burger', neighborhood=r_hill)

vegetarian = FoodTag(name='Vegetarian')
vegan = FoodTag(name='Vegan')
glutenfree = FoodTag(name='Gluten-free')
nutfree = FoodTag(name='Nut-free')
dairyfree = FoodTag(name='Dairy-free')
paleo = FoodTag(name='Paleo')

halal = FoodTag(name='Halal')
kosher = FoodTag(name='Kosher')

ceviche = FoodEntry(name='Cevicheria', 
    restaurant=lim_rot, active=True, price=12.00,
    imageurl_icon='http://www.hunterspointcommunity.com/wp-content/uploads/2012/12/limonsf-e1355421301704.jpg', 
    imageurl_full='https://images0.mnch.io/menu-items/6444/2014-10-28-31558-edit-1.jpg?dpr=2.0&q=70&sharp=0&vib=10&gam=-10&w=770&h=510&fit=crop&s=01e8616a3254574391b5fac4a7cc2c26',
    details="""Fresh seafood cured in citrus boasts a lively and bright combination that can't be missed. Limon executes this Peruvian signature dish better than anyone in the city.""",
    nutrition = """
    Total Fat: 
    12g, 
    Sat. Fat:
    2g,
    Trans. Fat:
    0g, 
    Chloesterol:
    0mg, 
    Sodium:
    300mg,
    Total Carbs:
    5g,
    Dietary:
    0g,
    Sugar: 
    2g,
    Protein:
    25g
    """,
    ingredients="""Leche de tigre milk, Halibut, Shrimp, Onion, Tomato, Lemon juice, Red pepper, Cilantro, and Lime juice""",

    )
salad = FoodEntry(name='Winter Salad', 
    restaurant=blue_barn, active=True, price=15.00,
    imageurl_icon='http://www.bluebarngourmet.com/static/media/uploads/Pics/.thumbnails/IMG_4598-657x345.JPG', 
    imageurl_full='https://images0.mnch.io/menu-items/6661/2014-12-05-33288-edit-1.jpg?dpr=2.0&q=70&sharp=0&vib=10&gam=-10&w=770&h=510&fit=crop&s=0856e77340bae29e9a1383dc5701e7b7',
    details="""This light side salad is perfect for rounding out an entree. The baby lettuces are tossed with tarragon, dill, basil, parsley and chives. The salad is topped with shaved pickled red onion, multi grain croutons and red wine - whole grain mustard vinaigrette.""",    
    nutrition = """
    Total Fat: 
    7g, 
    Sat. Fat:
    1g, 
    Trans. Fat:
    0g, 
    Chloesterol:
    0mg, 
    Sodium:
    400mg, 
    Total Carbs:
    0g, 
    Dietary:
    0g, 
    Suga14g,r: 
    3g, 
    Protein:
    4g, 
    """,
    ingredients="""Mixed Greens, Whole Grain Bread, Onions, Red wine vinegar, Olive Oil, Whole grain mustard , Black pepper, Kosher Salt, Basil, Chives, Dill, Parsley, Tarragon""",
    
    )
chicken = FoodEntry(name='Rotisserie Chicken', 
    restaurant=herbivore, active=True, price=13.00,
    imageurl_icon='http://www.herbivorerestaurant.com/images/logo4menu.jpg', 
    imageurl_full='https://images4.mnch.io/menu-items/2763/2013-11-1-2930-edit.jpg?dpr=2.0&q=70&sharp=0&vib=10&gam=-10&w=770&h=510&fit=crop&s=a16d25998599f7004b264fb7c6d94b74',
    details="""Free Range chicken braised with Filipino cane vinegar, soy sauce, coconut milk, bay, peppercorns and garlic. Served with bok choy, and bell peppers. A side of steamed coconut turmeric rice accompanies the adobo.""",    
    nutrition = """
    Total Fat: 
    14g, 
    Sat. Fat:
    4g, 
    Trans. Fat:
    0g, 
    Chloesterol:
    125mg, 
    Sodium:
    600mg, 
    Total Carbs:
    10g, 
    Dietary:
    2g, 
    Sugar: 
    2g, 
    Protein:
    34g
    """,  
    ingredients="""Chicken leg and thigh, Bok Choy, Coconut cream, White rice, Carrots, Sweet green peppers, Sweet red peppers, Thyme, Bay leaf, Black pepper, Garlic, Kosher Salt, Sugar, Soy sauce, Rice wine vinegar""",
    
    )
tuna_roll = FoodEntry(name='Spicy Tuna & Tobiko Roll', 
    restaurant=ele_sushi, active=True, price=14.00,
    imageurl_icon='http://2458polkstreet.com/wp-content/uploads/2013/12/Russian-Hill-Elephant-Sushi1.jpg', 
    imageurl_full='https://images0.mnch.io/menu-items/3996/2014-05-09-16403-edit.jpg?dpr=2.0&q=70&sharp=0&vib=10&gam=-10&w=770&h=510&fit=crop&s=94fdad4e34a25223fbf366f2d773416a',
    details="""A simple but tasty traditional roll. Chopped hamachi (yellow tail) and green onions. Served with soy sauce, wasabi and pickled ginger.""",    
    nutrition = """
    Total Fat: 
    10g,     
    Sat. Fat:
    3g, 
    Trans. Fat:
    0g, 
    Chloesterol:
    0mg, 
    Sodium:
    200mg, 
    Total Carbs:
    20g,
    Dietary:
    1g, 
    Sugar: 
    2g, 
    Protein:
    10g
    """,    
    ingredients="""White rice, Yellowtail, Soy sauce, Rice wine vinegar, Nori, Young green onions, Ginger root, Pure Cane Sugar, Wasabi, Sea Salt, Sesame Seeds""",
    
    )
burger = FoodEntry(name='Pacific Blue Veggie Burger', 
    restaurant=roam_burger, active=True, price=11.00,
    imageurl_icon='http://roamburgers.com/wp-content/themes/roam/i/global/logo-print.png', 
    imageurl_full='http://imgs.sfgate.com/blogs/images/sfgate/hamblogger/2010/08/27/roam1624x406.jpg',
    details="""House-Made Organic made.""",    
    nutrition = """
    Total Fat: 
    17g, 
    Sat. Fat:
    5g, 
    Trans. Fat:
    0g, 
    Chloesterol:
    0g, 
    Sodium:
    300mg, 
    Total Carbs:
    45g, 
    Dietary:
    4g, 
    Sugar: 
    3g, 
    Protein:
    28g
    """, 
    ingredients="""Blue Cheese, Watercress, Tomato, Caramelized Onions, Steak Sauce""",
    
    )

ceviche.tags = [vegetarian, glutenfree, nutfree, paleo]
salad.tags = [vegetarian, glutenfree, nutfree, vegan, dairyfree, paleo]
chicken.tags = [glutenfree, nutfree, dairyfree, paleo]
tuna_roll.tags = [vegetarian, glutenfree, nutfree, dairyfree]
burger.tags = [vegetarian, glutenfree, nutfree, vegan]



for item in [mission, marina, l_haight, r_hill, lim_rot, blue_barn, herbivore, ele_sushi, roam_burger, ceviche, salad, chicken, tuna_roll, burger]:
    db.session.add(item)


db.session.commit()