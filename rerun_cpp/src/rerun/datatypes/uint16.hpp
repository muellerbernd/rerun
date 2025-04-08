// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/datatypes/uint16.fbs".

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
    class UInt16Type;
    using UInt16Builder = NumericBuilder<UInt16Type>;
} // namespace arrow

namespace rerun::datatypes {
    /// **Datatype**: A 16bit unsigned integer.
    struct UInt16 {
        uint16_t value;

      public:
        UInt16() = default;

        UInt16(uint16_t value_) : value(value_) {}

        UInt16& operator=(uint16_t value_) {
            value = value_;
            return *this;
        }
    };
} // namespace rerun::datatypes

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<datatypes::UInt16> {
        static constexpr ComponentDescriptor Descriptor = "rerun.datatypes.UInt16";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Serializes an array of `rerun::datatypes::UInt16` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const datatypes::UInt16* instances, size_t num_instances
        );

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::UInt16Builder* builder, const datatypes::UInt16* elements, size_t num_elements
        );
    };
} // namespace rerun
