from autorecon.plugins import ServiceScan

class SSHAudit(ServiceScan):

    def __init__(self):
        super().__init__()
        self.name = 'ssh-audit'
        self.description = 'Runs ssh-audit against the target.'
        self.type = 'tcp'
        self.tags = ['default', 'community', 'ssh', 'safe']

    def configure(self):
        self.match_service_name('ssh')

    async def run(self, service):
        cmd = 'ssh-audit -n -p {port} {address} > {scandir}/{protocol}_{port}_ssh-audit.txt'
        await service.execute(cmd)
