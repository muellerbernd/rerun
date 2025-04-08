# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/blueprint/archetypes/container_blueprint.fbs".

# You can extend this class by creating a "ContainerBlueprintExt" class in "container_blueprint_ext.py".

from __future__ import annotations

from typing import Any

from attrs import define, field

from ... import components, datatypes
from ..._baseclasses import (
    Archetype,
)
from ...blueprint import components as blueprint_components
from ...error_utils import catch_and_log_exceptions

__all__ = ["ContainerBlueprint"]


@define(str=False, repr=False, init=False)
class ContainerBlueprint(Archetype):
    """
    **Archetype**: The description of a container.

    ⚠️ **This type is _unstable_ and may change significantly in a way that the data won't be backwards compatible.**
    """

    def __init__(
        self: Any,
        container_kind: blueprint_components.ContainerKindLike,
        *,
        display_name: datatypes.Utf8Like | None = None,
        contents: datatypes.EntityPathArrayLike | None = None,
        col_shares: datatypes.Float32ArrayLike | None = None,
        row_shares: datatypes.Float32ArrayLike | None = None,
        active_tab: datatypes.EntityPathLike | None = None,
        visible: datatypes.BoolLike | None = None,
        grid_columns: datatypes.UInt32Like | None = None,
    ) -> None:
        """
        Create a new instance of the ContainerBlueprint archetype.

        Parameters
        ----------
        container_kind:
            The class of the view.
        display_name:
            The name of the container.
        contents:
            `ContainerId`s or `ViewId`s that are children of this container.
        col_shares:
            The layout shares of each column in the container.

            For [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal] containers, the length of this list should always match the number of contents.

            Ignored for [`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers.
        row_shares:
            The layout shares of each row of the container.

            For [`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers, the length of this list should always match the number of contents.

            Ignored for [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal] containers.
        active_tab:
            Which tab is active.

            Only applies to `Tabs` containers.
        visible:
            Whether this container is visible.

            Defaults to true if not specified.
        grid_columns:
            How many columns this grid should have.

            If unset, the grid layout will be auto.

            Ignored for [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal]/[`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers.

        """

        # You can define your own __init__ function as a member of ContainerBlueprintExt in container_blueprint_ext.py
        with catch_and_log_exceptions(context=self.__class__.__name__):
            self.__attrs_init__(
                container_kind=container_kind,
                display_name=display_name,
                contents=contents,
                col_shares=col_shares,
                row_shares=row_shares,
                active_tab=active_tab,
                visible=visible,
                grid_columns=grid_columns,
            )
            return
        self.__attrs_clear__()

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            container_kind=None,
            display_name=None,
            contents=None,
            col_shares=None,
            row_shares=None,
            active_tab=None,
            visible=None,
            grid_columns=None,
        )

    @classmethod
    def _clear(cls) -> ContainerBlueprint:
        """Produce an empty ContainerBlueprint, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    @classmethod
    def from_fields(
        cls,
        *,
        clear_unset: bool = False,
        container_kind: blueprint_components.ContainerKindLike | None = None,
        display_name: datatypes.Utf8Like | None = None,
        contents: datatypes.EntityPathArrayLike | None = None,
        col_shares: datatypes.Float32ArrayLike | None = None,
        row_shares: datatypes.Float32ArrayLike | None = None,
        active_tab: datatypes.EntityPathLike | None = None,
        visible: datatypes.BoolLike | None = None,
        grid_columns: datatypes.UInt32Like | None = None,
    ) -> ContainerBlueprint:
        """
        Update only some specific fields of a `ContainerBlueprint`.

        Parameters
        ----------
        clear_unset:
            If true, all unspecified fields will be explicitly cleared.
        container_kind:
            The class of the view.
        display_name:
            The name of the container.
        contents:
            `ContainerId`s or `ViewId`s that are children of this container.
        col_shares:
            The layout shares of each column in the container.

            For [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal] containers, the length of this list should always match the number of contents.

            Ignored for [`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers.
        row_shares:
            The layout shares of each row of the container.

            For [`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers, the length of this list should always match the number of contents.

            Ignored for [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal] containers.
        active_tab:
            Which tab is active.

            Only applies to `Tabs` containers.
        visible:
            Whether this container is visible.

            Defaults to true if not specified.
        grid_columns:
            How many columns this grid should have.

            If unset, the grid layout will be auto.

            Ignored for [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal]/[`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers.

        """

        inst = cls.__new__(cls)
        with catch_and_log_exceptions(context=cls.__name__):
            kwargs = {
                "container_kind": container_kind,
                "display_name": display_name,
                "contents": contents,
                "col_shares": col_shares,
                "row_shares": row_shares,
                "active_tab": active_tab,
                "visible": visible,
                "grid_columns": grid_columns,
            }

            if clear_unset:
                kwargs = {k: v if v is not None else [] for k, v in kwargs.items()}  # type: ignore[misc]

            inst.__attrs_init__(**kwargs)
            return inst

        inst.__attrs_clear__()
        return inst

    @classmethod
    def cleared(cls) -> ContainerBlueprint:
        """Clear all the fields of a `ContainerBlueprint`."""
        return cls.from_fields(clear_unset=True)

    container_kind: blueprint_components.ContainerKindBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=blueprint_components.ContainerKindBatch._converter,  # type: ignore[misc]
    )
    # The class of the view.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    display_name: components.NameBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.NameBatch._converter,  # type: ignore[misc]
    )
    # The name of the container.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    contents: blueprint_components.IncludedContentBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=blueprint_components.IncludedContentBatch._converter,  # type: ignore[misc]
    )
    # `ContainerId`s or `ViewId`s that are children of this container.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    col_shares: blueprint_components.ColumnShareBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=blueprint_components.ColumnShareBatch._converter,  # type: ignore[misc]
    )
    # The layout shares of each column in the container.
    #
    # For [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal] containers, the length of this list should always match the number of contents.
    #
    # Ignored for [`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    row_shares: blueprint_components.RowShareBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=blueprint_components.RowShareBatch._converter,  # type: ignore[misc]
    )
    # The layout shares of each row of the container.
    #
    # For [`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers, the length of this list should always match the number of contents.
    #
    # Ignored for [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal] containers.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    active_tab: blueprint_components.ActiveTabBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=blueprint_components.ActiveTabBatch._converter,  # type: ignore[misc]
    )
    # Which tab is active.
    #
    # Only applies to `Tabs` containers.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    visible: components.VisibleBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.VisibleBatch._converter,  # type: ignore[misc]
    )
    # Whether this container is visible.
    #
    # Defaults to true if not specified.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    grid_columns: blueprint_components.GridColumnsBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=blueprint_components.GridColumnsBatch._converter,  # type: ignore[misc]
    )
    # How many columns this grid should have.
    #
    # If unset, the grid layout will be auto.
    #
    # Ignored for [`components.ContainerKind.Horizontal`][rerun.blueprint.components.ContainerKind.Horizontal]/[`components.ContainerKind.Vertical`][rerun.blueprint.components.ContainerKind.Vertical] containers.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
