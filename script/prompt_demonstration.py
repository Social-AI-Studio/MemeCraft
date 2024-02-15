
context_string = {}
# List down top 5 <Aspects> of Climate Change
cause = '''Causes of Climate Change "Greenhouse Gas Emissions, Deforestation, Agriculture and Livestock, Industrial Processesa, Transportation..." \n'''
consequences = '''Consequences of Climate Change "Rising Global Temperatures, Melting Ice and Rising Sea Levels, Extreme Weather Events, Ocean Acidification, Ecosystem Disruption and Biodiversity Loss..." \n'''
solutions = '''Solutions of Climate Change "Transition to Renewable Energy, Energy Efficiency Improvements, Afforestation and Reforestation, Climate Policy and Regulations, Climate Adaptation and Resilience..." \n'''
context_string["Supporter"] = {}
context_string["Supporter"]["Causes"] = cause 
context_string["Supporter"]["Consequences"] = consequences 
context_string["Supporter"]["Solutions"] = solutions 

generation_question = '''Question: Generate a caption to turn the image into a humorous meme that highlights the <Context> of Climate Change to <Stance2> it. \n''' # climate change

image_selection_pools = {}
image_selection_pool = []
image_selection_pool.append({
        "Name": "willywonka",
        "Caption": "A man wearing a purple and gold suit, a top hat, and a smile sits in a chair, posing for the camera.", 
        "COT": '''The "willywonka" image is frequently employed sarcastically, often with rhetorical questions. Let's use it for a meme emphasizing how Greenhouse gas emissions significantly contribute to climate change, making politicians and oil companies' statements unreliable.''',
        "Text": '''You think global warming is fake? - Please tell me how you get the "FACTS" from politicians and oil companies'''
    })
image_selection_pool.append({
        "Name": "Toilet tissue hoard",
       "Caption": "In the image, a large stack of toilet paper rolls is placed next to a stack of bottled water.", 
         "COT": '''The "Toilet tissue hoard" image is frequently associated with panic buying during crises and its connection to deforestation. Let's use this image for a meme that underscores how deforestation is a significant contributor to climate change.''',
        "Text": '''The climate change deniers house'''
    })
image_selection_pool.append({
        "Name": "cow",
        "Caption": "In the image, a cow is standing in a grassy field, looking at the camera with its eyes wide open.", 
        "COT": '''The "cow" image is often linked to agriculture. Let's use this image for a meme that emphasizes how agriculture is a significant driver of climate change.''',
        "Text": '''When you realize your meaty diet contributes to the global warming'''
    })
image_selection_pool.append({
        "Name": "angry doge with gun",
        "Caption": "A Shiba Inu dog is holding a gun and appears to be very angry, with its mouth wide open and teeth showing.", 
        "COT": '''The "angry doge with gun" meme is frequently employed to convey disapproval of certain actions. Let's create a new meme using this image to scold those who contribute to climate change by neglecting to turn off lights.''',
        "Text": '''If you are not Climate change Denier - Turn off the lights when leaving the room!!!'''
    })

image_selection_pools["Supporter"] = {}
image_selection_pools["Supporter"]["Causes"] = image_selection_pool

image_selection_pool = []
image_selection_pool.append({
        "Name": "What if I told you",
        "Caption": "The image features a man wearing glasses, a black jacket, and a black shirt, with a pair of sunglasses on his head.", 
        "COT": '''The "What if I told you" image often begins with the phrase "What if I told you" and is followed by a question about social behavior. Let's use this image for a meme that emphasizes how climate change's impact extends beyond wildlife in polar regions.''',
        "Text": '''WHAT IF I TOLD YOU - CLIMATE CHANGE DOESN'T ONLY AFFECT THE POLAR BEARS'''
    })
image_selection_pool.append({
        "Name": "Leonardo DiCaprio is Swimming",
        "Caption": "In the image, a man is floating in the ocean wearing sunglasses and a hat.", 
        "COT": '''The "Leonardo DiCaprio is Swimming" image, commonly used humorously in casual settings, references the Titanic sinking. Let's use this image for a meme that playfully suggests that, thanks to global warming—an outcome of climate change—Leonardo could have avoided the icy waters and survived.''',
        "Text": '''Some Years After Global Warming... - Rose?'''
    })
