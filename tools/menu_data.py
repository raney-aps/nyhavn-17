# -*- coding: utf-8 -*-
"""Nyhavn 17 menu data — source of truth: 'NYHAVN 17 NYT KORT (7).pdf' (client, Sept 2026).

Every item carries both languages so the DA and EN sites can never drift apart.
price=None  -> no price column (prices are inline in the description)
"""

def I(da, en, desc_da="", desc_en="", price=None):
    return {"da": da, "en": en, "desc_da": desc_da, "desc_en": desc_en, "price": price}


def S(label_da, label_en, items, note_da="", note_en=""):
    return {"label_da": label_da, "label_en": label_en,
            "note_da": note_da, "note_en": note_en, "items": items}


# ---------------------------------------------------------------- BREAKFAST
BREAKFAST_FEATURED = [
    I("Grillet croissant", "Grilled croissant",
      "Med kogt skinke, smeltet ost og sennep",
      "With boiled ham, melted cheese and mustard", "55"),
    I("Burger", "Burger",
      "Med ost, bacon og pommes frites",
      "With cheese, bacon and fries", "169"),
    I("Morgenmadstallerken", "Breakfast platter",
      "Skinke, ost, røget laks, brød, syltetøj og smør &nbsp;·&nbsp; tilføj røræg +35",
      "Ham, cheese, smoked salmon, bread, jam and butter &nbsp;·&nbsp; add scrambled eggs +35", "89"),
]

BREAKFAST_LEFT = [
    S("Bagværk", "Pastry", [
        I("Croissant", "Croissant", "Med smør og syltetøj", "With butter and jam", "55"),
        I("Pain au chocolat", "Pain au chocolat", "Med nougatfyld", "With nougat filling", "60"),
        I("Wienerbrød", "Danish pastry", "Med cremefyld og syltetøj", "With cream filling and jam", "40"),
        I("Brød og smør", "Bread and butter", "Lune brødboller og saltet smør", "Warm bread rolls and salted butter", "45"),
    ]),
    S("Æggeretter", "The eggs", [
        I("Røræg", "Scrambled eggs", "Med purløg", "With chives", "40"),
        I("Omelet", "Omelette", "Stegt i smør", "Cooked in butter", "60"),
        I("Spejlæg", "Sunny side eggs", "Stegt i smør", "Cooked in butter", "45"),
        I("Blødkogt æg", "Soft boiled egg", "Serveret med havsalt", "Served with sea salt", "25"),
    ]),
]

BREAKFAST_RIGHT = [
    S("Toast", "The toast", [
        I("Avocadotoast", "Avocado toast",
          "Ristet rugbrød, avocado i skiver, purløg, havsalt og olivenolie",
          "Toasted rye bread, sliced avocado, chives, sea salt and olive oil", "99"),
        I("Toast med skinke og ost", "Ham and cheese toast",
          "Ristet toastbrød, skinke og smeltet ost",
          "Toasted sandwich bread, ham and melted cheese", "79"),
        I("Toast med røget laks", "Smoked salmon toast",
          "Ristet toastbrød, cremet æggesalat, dild, spinat og røget laks",
          "Toasted sandwich bread, creamy egg salad, dill, spinach and smoked salmon", "95"),
        I("Æg og bacon", "Egg and bacon",
          "Ristet toastbrød, røræg og bacon",
          "Toasted sandwich bread, scrambled eggs and bacon", "85"),
    ]),
    S("Tilbehør", "The add ons", [
        I("Brød", "Bread",
          "Brød og smør 35 &nbsp;·&nbsp; rugbrød og smør 35",
          "Bread and butter 35 &nbsp;·&nbsp; rye bread and butter 35", None),
        I("Pålæg og andet", "Meats and others",
          "Røget laks 35 &nbsp;·&nbsp; bacon 35 &nbsp;·&nbsp; ost 25 &nbsp;·&nbsp; pølser 40 &nbsp;·&nbsp; avocado 40",
          "Smoked salmon 35 &nbsp;·&nbsp; bacon 35 &nbsp;·&nbsp; cheese 25 &nbsp;·&nbsp; sausages 40 &nbsp;·&nbsp; avocado 40", None),
        I("Morgenmadsskål", "Breakfast bowl",
          "Frisk frugt, yoghurt, granola og honning",
          "Fresh fruit, yoghurt, granola and honey", "95"),
        I("Pandekager", "Pancakes",
          "Luftige pandekager med smør og ahornsirup",
          "Fluffy pancakes with butter and maple syrup", "65"),
    ]),
]

