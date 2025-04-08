// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/rust/api.rs
// Based on "crates/store/re_types/definitions/rerun/archetypes/recording_properties.fbs".

#![allow(unused_imports)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]
#![allow(clippy::cloned_instead_of_copied)]
#![allow(clippy::map_flatten)]
#![allow(clippy::needless_question_mark)]
#![allow(clippy::new_without_default)]
#![allow(clippy::redundant_closure)]
#![allow(clippy::too_many_arguments)]
#![allow(clippy::too_many_lines)]

use ::re_types_core::try_serialize_field;
use ::re_types_core::SerializationResult;
use ::re_types_core::{ComponentBatch as _, SerializedComponentBatch};
use ::re_types_core::{ComponentDescriptor, ComponentName};
use ::re_types_core::{DeserializationError, DeserializationResult};

/// **Archetype**: A list of properties associated with a recording.
#[derive(Clone, Debug, Default)]
pub struct RecordingProperties {
    /// When the recording started.
    ///
    /// Should be an absolute time, i.e. relative to Unix Epoch.
    pub start_time: Option<SerializedComponentBatch>,

    /// A user-chosen name for the recording.
    pub name: Option<SerializedComponentBatch>,
}

impl RecordingProperties {
    /// Returns the [`ComponentDescriptor`] for [`Self::start_time`].
    #[inline]
    pub fn descriptor_start_time() -> ComponentDescriptor {
        ComponentDescriptor {
            archetype_name: Some("rerun.archetypes.RecordingProperties".into()),
            component_name: "rerun.components.Timestamp".into(),
            archetype_field_name: Some("start_time".into()),
        }
    }

    /// Returns the [`ComponentDescriptor`] for [`Self::name`].
    #[inline]
    pub fn descriptor_name() -> ComponentDescriptor {
        ComponentDescriptor {
            archetype_name: Some("rerun.archetypes.RecordingProperties".into()),
            component_name: "rerun.components.Name".into(),
            archetype_field_name: Some("name".into()),
        }
    }

    /// Returns the [`ComponentDescriptor`] for the associated indicator component.
    #[inline]
    pub fn descriptor_indicator() -> ComponentDescriptor {
        ComponentDescriptor {
            archetype_name: Some("rerun.archetypes.RecordingProperties".into()),
            component_name: "rerun.components.RecordingPropertiesIndicator".into(),
            archetype_field_name: None,
        }
    }
}

static REQUIRED_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 0usize]> =
    once_cell::sync::Lazy::new(|| []);

static RECOMMENDED_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 1usize]> =
    once_cell::sync::Lazy::new(|| [RecordingProperties::descriptor_indicator()]);

static OPTIONAL_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 2usize]> =
    once_cell::sync::Lazy::new(|| {
        [
            RecordingProperties::descriptor_start_time(),
            RecordingProperties::descriptor_name(),
        ]
    });

static ALL_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 3usize]> =
    once_cell::sync::Lazy::new(|| {
        [
            RecordingProperties::descriptor_indicator(),
            RecordingProperties::descriptor_start_time(),
            RecordingProperties::descriptor_name(),
        ]
    });

impl RecordingProperties {
    /// The total number of components in the archetype: 0 required, 1 recommended, 2 optional
    pub const NUM_COMPONENTS: usize = 3usize;
}

/// Indicator component for the [`RecordingProperties`] [`::re_types_core::Archetype`]
pub type RecordingPropertiesIndicator =
    ::re_types_core::GenericIndicatorComponent<RecordingProperties>;

impl ::re_types_core::Archetype for RecordingProperties {
    type Indicator = RecordingPropertiesIndicator;

    #[inline]
    fn name() -> ::re_types_core::ArchetypeName {
        "rerun.archetypes.RecordingProperties".into()
    }

    #[inline]
    fn display_name() -> &'static str {
        "Recording properties"
    }

    #[inline]
    fn indicator() -> SerializedComponentBatch {
        #[allow(clippy::unwrap_used)]
        RecordingPropertiesIndicator::DEFAULT.serialized().unwrap()
    }

    #[inline]
    fn required_components() -> ::std::borrow::Cow<'static, [ComponentDescriptor]> {
        REQUIRED_COMPONENTS.as_slice().into()
    }

    #[inline]
    fn recommended_components() -> ::std::borrow::Cow<'static, [ComponentDescriptor]> {
        RECOMMENDED_COMPONENTS.as_slice().into()
    }

    #[inline]
    fn optional_components() -> ::std::borrow::Cow<'static, [ComponentDescriptor]> {
        OPTIONAL_COMPONENTS.as_slice().into()
    }

    #[inline]
    fn all_components() -> ::std::borrow::Cow<'static, [ComponentDescriptor]> {
        ALL_COMPONENTS.as_slice().into()
    }

    #[inline]
    fn from_arrow_components(
        arrow_data: impl IntoIterator<Item = (ComponentDescriptor, arrow::array::ArrayRef)>,
    ) -> DeserializationResult<Self> {
        re_tracing::profile_function!();
        use ::re_types_core::{Loggable as _, ResultExt as _};
        let arrays_by_descr: ::nohash_hasher::IntMap<_, _> = arrow_data.into_iter().collect();
        let start_time = arrays_by_descr
            .get(&Self::descriptor_start_time())
            .map(|array| {
                SerializedComponentBatch::new(array.clone(), Self::descriptor_start_time())
            });
        let name = arrays_by_descr
            .get(&Self::descriptor_name())
            .map(|array| SerializedComponentBatch::new(array.clone(), Self::descriptor_name()));
        Ok(Self { start_time, name })
    }
}

