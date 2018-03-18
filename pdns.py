
from apiobject.resource import Resource, CreatableResourceMixin, DeletableResourceMixin, UpdatableResourceMixin, base


Base = base()


class PdnsResource(Base):

    @classmethod
    def class_name(cls):
        return cls.__name__

    @classmethod
    def class_path(cls):
        return '/%ss' % cls.class_name().lower()


class Server(PdnsResource):
    pass


class Zone(CreatableResourceMixin, DeletableResourceMixin, UpdatableResourceMixin, PdnsResource):

    @classmethod
    def class_path(cls):
        return '/servers/localhost/zones'
