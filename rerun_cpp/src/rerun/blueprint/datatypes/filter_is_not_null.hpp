// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/datatypes/filter_is_not_null.fbs".

#pragma once

#include "../../component_descriptor.hpp"
#include "../../datatypes/bool.hpp"
#include "../../result.hpp"
#include "component_column_selector.hpp"

#include <cstdint>
#include <memory>

namespace arrow {
    class Array;
    class DataType;
    class StructBuilder;
} // namespace arrow

namespace rerun::blueprint::datatypes {
    /// **Datatype**: Configuration for the filter is not null feature of the dataframe view.
    ///
    /// ⚠ **This type is _unstable_ and may change significantly in a way that the data won't be backwards compatible.**
    ///
    struct FilterIsNotNull {
        /// Whether the filter by event feature is active.
        rerun::datatypes::Bool active;

        /// The column used when the filter by event feature is used.
        rerun::blueprint::datatypes::ComponentColumnSelector column;

      public:
        FilterIsNotNull() = default;
    };
} // namespace rerun::blueprint::datatypes

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<blueprint::datatypes::FilterIsNotNull> {
        static constexpr ComponentDescriptor Descriptor =
            "rerun.blueprint.datatypes.FilterIsNotNull";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Serializes an array of `rerun::blueprint:: datatypes::FilterIsNotNull` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const blueprint::datatypes::FilterIsNotNull* instances, size_t num_instances
        );

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::StructBuilder* builder, const blueprint::datatypes::FilterIsNotNull* elements,
            size_t num_elements
        );
    };
} // namespace rerun
