// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/components/view_origin.fbs".

#pragma once

#include "../../component_descriptor.hpp"
#include "../../datatypes/entity_path.hpp"
#include "../../result.hpp"

#include <cstdint>
#include <memory>
#include <string>
#include <utility>

namespace rerun::blueprint::components {
    /// **Component**: The origin of a view.
    ///
    /// ⚠ **This type is _unstable_ and may change significantly in a way that the data won't be backwards compatible.**
    ///
    struct ViewOrigin {
        rerun::datatypes::EntityPath value;

      public:
        ViewOrigin() = default;

        ViewOrigin(rerun::datatypes::EntityPath value_) : value(std::move(value_)) {}

        ViewOrigin& operator=(rerun::datatypes::EntityPath value_) {
            value = std::move(value_);
            return *this;
        }

        ViewOrigin(std::string path_) : value(std::move(path_)) {}

        ViewOrigin& operator=(std::string path_) {
            value = std::move(path_);
            return *this;
        }

        /// Cast to the underlying EntityPath datatype
        operator rerun::datatypes::EntityPath() const {
            return value;
        }
    };
} // namespace rerun::blueprint::components

namespace rerun {
    static_assert(
        sizeof(rerun::datatypes::EntityPath) == sizeof(blueprint::components::ViewOrigin)
    );

    /// \private
    template <>
    struct Loggable<blueprint::components::ViewOrigin> {
        static constexpr ComponentDescriptor Descriptor = "rerun.blueprint.components.ViewOrigin";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::datatypes::EntityPath>::arrow_datatype();
        }

        /// Serializes an array of `rerun::blueprint:: components::ViewOrigin` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const blueprint::components::ViewOrigin* instances, size_t num_instances
        ) {
            if (num_instances == 0) {
                return Loggable<rerun::datatypes::EntityPath>::to_arrow(nullptr, 0);
            } else if (instances == nullptr) {
                return rerun::Error(
                    ErrorCode::UnexpectedNullArgument,
                    "Passed array instances is null when num_elements> 0."
                );
            } else {
                return Loggable<rerun::datatypes::EntityPath>::to_arrow(
                    &instances->value,
                    num_instances
                );
            }
        }
    };
} // namespace rerun