image_selection_pool.append({
        "Name": "Sandy with a wedding outfit!",
        "Caption": "A cute squirrel wearing a wedding dress and a diving oxygen mask is sitting on a flag, holding a bouquet of flowers.", 
        "COT": '''The image of "Sandy in a wedding outfit" shows a cartoon character attending an underwater wedding, wearing a diving oxygen mask. et's use this image for a meme that emphasizes the impact of climate change with rising sea levels, suggesting that future activities might take place underwater.''',
        "Text": '''Wedding in Climate Change'''
    })
image_selection_pool.append({
        "Name": "first world problems",
        "Caption": "A frog with a big mouth is sitting on a green leaf, making a funny face.", 
         "COT": '''The "first world problems" image usually shows someone frustrated over a minor inconvenience. Let's use this image for a meme that reminds us of our privilege to worry about trivial issues compared to the severe consequences of climate change.''',
        "Text": '''Curses, Global Warming! - It's melting my ice cream when I can't decide which flavor to choose'''
    })
image_selection_pools["Supporter"]["Consequences"] = image_selection_pool

image_selection_pool = []
image_selection_pool.append({
        "Name": "It'd Be A Lot Cooler If You Did",
        "Caption": "In the image, a man is sitting in a car, smiling and pointing at something outside the vehicle.", 
        "COT": '''The "It'd Be A Lot Cooler If You Did" image is humorously used as a response to questions with the phrase "Be A Lot Cooler If You Did." Let's create a meme using this phrase as a witty reply to those denying support for renewables, a crucial solution to Climate Change.''',
        "Text": '''Governments: Were not gonna support renewables - Scients: '''
    })
image_selection_pool.append({
        "Name": "Big Ship",
        "Caption": "In the image, a large ship is docked at a port, and a small crane is lifting a container off the ship.", 
         "COT": '''The "Big Ship" image humorously compares a large ship representing a big problem with a small crane representing a tiny step towards its solution. Let's create a meme where the big ship symbolizes climate change, and the small crane represents the use of e-cars as a small but essential step towards tackling the issue.''',
        "Text": '''climate change - driving an e-car'''
    })
image_selection_pool.append({
        "Name": "One Does Not Simply",
        "Caption": "The image features a close-up of the face of a scruffy, beardy man holding a finger up while wearing a brown blazer, jeans, and hooded jacket.", 
         "COT": '''The "One Does Not Simply" image humorously emphasizes the difficulty of accomplishing certain tasks. Let's create a meme using this image to underscore the significance of taking small actions in the fight against climate change.''',
        "Text": '''One does not simply save the planet in one day... - but recycling and buying eco-friendly products is a good start!'''
    })
image_selection_pool.append({
        "Name": "Bored Spongebob",
        "Caption": "In the image, a man is standing on a beach, looking at the camera with a blank expression.", 
         "COT": '''The "Bored Spongebob" image humorously exposes commonly known but overlooked facts. Let's create a meme using this image to emphasize the significance of recycling in preventing climate change.''',
        "Text": '''me: "single-use plastic is ok if you reuse it"'''
    })
image_selection_pools["Supporter"]["Solutions"] = image_selection_pool




cause = '''Evidence of Absence of Climate Change "Short-term temperature fluctuations, Natural climate variability, No consensus among scientists, Data manipulation and errors, Limited historical data..." \n'''
consequences = '''Benefits of Climate Change "Longer Growing Seasons, Opening of New Trade Routes, Increased Tourism in Some Areas, Expanded Habitats for Some Species, Enhanced Renewable Energy Potential..." \n'''
context_string["Denier"] = {}
context_string["Denier"]["Evidence of Absence"] = cause 
context_string["Denier"]["Benefits"] = consequences 

image_selection_pool = []
image_selection_pool.append({
        "Name": "Jack Nicholson The Shining Snow",
        "Caption": "A man is sitting in the snow, wearing a red jacket and a beard, with his head covered in frost.", 
        "COT": '''The "Jack Nicholson Shining Snow" image portrays a man struggling in the snow and is sometimes used as evidence against global warming. Let's create a meme that humorously questions Al Gore, the chair of The Climate Reality Project, by implying that climate change has no impact on polar bear populations, playfully suggesting that it isn't real.''',
        "Text": '''WHEN AL GORE WAS BORN ONLY 7000 POLAR BEARS EXISTED - NOW ONLY 26,000 POLAR BEARS REMAIN'''
    })
image_selection_pool.append({
        "Name": "Futurama Fry",
        "Caption": "The image shows a young man with long orange hair, which is a distinctive red hair color typically associated with anime characters.", 
        "COT": '''The "Futurama Fry" image frequently expresses confusion or skepticism. Let's create a meme that playfully questions the scientific consensus on climate change by implying that it's all just a big misunderstanding of data.''',
        "Text": '''So you're telling me the Earth is getting warmer - but I'm still freezing my butt off in winter'''
    })
