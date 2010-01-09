from zope.interface import implements
from plone.cachepurging.interfaces import IPurgeEvent

class Purge(object):
    """Event implementation.
    
    To queue a purge for a given object, you can do::
    
        from plone.cachepurging import Purge
        from zope.event import notify
        
        notify(Purge(someobject))
    
    The actual URL(s) to purge are looked up via any relevant IPurgeURLs
    adapters.
    """
    
    implements(IPurgeEvent)
    
    def __init__(self, object):
        self.object = object
