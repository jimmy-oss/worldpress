import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("BBC News","US East Coast hunkers down for 'bombogenesis' snowstorm - BBC News","https://www.facebook.com/bbcnews","general","us", "https://ichef.bbci.co.uk/news/1024/branded_news/60B2/production/_123045742_gettyimages-1238044808.jpg","2022-01-29T05:45:49Z","Image source, Getty Images\r\nThe US East Coast is bracing for a major blizzard to hit the region for the first time in four years. \r\nThe storm is forecast to stretch from the Carolinas to Maine, packi… [+2120 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()