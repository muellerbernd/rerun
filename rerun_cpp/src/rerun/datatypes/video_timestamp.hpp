// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/datatypes/video_timestamp.fbs".

#pragma once

#include "../component_descriptor.hpp"
#include "../result.hpp"

#include <cstdint>
#include <memory>

namespace arrow {
    /// \private
    template <typename T>
    class NumericBuilder;

    class Array;
    class DataType;
    class Int64Type;
    using Int64Builder = NumericBuilder<Int64Type>;
} // namespace arrow

namespace rerun::datatypes {
    /// **Datatype**: Presentation timestamp within a `archetypes::AssetVideo`.
    ///
    /// Specified in nanoseconds.
    /// Presentation timestamps are typically measured as time since video start.
    struct VideoTimestamp {
        /// Presentation timestamp value in nanoseconds.
        int64_t timestamp_ns;

      public:
        VideoTimestamp() = default;

        VideoTimestamp(int64_t timestamp_ns_) : timestamp_ns(timestamp_ns_) {}

        VideoTimestamp& operator=(int64_t timestamp_ns_) {
            timestamp_ns = timestamp_ns_;
            return *this;
        }
    };
} // namespace rerun::datatypes

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<datatypes::VideoTimestamp> {
        static constexpr ComponentDescriptor Descriptor = "rerun.datatypes.VideoTimestamp";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Serializes an array of `rerun::datatypes::VideoTimestamp` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const datatypes::VideoTimestamp* instances, size_t num_instances
        );

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::Int64Builder* builder, const datatypes::VideoTimestamp* elements,
            size_t num_elements
        );
    };
} // namespace rerun