# ------------------------------------------------- SHARED: LUNCH AND DINNER
MAINS_FEATURED = [
    I("Club sandwich", "Club sandwich",
      "Med kylling, bacon, karrydressing, salat og pommes frites",
      "With chicken, bacon, curry dressing, salad and fries", "159"),
    I("Burger", "Burger",
      "Med ost, bacon og pommes frites",
      "With cheese, bacon and fries", "159"),
    I("Nachos", "Nachos",
      "Cheddar, salsa, guacamole og creme fraiche",
      "Cheddar, salsa, guacamole and creme fraiche", "139"),
    I("Fish &amp; chips", "Fish n chips",
      "Med frisk kuller, sauce tartare eller remoulade, sprøde pommes frites og citron",
      "With fresh haddock, sauce tartare or remoulade, golden fries and lemon", "169"),
    I("Dagens suppe", "Soup of the day", "", "", "89"),
]

STJERNESKUD = I(
    "Stjerneskud", "Shootingstar / Stjerneskud",
    "Stegte og dampede rødspættefileter med rejer, asparges og dressing",
    "Fried and steamed fillets of plaice with shrimps, asparagus and dressing", "179")

SMORREBROD_LEFT = S("Smørrebrød", "Open faced sandwich / Smørrebrød", [
    I("Æg og rejer", "Egg and peeled shrimp",
      "Med mayonnaise, sort peber, dild og citron",
      "With mayonnaise, black pepper, dill and lemon", "125"),
    I("Pillede rejer", "Peeled shrimps",
      "Med mayonnaise, sort peber, citron og dild",
      "With mayonnaise, black pepper, lemon and dill", "135"),
    I("Rødspættefilet 1.", "Fillet of plaice 1.",
      "Med remoulade, citron og dild",
      "With remoulade, lemon and dill", "125"),
    I("Rødspættefilet 2.", "Fillet of plaice 2.",
      "Med mayonnaise, rejer, citron og dild",
      "With mayonnaise, shrimps, lemon and dill", "135"),
    I("Rødspættefilet 3.", "Fillet of plaice 3.",
      "Med mayonnaise, rejer, lakserogn, citron og dild",
      "With mayonnaise, shrimps, salmon roe, lemon and dill", "145"),
    I("Røget laks", "Smoked salmon",
      "Med peberrod og røgeostecreme",
      "With horseradish and smoked cheese cream", "145"),
    I("Røget laks og æg", "Smoked salmon and eggs",
      "Med cremet æggesalat, tomat, citron og dild",
      "With creamy egg salad, tomato, lemon and dill", "155"),
    I("Snapsemad", "Snapsemad",
      "Med marineret sild, kogte kartofler, dildcreme og citron",
      "With marinated herring, boiled potatoes, dill cream and lemon", "155"),
    I("Sprødstegt flæsk", "Crispy pork",
      "Med rødkål og agurkesalat",
      "With red cabbage and cucumber salad", "145"),
    I("Frikadeller", "Danish meat balls",
      "Med rødkål og agurkesalat",
      "With red cabbage and cucumber salad", "145"),
    I("Hønsesalat", "Chicken salad",
      "Med bacon, champignon, asparges og karse",
      "With bacon, mushrooms, asparagus and cress", "145"),
    I("Roastbeef", "Roastbeef",
      "Med asier, agurkesalat, peberrod, karse, kapers og ristede løg",
      "With pickles, cucumber salad, horseradish, cress, capers and crispy onions", "155"),
])