image_selection_pool.append({
        "Name": "Solar power",
        "Caption": "A man is sitting on a rock, using his cell phone while wearing a solar-powered hat, charging his device in the sun.", 
        "COT": '''The "Solar power" meme illustrates a man charging his phone using solar power, which is portrayed as ineffective. We can create a meme with this image to highlight that some businesspeople may exploit climate change as an excuse to sell solar panels.''',
        "Text": '''When you realize climate change is just a ploy to sell more solar panels.'''
    })
image_selection_pool.append({
        "Name": "Roll Safe Think About It",
        "Caption": "A man with a beard is sitting in a chair, wearing a black shirt and a black jacket, and making a funny face.", 
         "COT": '''The "Roll Safe Think About It" image is often used in discussions about social events to prompt people to reconsider their perspectives. Let's create a meme playfully questioning the reality of Climate Change, suggesting it might be akin to short-term temperature fluctuations, resembling a mere hot flash in a person.''',
        "Text": '''Is Climate Change Real? - Unsure if it's Mother Nature just having a hot flash!'''
    })

image_selection_pools["Denier"] = {}
image_selection_pools["Denier"]["Evidence of Absence"] = image_selection_pool

image_selection_pool = []
image_selection_pool.append({
        "Name": "Icebreaker",
        "Caption": "In the image, a large ship is sailing through a vast expanse of ice-covered water.", 
        "COT": '''The "Icebreaker" image shows humans breaking ice in high latitudes of the ocean. Let's create a meme that humorously highlights one potential benefit of global warming, such as the opening of new trade routes without the need for Icebreakers.''',
        "Text": '''Thanks to global warming - the Northwest Passage is no longer an impossible feat'''
    })
image_selection_pool.append({
        "Name": "Antarctica Is Getting Greener",
        "Caption": "In the image, a lush green hillside is covered with moss and lichen, creating a vibrant and verdant landscape.", 
        "COT": '''The "Antarctica Is Getting Greener" image beautifully showcases the scenic transformation of Antarctica. Let's create a meme that humorously highlights one positive aspect of global warming, such as the rise in tourism in certain regions like Antarctica.''',
        "Text": '''Global warming: - Now even Antarctica wants to show off its green thumb!'''
    })
image_selection_pool.append({
        "Name": "Leonardo Dicaprio Vacation",
        "Caption": "A shirtless man is playing with a water gun in a grassy field, enjoying a fun and refreshing summer activity.", 
        "COT": '''"The "Leonardo DiCaprio Vacation" meme depicts a man joyfully relishing his vacation during a hot season. By creating a meme with this image, we emphasize that climate change may can lead to more sunny days and more delightful vacations."''',
        "Text": '''Can you believe it? - More sunny days and beach vacations if global warming is real?'''
    })
image_selection_pool.append({
        "Name": "farmer",
        "Caption": "A man in a cowboy hat and overalls stands in a vineyard, holding a large garden hoe, enjoying the beautiful scenery.", 
         "COT": '''The "farmer" image can be used to highlight potential agricultural benefits from climate change, like longer growing seasons. Let's create a meme showcasing this advantage!''',
        "Text": '''Global warming? - Now winter is my new farming season!'''
    })
image_selection_pools["Denier"]["Benefits"] = image_selection_pool




context_string = {}
# List down top 5 <Aspects> of gender inequality
cause = '''Causes of Gender Inequality "Social Norms and Stereotypes, Economic Disparities, Education Disparities, Violence and Discrimination and Political Underrepresentation..." \n'''
consequences = '''Consequences of Gender Inequality "Economic Disparities, Limited Access to Education, Health Disparities, Violence Against Women and Underrepresentation in Decision-Making..." \n'''
solutions = '''Solutions of Gender Inequality "Education and Awareness, Economic Empowerment, Legal and Policy Reforms, Healthcare and Reproductive Rights and Cultural and Social Change..." \n'''
context_string["Supporter"] = {}
context_string["Supporter"]["Causes"] = cause 
context_string["Supporter"]["Consequences"] = consequences 
context_string["Supporter"]["Solutions"] = solutions 

generation_question = '''Question: Generate a caption to turn the image into a humorous meme that highlights the <Context> of Gender Inequality to <Stance2> Gender Equality. \n''' # climate change

