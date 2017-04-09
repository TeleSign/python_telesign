from pkg_resources import get_distribution

__import__('pkg_resources').declare_namespace(__name__)

__version__ = get_distribution("telesign").version
__author__ = "TeleSign"
__copyright__ = "Copyright 2017, TeleSign Corp."
__credits__ = ["TeleSign"]
__license__ = "MIT"
__maintainer__ = "TeleSign Corp."
__email__ = "support@telesign.com"
__status__ = "Production"
