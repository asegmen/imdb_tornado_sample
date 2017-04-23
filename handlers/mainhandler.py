import tornado.web
import tornado.template
from tornado import gen
from helpers import content_helpers
from helpers import json_helpers

class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        try:
            movie_list = json_helpers.get_movies(self.settings.get('data_path'))
            items = []
            if movie_list is not None:
                for movie in movie_list:
                    item = content_helpers.get_content_by_title(movie['title'])
                    items.append(item)
                self.render("index.html", items=items)
            else:
                self.write("list is null")
        except:
            raise tornado.web.HTTPError(status_code=404)