image_selection_pools = {}
image_selection_pool = []
image_selection_pool.append({
        "Name": "Trump Bill Signing",
        "Caption": "The President, holding a framed parchment document, poses with his fellow officials for a photo.", 
        "COT": '''The "Trump Bill Signing" image captures a moment of political power and influence. To create a meme highlighting the causes of gender inequality, we can playfully reference how policy decisions can impact gender equality.''',
        "Text": '''Signing bills without considering gender equality - Oops, did we forget something important again?'''
    }) 
image_selection_pool.append({
        "Name": "Dumb Blonde",
        "Caption": "The image features a curly-haired woman with sunglasses and a co2lorful background, possibly featuring a rainbow. She looks like she is waving to the camera, suggesting a friendly and approachable demeanor.", 
        "COT": ''''The 'Dumb Blonde' stereotype portrays attractive women as unintelligent. Let's create a meme to highlight how this stereotype contributes to gender inequality and has a negative impact.''',
        "Text": '''WHY DO PEOPLE CALL ME 'BLONDE DUMB' SIMPLY BECAUSE OF MY HAIR COLOR?'''
    })
image_selection_pool.append({
        "Name": "willywonka",
        "Caption": "A man wearing a purple and gold suit, a top hat, and a smile sits in a chair, posing for the camera.", 
        "COT": '''The 'willywonka' image is frequently employed sarcastically, often with rhetorical questions. We can use it in a meme to spotlight stereotypes that causes gender inequality, such as the notion that women should primarily be responsible for cooking.''',
        "Text": '''Gender equality in society are not influenced by the media - Honey, go make me a sandwich while I tell you more about it.'''
    })
image_selection_pool.append({
        "Name": "Leave Brittney alone",
        "Caption": "The image shows a young man with long brown hair, holding his head in his hands and crying on the side of the bed.", 
        "COT": '''The "Leave Brittney alone" image captures a moment of emotional distress. To create a meme highlighting the issues of violence and discrimination in gender inequality and to support gender equality, we can use this image to emphasize the importance of empathy and understanding.''',
        "Text": '''"WHEN GENDER INEQUALITY SPARKS VIOLENCE - LET'S STEP IN AND SAY, 'LEAVE HER/HIM ALONE'.''',
    }) 

image_selection_pools["Supporter"] = {}
image_selection_pools["Supporter"]["Causes"] = image_selection_pool

image_selection_pool = []
image_selection_pool.append({
        "Name": "Leave Brittney alone",
        "Caption": "The image shows a young man with long brown hair, holding his head in his hands and crying on the side of the bed.", 
        "COT": '''The "Leave Brittney alone" image became famous as a representation of the emotional distress faced by individuals due to societal scrutiny and judgment. To create a meme highlighting the consequences of gender inequality, we can focus on the pressure and expectations placed on women in the public eye.''',
        "Text": '''Society demands women to be perfect - yet I struggle to pick an outfit every morning!''',
    }) # consequence
image_selection_pool.append({
        "Name": "Dumb Blonde",
        "Caption": "The image features a curly-haired woman with sunglasses and a colorful background, possibly featuring a rainbow. She looks like she is waving to the camera, suggesting a friendly and approachable demeanor.", 
        "COT": ''''The 'Dumb Blonde' stereotype portrays attractive women as unintelligent. Let's craft a meme to spotlight the harmful effects of gender inequality stereotypes on blonde beauty.''',
        "Text": '''WHY DO PEOPLE CALL ME 'BLONDE DUMB' SIMPLY BECAUSE OF MY HAIR COLOR?'''
    })
image_selection_pool.append({
        "Name": "willywonka",
        "Caption": "A man wearing a purple and gold suit, a top hat, and a smile sits in a chair, posing for the camera.", 
        "COT": '''The 'willywonka' image is often used sarcastically, usually with rhetorical questions. Let's use it in a meme to highlight stereotypes that link women to cooking, resulting in some husbands demanding sandwiches without appreciation.''',
        "Text": '''Gender equality in society are not influenced by the media - Honey, go make me a sandwich while I tell you more about it.'''
    })
image_selection_pool.append({
        "Name": "Trump Bill Signing",
        "Caption": "The President, holding a framed parchment document, poses with his fellow officials for a photo.", 
        "COT": '''The "Trump Bill Signing" image exemplifies a moment of political authority and its potential relevance in highlighting the consequence of gender inequality: underrepresentation in decision-making, as politicians often overlook gender equality.''',
        "Text": '''When they said 'equal opportunities for all genders' - Not sure this is what they had in mind'''
    }) 