SMORREBROD_RIGHT = S("Smørrebrød", "Open faced sandwich / Smørrebrød", [
    I("Kartoffel <span class=\"text-gold/70\">(vegetarisk)</span>", "Potato <span class=\"text-gold/70\">(vegetarian)</span>",
      "Med røgeostecreme, syltede løg, ristede løg, karse og forårsløg",
      "With smoked cheese cream, pickled onions, crispy onions, cress and spring onion", "125"),
    I("Tomat <span class=\"text-gold/70\">(vegetarisk)</span>", "Tomato <span class=\"text-gold/70\">(vegetarian)</span>",
      "Med hårdkogt æg, marinerede tomater, mayonnaise og purløg",
      "With hard boiled egg, marinated tomatoes, mayonnaise and chives", "125"),
    I("Blåskimmelost", "Blue cheese",
      "Med rå æggeblomme, løg og karse",
      "With raw egg yolk, onions and cress", "125"),
    I("Gammel ost", "Old cheese",
      "Med sky, løg og karse",
      "With chicken stock jelly, onions and cress", "125"),
    I("Friteret camembert", "Deep fried camembert",
      "Med blåbærsyltetøj og ristet brioche",
      "With blueberry jam and toasted brioche", "125"),
])

DESSERTS = S("Desserter", "Desserts", [
    I("Affogato", "Affogato",
      "Vaniljeis med varm espresso",
      "Vanilla ice cream with a hot espresso shot", "89"),
    I("Pandekager", "Pancakes",
      "Med vaniljeis og chokoladesauce",
      "With vanilla ice cream and chocolate sauce", "89"),
    I("Chokoladelavakage", "Chocolate lava cake",
      "Med vaniljeis og bærcoulis",
      "With vanilla ice cream and berry coulis", "89"),
    I("Æbletrifli", "Apple trifle",
      "Med vaniljecreme, syltetøj, danske makroner og cognac",
      "With vanilla cream, jam, Danish macaroons and cognac", "89"),
])

HOT_KITCHEN = S("Det varme køkken", "Hot kitchen", [
    I("Rødspættefilet", "Filet of plaice",
      "Med remoulade, sprøde pommes frites, citron og dild",
      "With remoulade, golden fries, lemon and dill", "168"),
    I("Bagt vildlaks", "Baked wild salmon",
      "Med artiskokker, kartofler, grønne oliven, hollandaisesauce og citron",
      "With artichokes, potatoes, green olives, hollandaise sauce and lemon", "178"),
    I("Herregårdsbøf", "Danish minced steak / Herregårdsbøf",
      "Med 230 g hakkebøf, bearnaisesauce, grønne ærter og kartoffelbåde",
      "With a 230 g minced beef patty, bearnaise sauce, green peas and potato wedges", "178"),
    I("Wienerschnitzel", "Wiener schnitzel",
      "Sprødpaneret kalvekød, serveret med stegte kartofler, ærter, citron, kapers og ansjoser",
      "Crispy breaded veal, served with fried potatoes, peas, lemon, capers and anchovies", "198"),
    I("Steak frites af oksemørbrad", "Steak frites of beef filet",
      "Med valgfri sauce: bearnaise eller grøn peber, sprøde pommes frites og grøn salat",
      "With optional sauce: bearnaise or green peppercorn, golden fries and green salad", "198"),
])

DANISH_CLASSICS = S("Danske klassikere", "Danish classics", [
    I("Biksemad", "Biksemad",
      "En klassisk dansk ret med kartofler i tern, løg og møre stykker kød, stegt gyldent og sprødt. Serveres med spejlæg, rødbeder og klassisk dansk tilbehør.",
      "A traditional Danish comfort-food classic made with diced potatoes, onions and tender pieces of meat, pan-fried until golden and crispy. Served with a fried egg, beetroot and classic Danish condiments.", "159"),
    I("Frikadeller", "Danish meatballs (frikadeller)",
      "Klassiske pandestegte frikadeller af svine- og kalvekød, serveret med kartofler, brun sovs og syltede agurker.",
      "Traditional pan-fried pork and veal meatballs, served with potatoes, rich gravy and pickled cucumber.", "159"),
    I("Stegt flæsk", "Stegt flæsk / crispy pork belly",
      "Sprødstegt flæsk serveret med kogte kartofler og cremet persillesovs. En ægte dansk klassiker.",
      "Traditional Danish crispy pork belly served with boiled potatoes and a creamy parsley sauce. A true Danish classic.", "159"),
])

