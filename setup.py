from setuptools import setup

setup(
    name="electrum-server",
    version="1.0",
    scripts=['run_electrum_server', 'electrum-server'],
    install_requires=['plyvel', 'jsonrpclib', 'irc>=11'],
    package_dir={'electrumserver': 'src'},
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp',
        'electrumserver.stratum_http'
    ],
    description="VCoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum Lightweight VCoin Wallet""",
    maintainer="Graham Higgins",
    maintainer_email="gjh@bel-epa.com",
)
