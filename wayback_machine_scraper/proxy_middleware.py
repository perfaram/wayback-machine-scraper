class ProxyMiddleware:
    connection_string: str = None

    def process_request(self, request, spider):
        if self.connection_string is not None:
            request.meta['proxy'] = self.connection_string