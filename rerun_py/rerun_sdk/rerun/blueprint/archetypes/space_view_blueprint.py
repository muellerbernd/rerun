# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/blueprint/archetypes/space_view_blueprint.fbs".

# You can extend this class by creating a "SpaceViewBlueprintExt" class in "space_view_blueprint_ext.py".

from __future__ import annotations

from typing import Any

from attrs import define, field

from ... import blueprint, datatypes
from ..._baseclasses import Archetype
from ...error_utils import catch_and_log_exceptions

__all__ = ["SpaceViewBlueprint"]


@define(str=False, repr=False, init=False)
class SpaceViewBlueprint(Archetype):
    """**Archetype**: The top-level description of the Viewport."""

    def __init__(
        self: Any,
        class_identifier: blueprint.components.SpaceViewClassLike,
        *,
        display_name: blueprint.components.NameLike | None = None,
        space_origin: datatypes.EntityPathLike | None = None,
        entities_determined_by_user: blueprint.components.EntitiesDeterminedByUserLike | None = None,
        contents: blueprint.components.IncludedQueriesLike | None = None,
        visible: blueprint.components.VisibleLike | None = None,
    ):
        """
        Create a new instance of the SpaceViewBlueprint archetype.

        Parameters
        ----------
        class_identifier:
            The class of the view.
        display_name:
            The name of the view.
        space_origin:
            The "anchor point" of this space view.

            The transform at this path forms the reference point for all scene->world transforms in this space view.
            I.e. the position of this entity path in space forms the origin of the coordinate system in this space view.
            Furthermore, this is the primary indicator for heuristics on what entities we show in this space view.
        entities_determined_by_user:
            True if the user is has added entities themselves. False otherwise.
        contents:
            `BlueprintId`s of the `DataQuery`s that make up this `SpaceView`.

            It determines which entities are part of the spaceview.
        visible:
            Whether this space view is visible.

            Defaults to true if not specified.
        """

        # You can define your own __init__ function as a member of SpaceViewBlueprintExt in space_view_blueprint_ext.py
        with catch_and_log_exceptions(context=self.__class__.__name__):
            self.__attrs_init__(
                class_identifier=class_identifier,
                display_name=display_name,
                space_origin=space_origin,
                entities_determined_by_user=entities_determined_by_user,
                contents=contents,
                visible=visible,
            )
            return
        self.__attrs_clear__()

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            class_identifier=None,  # type: ignore[arg-type]
            display_name=None,  # type: ignore[arg-type]
            space_origin=None,  # type: ignore[arg-type]
            entities_determined_by_user=None,  # type: ignore[arg-type]
            contents=None,  # type: ignore[arg-type]
            visible=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> SpaceViewBlueprint:
        """Produce an empty SpaceViewBlueprint, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    class_identifier: blueprint.components.SpaceViewClassBatch = field(
        metadata={"component": "required"},
        converter=blueprint.components.SpaceViewClassBatch._required,  # type: ignore[misc]
    )
    # The class of the view.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    display_name: blueprint.components.NameBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.NameBatch._optional,  # type: ignore[misc]
    )
    # The name of the view.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    space_origin: blueprint.components.SpaceViewOriginBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.SpaceViewOriginBatch._optional,  # type: ignore[misc]
    )
    # The "anchor point" of this space view.
    #
    # The transform at this path forms the reference point for all scene->world transforms in this space view.
    # I.e. the position of this entity path in space forms the origin of the coordinate system in this space view.
    # Furthermore, this is the primary indicator for heuristics on what entities we show in this space view.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    entities_determined_by_user: blueprint.components.EntitiesDeterminedByUserBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.EntitiesDeterminedByUserBatch._optional,  # type: ignore[misc]
    )
    # True if the user is has added entities themselves. False otherwise.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    contents: blueprint.components.IncludedQueriesBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.IncludedQueriesBatch._optional,  # type: ignore[misc]
    )
    # `BlueprintId`s of the `DataQuery`s that make up this `SpaceView`.
    #
    # It determines which entities are part of the spaceview.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    visible: blueprint.components.VisibleBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.VisibleBatch._optional,  # type: ignore[misc]
    )
    # Whether this space view is visible.
    #
    # Defaults to true if not specified.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__
