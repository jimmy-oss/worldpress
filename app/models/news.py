class News:
    '''
    News source class to define sources objects
    '''

    def __init__(self,id,name,description,url,category,country,publishedAt,content):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.publishedAt = publishedAt
        self.content = content