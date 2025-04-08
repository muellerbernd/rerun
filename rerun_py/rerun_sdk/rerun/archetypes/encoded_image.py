# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/archetypes/encoded_image.fbs".

# You can extend this class by creating a "EncodedImageExt" class in "encoded_image_ext.py".

from __future__ import annotations

import numpy as np
import pyarrow as pa
from attrs import define, field

from .. import components, datatypes
from .._baseclasses import (
    Archetype,
    ComponentColumnList,
)
from ..error_utils import catch_and_log_exceptions
from .encoded_image_ext import EncodedImageExt

__all__ = ["EncodedImage"]


@define(str=False, repr=False, init=False)
class EncodedImage(EncodedImageExt, Archetype):
    """
    **Archetype**: An image encoded as e.g. a JPEG or PNG.

    Rerun also supports uncompressed images with the [`archetypes.Image`][rerun.archetypes.Image].
    For images that refer to video frames see [`archetypes.VideoFrameReference`][rerun.archetypes.VideoFrameReference].

    To compress an image, use [`rerun.Image.compress`][].

    Example
    -------
    ### `encoded_image`:
    ```python
    from pathlib import Path

    import rerun as rr

    image_file_path = Path(__file__).parent / "ferris.png"

    rr.init("rerun_example_encoded_image", spawn=True)

    rr.log("image", rr.EncodedImage(path=image_file_path))
    ```

    """

    # __init__ can be found in encoded_image_ext.py

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            blob=None,
            media_type=None,
            opacity=None,
            draw_order=None,
        )

    @classmethod
    def _clear(cls) -> EncodedImage:
        """Produce an empty EncodedImage, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    @classmethod
    def from_fields(
        cls,
        *,
        clear_unset: bool = False,
        blob: datatypes.BlobLike | None = None,
        media_type: datatypes.Utf8Like | None = None,
        opacity: datatypes.Float32Like | None = None,
        draw_order: datatypes.Float32Like | None = None,
    ) -> EncodedImage:
        """
        Update only some specific fields of a `EncodedImage`.

        Parameters
        ----------
        clear_unset:
            If true, all unspecified fields will be explicitly cleared.
        blob:
            The encoded content of some image file, e.g. a PNG or JPEG.
        media_type:
            The Media Type of the asset.

            Supported values:
            * `image/jpeg`
            * `image/png`

            If omitted, the viewer will try to guess from the data blob.
            If it cannot guess, it won't be able to render the asset.
        opacity:
            Opacity of the image, useful for layering several images.

            Defaults to 1.0 (fully opaque).
        draw_order:
            An optional floating point value that specifies the 2D drawing order.

            Objects with higher values are drawn on top of those with lower values.

        """

        inst = cls.__new__(cls)
        with catch_and_log_exceptions(context=cls.__name__):
            kwargs = {
                "blob": blob,
                "media_type": media_type,
                "opacity": opacity,
                "draw_order": draw_order,
            }

            if clear_unset:
                kwargs = {k: v if v is not None else [] for k, v in kwargs.items()}  # type: ignore[misc]

            inst.__attrs_init__(**kwargs)
            return inst

        inst.__attrs_clear__()
        return inst

    @classmethod
    def cleared(cls) -> EncodedImage:
        """Clear all the fields of a `EncodedImage`."""
        return cls.from_fields(clear_unset=True)

    @classmethod
    def columns(
        cls,
        *,
        blob: datatypes.BlobArrayLike | None = None,
        media_type: datatypes.Utf8ArrayLike | None = None,
        opacity: datatypes.Float32ArrayLike | None = None,
        draw_order: datatypes.Float32ArrayLike | None = None,
    ) -> ComponentColumnList:
        """
        Construct a new column-oriented component bundle.

        This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.

        The returned columns will be partitioned into unit-length sub-batches by default.
        Use `ComponentColumnList.partition` to repartition the data as needed.

        Parameters
        ----------
        blob:
            The encoded content of some image file, e.g. a PNG or JPEG.
        media_type:
            The Media Type of the asset.

            Supported values:
            * `image/jpeg`
            * `image/png`

            If omitted, the viewer will try to guess from the data blob.
            If it cannot guess, it won't be able to render the asset.
        opacity:
            Opacity of the image, useful for layering several images.

            Defaults to 1.0 (fully opaque).
        draw_order:
            An optional floating point value that specifies the 2D drawing order.

            Objects with higher values are drawn on top of those with lower values.

        """

        inst = cls.__new__(cls)
        with catch_and_log_exceptions(context=cls.__name__):
            inst.__attrs_init__(
                blob=blob,
                media_type=media_type,
                opacity=opacity,
                draw_order=draw_order,
            )

        batches = inst.as_component_batches(include_indicators=False)
        if len(batches) == 0:
            return ComponentColumnList([])

        kwargs = {"blob": blob, "media_type": media_type, "opacity": opacity, "draw_order": draw_order}
        columns = []

        for batch in batches:
            arrow_array = batch.as_arrow_array()

            # For primitive arrays and fixed size list arrays, we infer partition size from the input shape.
            if pa.types.is_primitive(arrow_array.type) or pa.types.is_fixed_size_list(arrow_array.type):
                param = kwargs[batch.component_descriptor().archetype_field_name]  # type: ignore[index]
                shape = np.shape(param)  # type: ignore[arg-type]

                if pa.types.is_fixed_size_list(arrow_array.type) and len(shape) <= 2:
                    # If shape length is 2 or less, we have `num_rows` single element batches (each element is a fixed sized list).
                    # `shape[1]` should be the length of the fixed sized list.
                    # (This should have been already validated by conversion to the arrow_array)
                    batch_length = 1
                else:
                    batch_length = shape[1] if len(shape) > 1 else 1  # type: ignore[redundant-expr,misc]

                num_rows = shape[0] if len(shape) >= 1 else 1  # type: ignore[redundant-expr,misc]
                sizes = batch_length * np.ones(num_rows)
            else:
                # For non-primitive types, default to partitioning each element separately.
                sizes = np.ones(len(arrow_array))

            columns.append(batch.partition(sizes))

        indicator_column = cls.indicator().partition(np.zeros(len(sizes)))
        return ComponentColumnList([indicator_column] + columns)

    blob: components.BlobBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.BlobBatch._converter,  # type: ignore[misc]
    )
    # The encoded content of some image file, e.g. a PNG or JPEG.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    media_type: components.MediaTypeBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.MediaTypeBatch._converter,  # type: ignore[misc]
    )
    # The Media Type of the asset.
    #
    # Supported values:
    # * `image/jpeg`
    # * `image/png`
    #
    # If omitted, the viewer will try to guess from the data blob.
    # If it cannot guess, it won't be able to render the asset.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    opacity: components.OpacityBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.OpacityBatch._converter,  # type: ignore[misc]
    )
    # Opacity of the image, useful for layering several images.
    #
    # Defaults to 1.0 (fully opaque).
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    draw_order: components.DrawOrderBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.DrawOrderBatch._converter,  # type: ignore[misc]
    )
    # An optional floating point value that specifies the 2D drawing order.
    #
    # Objects with higher values are drawn on top of those with lower values.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
