__import__('pkg_resources').declare_namespace(__name__)
from pkg_resources import get_distribution
__version__ = get_distribution("telesign").version
