
import abc

class GameObject(metaclass=abc.ABCMeta):

    

    @abc.abstractproperty
    def sprite(self):
        pass

    @abc.abstractproperty
    def sprite_image(self):
        pass

    @abc.abstractclassmethod
    def update(self, dt):
        pass

    @abc.abstractclassmethod
    def onCollision(self, other):
        pass
