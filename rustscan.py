from autorecon.plugins import PortScan
from autorecon.io import info, error
from autorecon.config import config
import os, re

class QuickRustScanScan(PortScan):

    def __init__(self):
        super().__init__()
        self.name = 'Quick RustScan'
        self.description = 'Performs a basic RustScan scan.'
        self.type = 'tcp'
        self.tags = ['default', 'additional-port-scan']
        self.priority = 0

    async def run(self, target):
        if target.ports: # Don't run this plugin if there are custom ports.
            return []

        process, stdout, stderr = await target.execute('rustscan -a {address} -g -t 10000 --ulimit 5000 > "{scandir}/_quick_rustscan.txt"', blocking=False)
        services = await target.extract_services(stdout)
        await process.wait()
        return services
