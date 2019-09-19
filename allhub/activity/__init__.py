from .events import EventsMixin
from .feeds import FeedsMixin
from .notifications import NotificationsMixin
from .starring import StarringMixin
from .watching import WatchingMixin
from allhub.util import ConflictCheck


class ActivityMixin(
    EventsMixin,
    FeedsMixin,
    NotificationsMixin,
    StarringMixin,
    WatchingMixin,
    metaclass=ConflictCheck,
):
    pass
