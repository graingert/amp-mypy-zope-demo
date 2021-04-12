from typing import Optional

from zope.interface import Interface, implementer


class Responder:
    pass


class IResponderLocator(Interface):
    def locateResponder(name: bytes) -> Optional[Responder]:
        ...


@implementer(IResponderLocator)
class CommandLocator:
    def locateResponder(self, name: bytes) -> Optional[Responder]:
        return None


@implementer(IResponderLocator)
class SimpleStringLocator:
    def locateResponder(self, name: bytes) -> Optional[Responder]:
        return None


class AMP(CommandLocator, SimpleStringLocator):
    def locatorResponder(self, name: bytes) -> Optional[Responder]:
        v = CommandLocator.locatorResponder(self, name)  # type: ignore[attr-defined]
        if v is None:
            return SimpleStringLocator.locatorResponder(self, name)  # type: ignore[attr-defined, no-any-return]
        return v  # type: ignore[no-any-return]
