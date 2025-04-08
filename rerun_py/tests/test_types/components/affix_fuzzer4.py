# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/testing/components/fuzzy.fbs".

# You can extend this class by creating a "AffixFuzzer4Ext" class in "affix_fuzzer4_ext.py".

from __future__ import annotations

from rerun._baseclasses import (
    ComponentBatchMixin,
    ComponentDescriptor,
    ComponentMixin,
)

from .. import datatypes

__all__ = ["AffixFuzzer4", "AffixFuzzer4Batch"]


class AffixFuzzer4(datatypes.AffixFuzzer1, ComponentMixin):
    _BATCH_TYPE = None
    # You can define your own __init__ function as a member of AffixFuzzer4Ext in affix_fuzzer4_ext.py

    # Note: there are no fields here because AffixFuzzer4 delegates to datatypes.AffixFuzzer1


class AffixFuzzer4Batch(datatypes.AffixFuzzer1Batch, ComponentBatchMixin):
    _COMPONENT_DESCRIPTOR: ComponentDescriptor = ComponentDescriptor("rerun.testing.components.AffixFuzzer4")


# This is patched in late to avoid circular dependencies.
AffixFuzzer4._BATCH_TYPE = AffixFuzzer4Batch  # type: ignore[assignment]