image_selection_pools["Supporter"]["Consequences"] = image_selection_pool

image_selection_pool = []
image_selection_pool.append({
        "Name": "Dumb Blonde",
        "Caption": "The image features a curly-haired woman with sunglasses and a colorful background, possibly featuring a rainbow. She looks like she is waving to the camera, suggesting a friendly and approachable demeanor.", 
        "COT": '''The 'Dumb Blonde' image portrays attractive women as unintelligent. Let's create a meme to against this gender inequality stereotype and emphasize that beauty and intelligence can coexist in women.''',
        "Text": '''They called me 'Dumb Blonde' - they clearly hadn't seen my PhD in astrophysics!'''
    }) 
image_selection_pool.append({
        "Name": "Trump Bill Signing",
        "Caption": "The President, holding a framed parchment document, poses with his fellow officials for a photo.", 
        "COT": '''The "Trump Bill Signing" image presents an opportunity to create a meme that humorously underscores that one solution of gender equality is by Legal and Policy Reforms.''',
        "Text": '''WHEN THEY SAID WOMEN CAN'T HANDLE POWER - WE SIGNED A BILL TO BREAK THAT GLASS CEILING!'''
    }) 
image_selection_pool.append({
        "Name": "willywonka",
        "Caption": "A man wearing a purple and gold suit, a top hat, and a smile sits in a chair, posing for the camera.", 
        "COT": '''The 'willywonka' image exemplifies a man embracing elegance. This image can be used to create a meme emphasizing that breaking gender stereotypes involves raising awareness that men can also dress stylishly, just like women.''',
        "Text": '''Real men don't wear purple and gold? - I am here to redefine 'real'!'''
    })
image_selection_pool.append({
        "Name": "Leave Brittney alone",
        "Caption": "The image shows a young man with long brown hair, holding his head in his hands and crying on the side of the bed.", 
        "COT": '''The "Leave Brittney alone" image provides an opportunity to create a meme that humorously highlights the importance of empathy and support as a solution to gender inequality.''',
        "Text": '''JUDGING WOMEN FOR SHOWING EMOTIONS - REAL STRENGTH IS STANDING BY THEM, NOT TEARING THEM DOWN!''',
    }) 
image_selection_pools["Supporter"]["Solutions"] = image_selection_pool


cause = '''Evidence of Absence of Gender Inequality "..." \n'''
consequences = '''Benefits of Gender Inequality "..." \n'''
context_string["Denier"] = {}
context_string["Denier"]["Evidence of Absence"] = cause 
context_string["Denier"]["Benefits"] = consequences 

image_selection_pool = []
image_selection_pool.append({
        "Name": "Pissed Off Obama",
        "Caption": "The image features a man wearing a suit, tie, and sunglasses, extending his right index finger and pointing it towards the camera. The man appears to be an adult.", 
        "COT": '''The 'Pissed Off Obama,' a popular symbol of intense emotion about specific social issues. It visually represents those who vehemently deny gender equality, using the president as a backdrop.''',
        "Text": '''"As POTUS, I proudly declare that in the US, gender inequality has gone extinct!'''
    })
image_selection_pool.append({
        "Name": "Liam Neeson Taken 2",
        "Caption": "A man is seen talking on his cell phone, possibly seeking help, while wearing headphones.", 
        "COT": '''The 'Liam Neeson Taken 2' picture is frequently used as a symbolic response to queries. We may use this image to show that there are laws in place to guarantee gender equality, implying that there is no evidence of gender discrimination. This is not a problem that should worry everyone.''',
        "Text": '''Hey, you're looking for my support on gender equality? - We've got laws in place for that; I reckon they should do the trick!'''
    })
image_selection_pool.append({
        "Name": "Its Not Going To Happen",
        "Caption": "In the image, a beautiful young woman with brown hair is sitting in a classroom, looking into the camera. She has a serious look on her face and may be talking to someone, implying that she is engaged and focused on her class.", 
        "COT": '''Turning the 'It's Not Going To Happen' image into one action against a certain attitude. We can use this image as a response to deny there are still existence of gender inequality in our country.''',
        "Text": '''Gender inequality in our country, are you kidding me? - It's Not Going To Happen'''
    })
image_selection_pool.append({
        "Name": "Technologically Impaired Duck",
        "Caption": "A white duck is standing and smiling next to a multi-colored background..", 
        "COT": '''The 'Technologically Impaired Duck' meme, often used to poke fun at someone's lack of tech-savviness, can be repurposed to humorously deny the existence of gender inequality.''',
        "Text": '''When someone claims gender inequality still exists - I'm just here for laughter."'''
    })

