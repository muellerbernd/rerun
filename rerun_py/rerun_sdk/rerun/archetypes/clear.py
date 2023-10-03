# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/archetypes/clear.fbs".

# You can extend this class by creating a "ClearExt" class in "clear_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components
from .._baseclasses import Archetype
from .clear_ext import ClearExt

__all__ = ["Clear"]


@define(str=False, repr=False, init=False)
class Clear(ClearExt, Archetype):
    """
    **Archetype**: Empties all the components of an entity.

    Examples
    --------
    ### Flat:
    ```python

    import rerun as rr

    rr.init("rerun_example_clear_simple", spawn=True)

    vectors = [(1.0, 0.0, 0.0), (0.0, -1.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    origins = [(-0.5, 0.5, 0.0), (0.5, 0.5, 0.0), (0.5, -0.5, 0.0), (-0.5, -0.5, 0.0)]
    colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 0, 200)]

    # Log a handful of arrows.
    for i, (vector, origin, color) in enumerate(zip(vectors, origins, colors)):
        rr.log(f"arrows/{i}", rr.Arrows3D(vectors=vector, origins=origin, colors=color))

    # Now clear them, one by one on each tick.
    for i in range(len(vectors)):
        rr.log(f"arrows/{i}", rr.Clear(recursive=False))  # or `rr.Clear.flat()`
    ```

    ### Recursive:
    ```python

    import rerun as rr

    rr.init("rerun_example_clear_simple", spawn=True)

    vectors = [(1.0, 0.0, 0.0), (0.0, -1.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    origins = [(-0.5, 0.5, 0.0), (0.5, 0.5, 0.0), (0.5, -0.5, 0.0), (-0.5, -0.5, 0.0)]
    colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 0, 200)]

    # Log a handful of arrows.
    for i, (vector, origin, color) in enumerate(zip(vectors, origins, colors)):
        rr.log(f"arrows/{i}", rr.Arrows3D(vectors=vector, origins=origin, colors=color))

    # Now clear all of them at once.
    rr.log("arrows", rr.Clear(recursive=True))  # or `rr.Clear.recursive()`
    ```
    """

    # __init__ can be found in clear_ext.py

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            is_recursive=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> Clear:
        """Produce an empty Clear, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    is_recursive: components.ClearIsRecursiveBatch = field(
        metadata={"component": "required"},
        converter=components.ClearIsRecursiveBatch._required,  # type: ignore[misc]
    )
    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__