LUNCH_HERRING = S("Sild", "Herring", [
    I("Marineret sild", "Marinated white herring",
      "Med løg og kapers", "With onions and capers", "99"),
    I("Karrysild", "Curry herring",
      "Med hårdkogt æg, løg og kapers, friskt æble",
      "With hard boiled egg, onions and capers, fresh apple", "125"),
    I("Christiansø Pigesild", "Christiansø Pige Sild",
      "Med rå æggeblomme, løg og kapers",
      "With raw egg yolk, onions and capers", "125"),
    I("3 slags sild", "3 kinds of herring",
      "Med marineret sild, karrysild og Christiansø Pigesild",
      "With marinated herring, curry herring and Christiansø Pigesild", "179"),
])

DINNER_STARTERS = S("Forretter", "Starters", [
    I("Marineret sild", "Marinated white herring",
      "Med løg og kapers", "With onions and capers", "99"),
    I("Klassisk dansk rejecocktail", "Classic Danish shrimp cocktail",
      "Håndpillede rejer, sprød salat, agurk, citron og hjemmelavet cocktaildressing",
      "Hand-peeled shrimps, crisp lettuce, cucumber, lemon and homemade cocktail dressing", "99"),
    I("Røget laks", "Smoked salmon",
      "Med røgeostecreme, dild, citron og rugbrød",
      "With smoked cheese cream, dill, lemon and rye bread", "99"),
    I("Svampetoast", "Mushroom toast",
      "Med ristet surdejsbrød, sæsonens svampe og flødesauce med timian og hvidløg",
      "With toasted sourdough bread, mushrooms in season and cream sauce with thyme and garlic", "99"),
])

# ------------------------------------------------------------------ DRINKS
COCKTAILS = S("Cocktails og kander", "Cocktails and pitchers", [
    I("Aperol Spritz", "Aperol Spritz", "Aperol, prosecco, sodavand, appelsin", "Aperol, prosecco, soda, orange", "109 / 349"),
    I("Espresso Martini", "Espresso Martini", "Vodka, kaffelikør, espresso, sukkersirup", "Vodka, coffee liqueur, espresso, sugar syrup", "109 / 349"),
    I("Moscow Mule", "Moscow Mule", "Vodka, lime, ginger beer", "Vodka, lime, ginger beer", "109 / 349"),
    I("Pornstar Martini", "Pornstar Martini", "Vodka, passionsfrugt, vanilje, lime og et shot prosecco", "Vodka, passion fruit, vanilla, lime and a shot of prosecco", "109 / 349"),
    I("Mojito", "Mojito", "Lys rom, lime, mynte, sukker, danskvand", "White rum, lime, mint, sugar, soda", "109 / 349"),
    I("Bramble", "Bramble", "Gin, citron, sukker, brombær", "Gin, lemon, sugar, blackberry", "109 / 349"),
    I("Dark ’n’ Stormy", "Dark ’n’ Stormy", "Mørk rom, lime, ginger beer", "Dark rum, lime, ginger beer", "109 / 349"),
    I("Margarita", "Margarita", "Tequila, triple sec, frisk lime, sukkersirup", "Tequila, triple sec, fresh lime, sugar syrup", "109 / 349"),
    I("Paloma", "Paloma", "Tequila, grapefrugt, frisk lime, danskvand", "Tequila, grapefruit, fresh lime, soda", "109 / 349"),
    I("Gin Basil Smash", "Gin Basil Smash", "Gin, frisk citron, basilikum, sukkersirup", "Gin, fresh lemon, basil, sugar syrup", "139 / 439"),
    I("Piña Colada", "Piña Colada", "Lys rom, kokos, ananas, frisk lime", "White rum, coconut, pineapple, fresh lime", "139 / 439"),
    I("Long Island Iced Tea", "Long Island Iced Tea", "Vodka, gin, rom, tequila, triple sec, citron, cola", "Vodka, gin, rum, tequila, triple sec, lemon, cola", "139 / 439"),
    I("Bloody Mary", "Bloody Mary", "Tomatjuice, vodka, tabasco, sellerisalt", "Tomato juice, vodka, tabasco, celery salt", "139 / 439"),
    I("Whisky Sour", "Whisky Sour", "Jameson whisky, citron, sukkersirup, æggehvide", "Jameson whisky, lemon, sugar syrup, egg whites", "139 / 439"),
], "Glas / kande", "Glass / pitcher")

