# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/datatypes/class_description.fbs".

# You can extend this class by creating a "ClassDescriptionExt" class in "class_description_ext.py".

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Union

import pyarrow as pa
from attrs import define, field

from .. import datatypes
from .._baseclasses import (
    BaseBatch,
)
from .class_description_ext import ClassDescriptionExt

__all__ = ["ClassDescription", "ClassDescriptionArrayLike", "ClassDescriptionBatch", "ClassDescriptionLike"]


@define(init=False)
class ClassDescription(ClassDescriptionExt):
    """
    **Datatype**: The description of a semantic Class.

    If an entity is annotated with a corresponding [`components.ClassId`][rerun.components.ClassId], Rerun will use
    the attached [`datatypes.AnnotationInfo`][rerun.datatypes.AnnotationInfo] to derive labels and colors.

    Keypoints within an annotation class can similarly be annotated with a
    [`components.KeypointId`][rerun.components.KeypointId] in which case we should defer to the label and color for the
    [`datatypes.AnnotationInfo`][rerun.datatypes.AnnotationInfo] specifically associated with the Keypoint.

    Keypoints within the class can also be decorated with skeletal edges.
    Keypoint-connections are pairs of [`components.KeypointId`][rerun.components.KeypointId]s. If an edge is
    defined, and both keypoints exist within the instance of the class, then the
    keypoints should be connected with an edge. The edge should be labeled and
    colored as described by the class's [`datatypes.AnnotationInfo`][rerun.datatypes.AnnotationInfo].

    Note that a `ClassDescription` can be directly logged using `rerun.log`.
    This is equivalent to logging a `rerun.AnnotationContext` containing
    a single `ClassDescription`.
    """

    # __init__ can be found in class_description_ext.py

    info: datatypes.AnnotationInfo = field(
        converter=ClassDescriptionExt.info__field_converter_override,  # type: ignore[misc]
    )
    # The [`datatypes.AnnotationInfo`][rerun.datatypes.AnnotationInfo] for the class.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    keypoint_annotations: list[datatypes.AnnotationInfo] = field(
        converter=ClassDescriptionExt.keypoint_annotations__field_converter_override,  # type: ignore[misc]
    )
    # The [`datatypes.AnnotationInfo`][rerun.datatypes.AnnotationInfo] for all of the keypoints.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    keypoint_connections: list[datatypes.KeypointPair] = field(
        converter=ClassDescriptionExt.keypoint_connections__field_converter_override,  # type: ignore[misc]
    )
    # The connections between keypoints.
    #
    # (Docstring intentionally commented out to hide this field from the docs)


if TYPE_CHECKING:
    ClassDescriptionLike = Union[ClassDescription, datatypes.AnnotationInfoLike]
else:
    ClassDescriptionLike = Any

ClassDescriptionArrayLike = Union[
    ClassDescription,
    Sequence[ClassDescriptionLike],
]


class ClassDescriptionBatch(BaseBatch[ClassDescriptionArrayLike]):
    _ARROW_DATATYPE = pa.struct([
        pa.field(
            "info",
            pa.struct([
                pa.field("id", pa.uint16(), nullable=False, metadata={}),
                pa.field("label", pa.utf8(), nullable=True, metadata={}),
                pa.field("color", pa.uint32(), nullable=True, metadata={}),
            ]),
            nullable=False,
            metadata={},
        ),
        pa.field(
            "keypoint_annotations",
            pa.list_(
                pa.field(
                    "item",
                    pa.struct([
                        pa.field("id", pa.uint16(), nullable=False, metadata={}),
                        pa.field("label", pa.utf8(), nullable=True, metadata={}),
                        pa.field("color", pa.uint32(), nullable=True, metadata={}),
                    ]),
                    nullable=False,
                    metadata={},
                )
            ),
            nullable=False,
            metadata={},
        ),
        pa.field(
            "keypoint_connections",
            pa.list_(
                pa.field(
                    "item",
                    pa.struct([
                        pa.field("keypoint0", pa.uint16(), nullable=False, metadata={}),
                        pa.field("keypoint1", pa.uint16(), nullable=False, metadata={}),
                    ]),
                    nullable=False,
                    metadata={},
                )
            ),
            nullable=False,
            metadata={},
        ),
    ])

    @staticmethod
    def _native_to_pa_array(data: ClassDescriptionArrayLike, data_type: pa.DataType) -> pa.Array:
        return ClassDescriptionExt.native_to_pa_array_override(data, data_type)
