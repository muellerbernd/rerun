// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/components/zoom_level.fbs".

#pragma once

#include "../../datatypes/float64.hpp"
#include "../../result.hpp"

#include <cstdint>
#include <memory>

namespace rerun::blueprint::components {
    /// **Component**: A zoom level determines how much of the world is visible on a map.
    struct ZoomLevel {
        /// Zoom level: 0 being the lowest zoom level (fully zoomed out) and 22 being the highest (fully zoomed in).
        rerun::datatypes::Float64 zoom;

      public:
        ZoomLevel() = default;

        ZoomLevel(rerun::datatypes::Float64 zoom_) : zoom(zoom_) {}

        ZoomLevel& operator=(rerun::datatypes::Float64 zoom_) {
            zoom = zoom_;
            return *this;
        }

        ZoomLevel(double value_) : zoom(value_) {}

        ZoomLevel& operator=(double value_) {
            zoom = value_;
            return *this;
        }

        /// Cast to the underlying Float64 datatype
        operator rerun::datatypes::Float64() const {
            return zoom;
        }
    };
} // namespace rerun::blueprint::components

namespace rerun {
    static_assert(sizeof(rerun::datatypes::Float64) == sizeof(blueprint::components::ZoomLevel));

    /// \private
    template <>
    struct Loggable<blueprint::components::ZoomLevel> {
        static constexpr const char Name[] = "rerun.blueprint.components.ZoomLevel";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::datatypes::Float64>::arrow_datatype();
        }

        /// Serializes an array of `rerun::blueprint:: components::ZoomLevel` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const blueprint::components::ZoomLevel* instances, size_t num_instances
        ) {
            if (num_instances == 0) {
                return Loggable<rerun::datatypes::Float64>::to_arrow(nullptr, 0);
            } else if (instances == nullptr) {
                return rerun::Error(
                    ErrorCode::UnexpectedNullArgument,
                    "Passed array instances is null when num_elements> 0."
                );
            } else {
                return Loggable<rerun::datatypes::Float64>::to_arrow(
                    &instances->zoom,
                    num_instances
                );
            }
        }
    };
} // namespace rerun