DRAUGHT = S("Fadøl og cider", "Draught beer &amp; cider", [
    I("Royal Pilsner", "Royal Pilsner", "4,6 % &nbsp;·&nbsp; sprød, forfriskende og let frugtig", "4.6% &nbsp;·&nbsp; crisp, refreshing and lightly fruity", "54 / 75"),
    I("Royal Classic", "Royal Classic", "4,6 % &nbsp;·&nbsp; fyldig, blød og let ristet", "4.6% &nbsp;·&nbsp; rich, smooth and lightly roasted", "54 / 75"),
    I("Royal I.P.A.", "Royal I.P.A.", "4,6 % &nbsp;·&nbsp; humlet og frisk med citrus- og bærnoter", "4.6% &nbsp;·&nbsp; hoppy and fresh with citrus and berry notes", "56 / 79"),
    I("Mørk Mumme", "Mørk Mumme", "6,5 % &nbsp;·&nbsp; mørk dansk ale med noter af karamel og ristet malt", "6.5% &nbsp;·&nbsp; dark Danish ale with notes of caramel and roasted malt", "56 / 79"),
    I("Murphy’s Irish Stout", "Murphy’s Irish Stout", "4,7 % &nbsp;·&nbsp; sprød og maltet med Saaz-humle og citrus", "4.7% &nbsp;·&nbsp; crisp and malty with Saaz hops and citrus", "56 / 79"),
    I("Royal Blanche", "Royal Blanche", "", "", "56 / 79"),
    I("Heineken Lager", "Heineken Lager", "5,0 % &nbsp;·&nbsp; sprød, forfriskende og afbalanceret", "5.0% &nbsp;·&nbsp; crisp, refreshing and balanced", "56 / 79"),
], "30 cl / 50 cl", "30 cl / 50 cl")

BOTTLED = S("Flaskeøl", "Bottled beer", [
    I("Crabbies Ginger Beer", "Crabbies Ginger Beer", "33 cl &nbsp;·&nbsp; 4,0 %", "33 cl &nbsp;·&nbsp; 4.0%", "69"),
    I("Magners Cider", "Magners Cider", "56,8 cl &nbsp;·&nbsp; 4,5 %", "56.8 cl &nbsp;·&nbsp; 4.5%", "89"),
    I("Fur Porter", "Fur Porter", "50 cl &nbsp;·&nbsp; 6,5 %", "50 cl &nbsp;·&nbsp; 6.5%", "89"),
    I("Fur Bock", "Fur Bock", "50 cl &nbsp;·&nbsp; 7,6 %", "50 cl &nbsp;·&nbsp; 7.6%", "89"),
    I("Fur Renæssance", "Fur Renæssance", "50 cl &nbsp;·&nbsp; 6,2 %", "50 cl &nbsp;·&nbsp; 6.2%", "89"),
])

WINE_NOTE = ("15 cl / 25 cl / 75 cl", "15 cl / 25 cl / 75 cl")

BUBBLES = S("Bobler", "Bubbles", [
    I("Cava", "Cava", "Codorníu &mdash; Anna de Codorníu, Blanc de Blancs, Cava Brut", "Codorníu &mdash; Anna de Codorníu, Blanc de Blancs, Cava Brut", "90 / 150 / 450"),
    I("Crémant", "Crémant", "Maison Albert Sounit &mdash; Crémant de Bourgogne, Prestige Brut", "Maison Albert Sounit &mdash; Crémant de Bourgogne, Prestige Brut", "120 / 200 / 540"),
    I("Prosecco", "Prosecco", "Tor del Colle &mdash; Prosecco Tor del Colle", "Tor del Colle &mdash; Prosecco Tor del Colle", "120 / 200 / 540"),
    I("Champagne", "Champagne", "Nicolas Feuillatte &mdash; Cuvée Spéciale, Brut 2019", "Nicolas Feuillatte &mdash; Cuvée Spéciale, Brut 2019", "240 / 400 / 800"),
], *WINE_NOTE)

