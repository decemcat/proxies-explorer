import jsonpath


class ResourceLocator:
    def get_ip_ports(self, response) -> list:
        pass


class JsonResourceLocator(ResourceLocator):
    def __init__(self, ip_port_separate: bool, **kwargs):
        self.__ip_port_separate = ip_port_separate
        if self.__ip_port_separate:
            self.__ip_path = kwargs['ip_path']
            self.__port_path = kwargs['port_path']
        else:
            self.__ip_port_path = kwargs['ip_port_path']
            self.__delimiter = kwargs['delimiter']

    def get_ip_ports(self, response) -> list:
        data = response.body.decode('utf-8')
        jsonpath.jsonpath(data, self.__ip_path)
        return list()



class XPathResourceLocator(ResourceLocator):
    def __init__(self, location: str, position: int, text_pos: str, ip_pos: int, port_pos: int):
        self.__location = location
        self.__position = position
        self.__text_pos = text_pos
        self.__ip_pos = ip_pos
        self.__port_pos = port_pos

    def get_ip_ports(self, response) -> list:
        pass
