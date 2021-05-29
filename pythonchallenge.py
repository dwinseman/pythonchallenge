import logging
import urllib.request
import textwrap

FORMAT = '%(asctime)-15s %(name)s %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

def fetch_url(url, logger):
    logger.info("fetching url:\n\t%s", url)
    response = urllib.request.urlopen(url)
    logger.info("\n" + textwrap.indent(str(response.headers), "\t"))
    if response.code != 200:
        return None
    body = response.read()
    logger.debug(body)
    return (response, body)

class challenge_level(object):
    def __init__(self, level_id, starting_url):
        self._url = starting_url
        self._url_root = self._url[:self._url.rfind("/")+1]
        logging.info(self._url_root)
        self._logger = logging.getLogger("Level #" + str(level_id))
        self._logger.info("starting level %s...", str(level_id))
        self._data = fetch_url(self._url, self._logger)
        if self._data is None:
            self._logger.warning("No data available. Stopping the challenge.")
        self()
        self.next()             

class level_0(challenge_level):
    def __init__(self, starting_url):
        super().__init__(0, starting_url)

    def __call__(self):
        x = pow(2, 38)
        self._next_url = self._url_root + str(x) + ".html"
        self._logger.info("next_url:\n\t[%s]", self._next_url)

    def next(self):
        level_1(self._next_url)

class level_1(challenge_level):
    def __init__(self, starting_url):
        super().__init__(1, starting_url)

    def __call__(self):
        pass

    def next(self):
        pass

def main():
    logging.info("Hello World! Let's try the python challenge...")

    url = "http://www.pythonchallenge.com/pc/def/0.html"
    x = level_0(url)
    #x()

if __name__ == "__main__":
    main()