WHITE = S("Hvidvin", "White wine", [
    I("Chardonnay", "Chardonnay", "Hillgrove Creek Chardonnay, Australien, South Eastern Australia", "Hillgrove Creek Chardonnay, Australia, South Eastern Australia", "90 / 150 / 450"),
    I("Riesling", "Riesling", "Nik Weis Riesling Dry 2025, Tyskland, Mosel", "Nik Weis Riesling Dry 2025, Germany, Mosel", "120 / 200 / 540"),
    I("Sauvignon Blanc", "Sauvignon Blanc", "Henri Bourgeois &mdash; Petit Bourgeois Sauvignon Blanc 2024, Frankrig, Loire", "Henri Bourgeois &mdash; Petit Bourgeois Sauvignon Blanc 2024, France, Loire", "145 / 240 / 720"),
    I("Solaris", "Solaris", "Tusen Vin Fjordglimt 2024, Danmark, Sjælland, Holbæk", "Tusen Vin Fjordglimt 2024, Denmark, Sjælland, Holbæk", "160 / 260 / 800"),
], *WINE_NOTE)

RED = S("Rødvin", "Red wine", [
    I("Pinot Noir", "Pinot Noir", "Marterey Pinot Noir 2025, Frankrig, Pays d’Oc", "Marterey Pinot Noir 2025, France, Pays d’Oc", "90 / 150 / 450"),
    I("Barbera", "Barbera", "Marziano Abbona Langhe Barbera Casaret 2025, Italien, Piemonte", "Marziano Abbona Langhe Barbera Casaret 2025, Italy, Piemonte", "120 / 200 / 540"),
    I("Tempranillo", "Tempranillo", "Viña Pomal Reserva 2020, Spanien, Rioja Alta", "Viña Pomal Reserva 2020, Spain, Rioja Alta", "145 / 240 / 720"),
    I("Nebbiolo", "Nebbiolo", "Contea di Castiglione Barolo 2021, Italien, Piemonte, Barolo", "Contea di Castiglione Barolo 2021, Italy, Piemonte, Barolo", "160 / 260 / 800"),
], *WINE_NOTE)

ROSE = S("Rosévin", "Rosé wine", [
    I("Maison Saint AIX", "Maison Saint AIX", "Frankrig, Provence, Coteaux d’Aix en Provence", "France, Provence, Coteaux d’Aix en Provence", "120 / 200 / 540"),
    I("Whispering Angel", "Whispering Angel", "Château d’Esclans Whispering Angel 2025, Frankrig, Provence", "Château d’Esclans Whispering Angel 2025, France, Provence", "145 / 240 / 720"),
], *WINE_NOTE)

NON_ALC_LEFT = S("Kaffe og te", "Coffee and tea", [
    I("Kaffe", "Coffees",
      "Espresso 24 &nbsp;·&nbsp; cortado 30 &nbsp;·&nbsp; caffe latte 45 &nbsp;·&nbsp; cappuccino 45 &nbsp;·&nbsp; flat white 45 &nbsp;·&nbsp; iskaffe 65 &nbsp;·&nbsp; varm chokolade 55",
      "Espresso 24 &nbsp;·&nbsp; cortado 30 &nbsp;·&nbsp; cafe latte 45 &nbsp;·&nbsp; cappuccino 45 &nbsp;·&nbsp; flat white 45 &nbsp;·&nbsp; ice latte 65 &nbsp;·&nbsp; chocolate 55", None),
    I("Te", "Tea selection",
      "Sort te, kamillete, grøn te, lakridste",
      "Black tea, chamomile tea, green tea, liquorice tea", "49"),
    I("Friskpresset appelsinjuice", "Fresh orange juice",
      "Presses hver dag &nbsp;·&nbsp; 30 cl 59 &nbsp;·&nbsp; 50 cl 79",
      "Freshly squeezed every day &nbsp;·&nbsp; 30 cl 59 &nbsp;·&nbsp; 50 cl 79", None),
])

