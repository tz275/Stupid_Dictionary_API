import justpy as jp



class Doc:
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=div, text="Get definitions of words: ", classes="text-lg")
        # Horizontal Line
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=moon")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "water", 
        "definition": ["Significant accumulation of water, 
        covering the Earth or another planet.", 
        "Common liquid (H\u2082O) which forms rain, rivers, 
        the sea, etc., and which makes up a large part of the bodies of organisms.", 
        "To pour water onto the soil surrounding plants.", 
        "Of the eyes: To secrete tears because of an irritation caused by wind, smoke etc."]}
        """)
        return wp

