from .events import EventsMixin
from .feeds import FeedsMixin
from .notifications import NotificationsMixin
from .starring import StarringMixin
from .watching import WatchingMixin


class ActivityMixin(
    EventsMixin, FeedsMixin, NotificationsMixin, StarringMixin, WatchingMixin
):
    pass