NON_ALC_RIGHT = S("Sodavand og andet", "Soft drinks and more", [
    I("Sodavand", "Flavoured soda",
      "Pepsi, Pepsi Max, Mirinda lemon, Mirinda orange, Faxe Kondi &nbsp;·&nbsp; 30 cl 42 &nbsp;·&nbsp; 50 cl 69",
      "Pepsi, Pepsi Max, Mirinda lemon, Mirinda orange, Faxe Kondi &nbsp;·&nbsp; 30 cl 42 &nbsp;·&nbsp; 50 cl 69", None),
    I("Filtreret vand", "Filtered water",
      "Med eller uden brus &nbsp;·&nbsp; 30 cl 29 &nbsp;·&nbsp; 75 cl 69",
      "Still or sparkling &nbsp;·&nbsp; 30 cl 29 &nbsp;·&nbsp; 75 cl 69", None),
    I("Lemonade", "Lemonades",
      "Hyldeblomst, fersken fra Lipton, lemonade fra Lipton",
      "Elderflower, peach from Lipton, lemonade from Lipton", "49"),
    I("Mimosa", "Mimosa",
      "Friskpresset appelsinjuice og prosecco &nbsp;·&nbsp; glas 75 &nbsp;·&nbsp; kande 300",
      "Fresh orange juice and prosecco &nbsp;·&nbsp; glass 75 &nbsp;·&nbsp; pitcher 300", None),
    I("Dansk tømmermændskur", "Danish hangover drink / hair of the dog",
      "Lille pilsner 30 cl og Gammel Dansk 3 cl",
      "Small pilsner 30 cl and Gammel Dansk 3 cl", "75"),
])


# The printed menu splits smørrebrød over two columns under one heading; the
# site renders it as a single section that flows into two columns on desktop.
SMORREBROD = S(SMORREBROD_LEFT["label_da"], SMORREBROD_LEFT["label_en"],
               SMORREBROD_LEFT["items"] + SMORREBROD_RIGHT["items"])


# ------------------------------------------------------- homepage highlights
# Six dishes shown on the front page, and the names scrolling in the marquee.
# Both are drawn from the menu above so the homepage can never quote a dish or
# a price the kitchen no longer serves.
HOME_FAVOURITES = [
    I("Stjerneskud", "Shootingstar",
      "Stegte og dampede rødspættefileter med rejer, asparges og dressing",
      "Fried and steamed fillets of plaice with shrimps, asparagus and dressing", "179"),
    I("Fish &amp; chips", "Fish n chips",
      "Frisk kuller, sauce tartare eller remoulade, sprøde pommes frites og citron",
      "Fresh haddock, sauce tartare or remoulade, golden fries and lemon", "169"),
    I("Wienerschnitzel", "Wiener schnitzel",
      "Sprødpaneret kalvekød med stegte kartofler, ærter, citron, kapers og ansjoser",
      "Crispy breaded veal with fried potatoes, peas, lemon, capers and anchovies", "198"),
    I("Steak frites af oksemørbrad", "Steak frites of beef filet",
      "Valgfri sauce: bearnaise eller grøn peber, sprøde pommes frites og grøn salat",
      "Optional sauce: bearnaise or green peppercorn, golden fries and green salad", "198"),
    I("Biksemad", "Biksemad",
      "Kartofler i tern, løg og møre stykker kød, stegt gyldent og sprødt, med spejlæg og rødbeder",
      "Diced potatoes, onions and tender pieces of meat, pan-fried until golden and crispy, with a fried egg and beetroot", "159"),
    I("Stegt flæsk", "Stegt flæsk",
      "Sprødstegt flæsk med kogte kartofler og cremet persillesovs",
      "Crispy pork belly with boiled potatoes and a creamy parsley sauce", "159"),
]

MARQUEE = [
    ("Smørrebrød", "Smørrebrød"),
    ("Stjerneskud", "Shootingstar"),
    ("Fish &amp; Chips", "Fish &amp; Chips"),
    ("Burger", "Burger"),
    ("Wienerschnitzel", "Wiener Schnitzel"),
    ("Biksemad", "Biksemad"),
    ("Frikadeller", "Danish Meatballs"),
    ("Stegt Flæsk", "Stegt Flæsk"),
]
