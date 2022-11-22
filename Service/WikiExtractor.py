import wikipedia

class WikiResult:
    #Constructor
    def __init__(self,url,title,definition,summary,image=None): 
        self.url=url
        self.title = title
        self.definition = definition 
        self.summary = summary 
        self.image = image 
    def __repr__(self):
        return f"<WikiResult url={self.url},title={self.title},definition={self.definition},summary={self.summary},image={self.image}"

#search_keyword="Mechanical_energy"

def extractInfoFromWikipedia(search_keyword):
    page = wikipedia.page(search_keyword)
    wikiResult=WikiResult(page.url,page.title,page.title,page.summary)
    wikiResult.definition=wikipedia.summary(search_keyword, sentences = 2)
    if len(page.images) > 0 :
        wikiResult.image=page.images[0]
    print(wikiResult)
    return wikiResult










