# PyNYT # ian-double-u #

class PyNYT():
    def __init__(self,api_key):
        self.api_key = api_key
    
    ## Different APIs ##
    
    # Get all NYT article metadeta for a given month #
    def archive(self):
        print('Get all NYT article metadeta for a given month')
    
    # Search for NYT articles #
    def search(self):
        print('Search for NYT articles')
    
    # Get NYT Best Sellers Lists and lookup book reviews #
    def books(self):
        print('Get NYT Best Sellers Lists and lookup book reviews')
        
    # Get user comments #
    def community(self):
        print('BETA\n\n')
        print('Get user comments')
        
    # Popular articles on NYTimes.com #
    def popular(self):
        print('Popular articles on NYTimes.com')
    
    # Search for movie reviews #
    def movies(self):
        # TODO
        endpoint_base = 'https://api.nytimes.com/svc/movies/v2'
        
        # might need more than one function for movies
        # like one for critics
        # one for reviews, etc.
        # or maybe look into subclasses
        
    
    # NYT RSS section feeds #
    def rss(self):
        print('NYT RSS section feeds')
    
    # Get semantic terms (people, places, organizations, and locations) #
    def semantic(self):
        print('Get semantic terms (people, places, organizations, and locations)')
    
    # NYT controlled vocabulary #
    def tags(self):
        print('NYT controlled vocabulary')
    
    # Real-time feed of NYT article publishes #
    def wire(self):
        print('Real-time feed of NYT article publishes')
    
    # Get articles currently on a section or the home page #
    def top_stories(self):
        print('Get articles currently on a section or the home page')
    
    ## - - - ##
    
def PyNYT_help():
    print('Here is some stuff to help...')
    
r1 = PyNYT('YOUR_API_KEY_HERE')