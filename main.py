# PyNYT # ian-double-u #

import requests
import json

class Table():
    def __init__(self,columns,data):
        self.columns = []
        self.data = []

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
    def movies(self,critic=False,review=False,table_friendly=False,
               critic_search='all'):
        
        base = 'https://api.nytimes.com/svc/movies/v2'
        summit = 'api-key=' + self.api_key

        def movies_critic(self,critic_search,table_friendly):
            url = base + '/critics/' + critic_search + '.json?' + summit
            
            result = requests.get(url)
            result = json.load(result.text)

            if table_friendly:
                table_data = []
                
                
                return Table(columns=['display_name',
                                      'sort_name',
                                      'status',
                                      'bio',
                                      'sea_name',
                                      'multimedia'],data=table_data)
            
            else:
                return result
        
        def movies_review(self):
            pass
        
        if critic:
            movies_critic(self=self,critic_search=critic_search,
                          table_friendly=table_friendly)
            return
        elif review:
            movies_review(table_friendly)
            return
        else:
            return
        
        # - - - 
        
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