impl ::re_types_core::AsComponents for RecordingProperties {
    #[inline]
    fn as_serialized_batches(&self) -> Vec<SerializedComponentBatch> {
        use ::re_types_core::Archetype as _;
        [
            Some(Self::indicator()),
            self.start_time.clone(),
            self.name.clone(),
        ]
        .into_iter()
        .flatten()
        .collect()
    }
}

impl ::re_types_core::ArchetypeReflectionMarker for RecordingProperties {}

impl RecordingProperties {
    /// Create a new `RecordingProperties`.
    #[inline]
    pub fn new() -> Self {
        Self {
            start_time: None,
            name: None,
        }
    }

    /// Update only some specific fields of a `RecordingProperties`.
    #[inline]
    pub fn update_fields() -> Self {
        Self::default()
    }

    /// Clear all the fields of a `RecordingProperties`.
    #[inline]
    pub fn clear_fields() -> Self {
        use ::re_types_core::Loggable as _;
        Self {
            start_time: Some(SerializedComponentBatch::new(
                crate::components::Timestamp::arrow_empty(),
                Self::descriptor_start_time(),
            )),
            name: Some(SerializedComponentBatch::new(
                crate::components::Name::arrow_empty(),
                Self::descriptor_name(),
            )),
        }
    }

    /// Partitions the component data into multiple sub-batches.
    ///
    /// Specifically, this transforms the existing [`SerializedComponentBatch`]es data into [`SerializedComponentColumn`]s
    /// instead, via [`SerializedComponentBatch::partitioned`].
    ///
    /// This makes it possible to use `RecordingStream::send_columns` to send columnar data directly into Rerun.
    ///
    /// The specified `lengths` must sum to the total length of the component batch.
    ///
    /// [`SerializedComponentColumn`]: [::re_types_core::SerializedComponentColumn]
    #[inline]
    pub fn columns<I>(
        self,
        _lengths: I,
    ) -> SerializationResult<impl Iterator<Item = ::re_types_core::SerializedComponentColumn>>
    where
        I: IntoIterator<Item = usize> + Clone,
    {
        let columns = [
            self.start_time
                .map(|start_time| start_time.partitioned(_lengths.clone()))
                .transpose()?,
            self.name
                .map(|name| name.partitioned(_lengths.clone()))
                .transpose()?,
        ];
        Ok(columns
            .into_iter()
            .flatten()
            .chain([::re_types_core::indicator_column::<Self>(
                _lengths.into_iter().count(),
            )?]))
    }

    /// Helper to partition the component data into unit-length sub-batches.
    ///
    /// This is semantically similar to calling [`Self::columns`] with `std::iter::take(1).repeat(n)`,
    /// where `n` is automatically guessed.
    #[inline]
    pub fn columns_of_unit_batches(
        self,
    ) -> SerializationResult<impl Iterator<Item = ::re_types_core::SerializedComponentColumn>> {
        let len_start_time = self.start_time.as_ref().map(|b| b.array.len());
        let len_name = self.name.as_ref().map(|b| b.array.len());
        let len = None.or(len_start_time).or(len_name).unwrap_or(0);
        self.columns(std::iter::repeat(1).take(len))
    }

    /// When the recording started.
    ///
    /// Should be an absolute time, i.e. relative to Unix Epoch.
    #[inline]
    pub fn with_start_time(mut self, start_time: impl Into<crate::components::Timestamp>) -> Self {
        self.start_time = try_serialize_field(Self::descriptor_start_time(), [start_time]);
        self
    }

    /// This method makes it possible to pack multiple [`crate::components::Timestamp`] in a single component batch.
    ///
    /// This only makes sense when used in conjunction with [`Self::columns`]. [`Self::with_start_time`] should
    /// be used when logging a single row's worth of data.
    #[inline]
    pub fn with_many_start_time(
        mut self,
        start_time: impl IntoIterator<Item = impl Into<crate::components::Timestamp>>,
    ) -> Self {
        self.start_time = try_serialize_field(Self::descriptor_start_time(), start_time);
        self
    }

    /// A user-chosen name for the recording.
    #[inline]
    pub fn with_name(mut self, name: impl Into<crate::components::Name>) -> Self {
        self.name = try_serialize_field(Self::descriptor_name(), [name]);
        self
    }

    /// This method makes it possible to pack multiple [`crate::components::Name`] in a single component batch.
    ///
    /// This only makes sense when used in conjunction with [`Self::columns`]. [`Self::with_name`] should
    /// be used when logging a single row's worth of data.
    #[inline]
    pub fn with_many_name(
        mut self,
        name: impl IntoIterator<Item = impl Into<crate::components::Name>>,
    ) -> Self {
        self.name = try_serialize_field(Self::descriptor_name(), name);
        self
    }
}

impl ::re_byte_size::SizeBytes for RecordingProperties {
    #[inline]
    fn heap_size_bytes(&self) -> u64 {
        self.start_time.heap_size_bytes() + self.name.heap_size_bytes()
    }
}
