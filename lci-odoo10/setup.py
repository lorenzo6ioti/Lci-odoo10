from ConfigParser import ConfigParser
from setuptools import setup


cfg = ConfigParser()
cfg.read('acsoo.cfg')


setup(
    version=cfg.get('acsoo', 'series') + '.' + cfg.get('acsoo', 'version'),
    name='odoo-addons-lci-odoo10',
    description='Lci-odoo10 Odoo Addons',
    setup_requires=['setuptools-odoo'],
    odoo_addons=True,
)
