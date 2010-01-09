import urlparse

from zope.interface import Interface, implements
from zope.component import adapts, getUtility

from plone.registry.interfaces import IRegistry

from plone.cachepurging.interfaces import IPurgePathRewriter
from plone.cachepurging.interfaces import ICachePurgingSettings

class DefaultRewriter(object):
    """Default rewriter, which is aware of virtual hosting
    """
    
    implements(IPurgePathRewriter)
    adapts(Interface)
    
    def __init__(self, request):
        self.request = request
    
    def __call__(self, path):
        request = self.request
        
        # No rewriting necessary
        virtualURL = request.get('VIRTUAL_URL', None)
        if virtualURL is None:
            return [path]
        
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICachePurgingSettings, check=False)
        
        virtualHosting = settings.virtualHosting
        
        # We don't want to rewrite
        if not virtualHosting:
            return [path]
        
        domains = settings.domains
        if not domains:
            domains = [request.get('SERVER_URL')]
        
        # We need to reconstruct VHM URLs for each of the domains
        virtualUrlParts = request.get('VIRTUAL_URL_PARTS')
        virtualRootPhysicalPath = request.get('VirtualRootPhysicalPath')

        # Make sure request is compliant
        if not virtualUrlParts or not virtualRootPhysicalPath \
            or len(virtualUrlParts) < 2 or len(virtualUrlParts) > 3:
            return [path]
        
        # Virtual root, e.g. /Plone. Clear if we don't have any virtual root
        virtualRoot = '/'.join(virtualRootPhysicalPath)
        if virtualRoot == '/':
            virtualRoot = ''
        
        # Prefix, e.g. /_vh_foo/_vh_bar. Clear if we don't have any.
        pathPrefix = len(virtualUrlParts) == 3 and virtualUrlParts[1] or ''
        if pathPrefix:
            pathPrefix = '/' + '/'.join(['_vh_%s' % p for p in pathPrefix.split('/')])
        
        # Path, e.g. /front-page
        pathPortion = '/' + virtualUrlParts[-1]
        
        paths = []
        for domain in domains:
            scheme, host = urlparse.urlparse(domain)[:2]
            paths.append(
                '/VirtualHostBase/%(scheme)s/%(host)s%(root)s/VirtualHostRoot%(prefix)s%(path)s' %
                    {'scheme':  scheme,
                     'host':    host,
                     'root':    virtualRoot,
                     'prefix':  pathPrefix,
                     'path':    pathPortion,
                    }
                )
        return paths
