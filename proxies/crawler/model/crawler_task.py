class ProxyCrawlerTask:
    def __init__(self, name: str, url: list, type: str, locator: ResourceLocator):
        self.name = name
        self.resources = url
        self.result_type = type
        self.locator = locator

