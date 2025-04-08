// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/archetypes/pinhole.fbs".

#include "pinhole.hpp"

#include "../collection_adapter_builtins.hpp"

namespace rerun::archetypes {
    Pinhole Pinhole::clear_fields() {
        auto archetype = Pinhole();
        archetype.image_from_camera =
            ComponentBatch::empty<rerun::components::PinholeProjection>(Descriptor_image_from_camera
            )
                .value_or_throw();
        archetype.resolution =
            ComponentBatch::empty<rerun::components::Resolution>(Descriptor_resolution)
                .value_or_throw();
        archetype.camera_xyz =
            ComponentBatch::empty<rerun::components::ViewCoordinates>(Descriptor_camera_xyz)
                .value_or_throw();
        archetype.image_plane_distance =
            ComponentBatch::empty<rerun::components::ImagePlaneDistance>(
                Descriptor_image_plane_distance
            )
                .value_or_throw();
        return archetype;
    }

    Collection<ComponentColumn> Pinhole::columns(const Collection<uint32_t>& lengths_) {
        std::vector<ComponentColumn> columns;
        columns.reserve(5);
        if (image_from_camera.has_value()) {
            columns.push_back(image_from_camera.value().partitioned(lengths_).value_or_throw());
        }
        if (resolution.has_value()) {
            columns.push_back(resolution.value().partitioned(lengths_).value_or_throw());
        }
        if (camera_xyz.has_value()) {
            columns.push_back(camera_xyz.value().partitioned(lengths_).value_or_throw());
        }
        if (image_plane_distance.has_value()) {
            columns.push_back(image_plane_distance.value().partitioned(lengths_).value_or_throw());
        }
        columns.push_back(
            ComponentColumn::from_indicators<Pinhole>(static_cast<uint32_t>(lengths_.size()))
                .value_or_throw()
        );
        return columns;
    }

    Collection<ComponentColumn> Pinhole::columns() {
        if (image_from_camera.has_value()) {
            return columns(std::vector<uint32_t>(image_from_camera.value().length(), 1));
        }
        if (resolution.has_value()) {
            return columns(std::vector<uint32_t>(resolution.value().length(), 1));
        }
        if (camera_xyz.has_value()) {
            return columns(std::vector<uint32_t>(camera_xyz.value().length(), 1));
        }
        if (image_plane_distance.has_value()) {
            return columns(std::vector<uint32_t>(image_plane_distance.value().length(), 1));
        }
        return Collection<ComponentColumn>();
    }
} // namespace rerun::archetypes

namespace rerun {

    Result<Collection<ComponentBatch>> AsComponents<archetypes::Pinhole>::as_batches(
        const archetypes::Pinhole& archetype
    ) {
        using namespace archetypes;
        std::vector<ComponentBatch> cells;
        cells.reserve(5);

        if (archetype.image_from_camera.has_value()) {
            cells.push_back(archetype.image_from_camera.value());
        }
        if (archetype.resolution.has_value()) {
            cells.push_back(archetype.resolution.value());
        }
        if (archetype.camera_xyz.has_value()) {
            cells.push_back(archetype.camera_xyz.value());
        }
        if (archetype.image_plane_distance.has_value()) {
            cells.push_back(archetype.image_plane_distance.value());
        }
        {
            auto result = ComponentBatch::from_indicator<Pinhole>();
            RR_RETURN_NOT_OK(result.error);
            cells.emplace_back(std::move(result.value));
        }

        return rerun::take_ownership(std::move(cells));
    }
} // namespace rerun
