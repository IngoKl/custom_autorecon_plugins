from autorecon.plugins import ServiceScan

class FTPBasicEnumeration(ServiceScan):

    def __init__(self):
        super().__init__()
        self.name = 'ftp-basic-enumeration'
        self.description = 'Performs Python-based enumeration'
        self.type = 'tcp'
        self.tags = ['default', 'community', 'ftp', 'safe']

    def configure(self):
        self.match_service_name('ftp')

    async def run(self, service):
        cmd = 'basic-ftp-enumeration.py {address} > {scandir}/{protocol}_{port}_basic-ftp-enumeration.txt'
        await service.execute(cmd)
