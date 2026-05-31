#!/usr/bin/env python3
"""Module that defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin that provides swim ability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides fly ability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")