image_selection_pools["Denier"] = {}
image_selection_pools["Denier"]["Evidence of Absence"] = image_selection_pool

image_selection_pool = []
image_selection_pool.append({
        "Name": "therefore-aliens",
        "Caption": "The image depicts a man with a wild head of hair sitting in a room, holding his arms up in the air and pretending to show something. The man appears to be in a suit, suggesting a formal setting. Despite his wild hair, he seems to be engaged and involved in a conversation with someone in the room, giving off an amusing and somewhat unpredictable vibe.", 
        "COT": '''The 'therefore-aliens' image, often used humorously to satirize and question social issues, highlights that one factor in gender inequality is the presence of distinct gender traits. Our aim is to promote gender equality while recognizing and valuing individual characteristics.''',
        "Text": '''Can treat genders be like coffee? - We want equality but not everyone takes it the same!'''
    })
image_selection_pool.append({
        "Name": "Professor Farnsworth Good News Everyone",
        "Caption": "An old man in a lab coat is standing in front of a control panel, looking surprised and holding his glasses.", 
        "COT": '''The 'Professor Farnsworth Good News Everyone' meme is frequently employed to highlight scientific distinctions. This image can be employed to illustrate differences between women and men, deny the absolute concept of gender equality.''',
        "Text": '''Why I reject the notion of gender equality - Because women minus men are not equal to zero.'''
    })
image_selection_pool.append({
        "Name": "Man and woman microphone Meme",
        "Caption": "A man and a woman are sitting at a table with multiple microphones in front of them, surrounded by a group of reporters. They are likely attending a press conference or giving a statement to the media.", 
        "COT": '''The 'Man and Woman Microphone Meme' features a single image depicting two people standing before microphones. This image can be employed to emphasize the physical distinctions between men and women, such as differences in height. The justification for treating them differently stems from their inherent dissimilarities.''',
        "Text": '''GENDER EQUALITY ISN'T ABOUT MAKING THE MICROPHONE THE SAME HEIGHT FOR BOTH GENDERS'''
    })
image_selection_pool.append({
        "Name": "Its Not Going To Happen",
        "Caption": "In the image, a beautiful young woman with brown hair is sitting in a classroom, looking into the camera. She has a serious look on her face and may be talking to someone, implying that she is engaged and focused on her class.", 
        "COT": '''The 'It's Not Going To Happen' image is commonly used as action against a certain attitude. We can use this image as a response to treating men and women equally, recognizing their physical differences like strength while considering specific privileges for women in certain situations.''',
        "Text": '''Treat a woman like a man? It's Not Going To Happen - They're as different as apples and oranges!'''
    })
image_selection_pools["Denier"]["Rationale"] = image_selection_pool


# def prompt_generation_cot_gpt(name, caption, supporter, context, demo_number):
#     demo= ""
#     generation_question_demo = generation_question.replace("<Stance>", supporter).replace("<Stance2>", supporter.replace("Supporter", "support").replace("Denier", "deny")).replace("<Context>", context)
#     i = 0
#     for image in image_selection_pools[supporter][context]:
#         i += 1
#         if(i > demo_number):
#             break
#         Name = image["Name"]
#         Caption = image["Caption"]
#         COT = image["COT"]
#         Text = image["Text"]
#         demo += generation_question_demo  \
#                 +  'Input: Image "'+ Name+'" describing "' + Caption + '" \n' 

#         if(" - " in Text):
#             caption_top = Text.split(" - ")[0]
#             caption_bottom = Text.split(" - ")[1]
#             demo += 'Output: Let\'s think step by step. ' + COT + ' Caption at top: "' + caption_top + '" and Caption at bottom: "' + caption_bottom + '" \n'
#         else:
#             demo += 'Output: Let\'s think step by step. ' + COT + ' Caption at top: "' + Text + '" \n'
        
            
#     demo += generation_question_demo  \
#                 +  'Input: Image "'+ name+'" describing "' + caption + '" \n' \
#                 + 'Output: Let\'s think step by step. '
#     return demo 

# id = 3
# Supporter = "Denier"
# context = "Evidence of Absence"
# print(prompt_generation_cot_gpt(image_selection_pools[Supporter][context][id]["Name"],\
#                                  image_selection_pools[Supporter][context][id]["Caption"],\
#                                 Supporter, context, id))