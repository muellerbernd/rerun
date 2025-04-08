// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/rust/api.rs
// Based on "crates/store/re_types/definitions/rerun/archetypes/scalars.fbs".

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

/// **Archetype**: One or more double-precision scalar values, e.g. for use for time-series plots.
///
/// The current timeline value will be used for the time/X-axis, hence scalars
/// should not be static.
/// Number of scalars per timestamp is expected to be the same over time.
///
/// When used to produce a plot, this archetype is used to provide the data that
/// is referenced by [`archetypes::SeriesLines`][crate::archetypes::SeriesLines] or [`archetypes::SeriesPoints`][crate::archetypes::SeriesPoints]. You can do
/// this by logging both archetypes to the same path, or alternatively configuring
/// the plot-specific archetypes through the blueprint.
///
/// ## Examples
///
/// ### Update a scalar over time
/// ```ignore
/// fn main() -> Result<(), Box<dyn std::error::Error>> {
///     let rec = rerun::RecordingStreamBuilder::new("rerun_example_scalar_row_updates").spawn()?;
///
///     for step in 0..64 {
///         rec.set_time_sequence("step", step);
///         rec.log(
///             "scalars",
///             &rerun::Scalars::single((step as f64 / 10.0).sin()),
///         )?;
///     }
///
///     Ok(())
/// }
/// ```
/// <center>
/// <picture>
///   <source media="(max-width: 480px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/480w.png">
///   <source media="(max-width: 768px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/768w.png">
///   <source media="(max-width: 1024px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/1024w.png">
///   <source media="(max-width: 1200px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/1200w.png">
///   <img src="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/full.png" width="640">
/// </picture>
/// </center>
///
/// ### Update a scalar over time, in a single operation
/// ```ignore
/// use rerun::TimeColumn;
///
/// fn main() -> Result<(), Box<dyn std::error::Error>> {
///     let rec = rerun::RecordingStreamBuilder::new("rerun_example_scalar_column_updates").spawn()?;
///
///     let times = TimeColumn::new_sequence("step", 0..64);
///     let scalars = (0..64).map(|step| (step as f64 / 10.0).sin());
///
///     rec.send_columns(
///         "scalars",
///         [times],
///         rerun::Scalars::new(scalars).columns_of_unit_batches()?,
///     )?;
///
///     Ok(())
/// }
/// ```
/// <center>
/// <picture>
///   <source media="(max-width: 480px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/480w.png">
///   <source media="(max-width: 768px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/768w.png">
///   <source media="(max-width: 1024px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/1024w.png">
///   <source media="(max-width: 1200px)" srcset="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/1200w.png">
///   <img src="https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/full.png" width="640">
/// </picture>
/// </center>
#[derive(Clone, Debug, PartialEq, Default)]
pub struct Scalars {
    /// The scalar values to log.
    pub scalars: Option<SerializedComponentBatch>,
}

impl Scalars {
    /// Returns the [`ComponentDescriptor`] for [`Self::scalars`].
    #[inline]
    pub fn descriptor_scalars() -> ComponentDescriptor {
        ComponentDescriptor {
            archetype_name: Some("rerun.archetypes.Scalars".into()),
            component_name: "rerun.components.Scalar".into(),
            archetype_field_name: Some("scalars".into()),
        }
    }

    /// Returns the [`ComponentDescriptor`] for the associated indicator component.
    #[inline]
    pub fn descriptor_indicator() -> ComponentDescriptor {
        ComponentDescriptor {
            archetype_name: Some("rerun.archetypes.Scalars".into()),
            component_name: "rerun.components.ScalarsIndicator".into(),
            archetype_field_name: None,
        }
    }
}

static REQUIRED_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 1usize]> =
    once_cell::sync::Lazy::new(|| [Scalars::descriptor_scalars()]);

static RECOMMENDED_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 1usize]> =
    once_cell::sync::Lazy::new(|| [Scalars::descriptor_indicator()]);

static OPTIONAL_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 0usize]> =
    once_cell::sync::Lazy::new(|| []);

static ALL_COMPONENTS: once_cell::sync::Lazy<[ComponentDescriptor; 2usize]> =
    once_cell::sync::Lazy::new(|| {
        [
            Scalars::descriptor_scalars(),
            Scalars::descriptor_indicator(),
        ]
    });

impl Scalars {
    /// The total number of components in the archetype: 1 required, 1 recommended, 0 optional
    pub const NUM_COMPONENTS: usize = 2usize;
}

/// Indicator component for the [`Scalars`] [`::re_types_core::Archetype`]
pub type ScalarsIndicator = ::re_types_core::GenericIndicatorComponent<Scalars>;

impl ::re_types_core::Archetype for Scalars {
    type Indicator = ScalarsIndicator;

    #[inline]
    fn name() -> ::re_types_core::ArchetypeName {
        "rerun.archetypes.Scalars".into()
    }

    #[inline]
    fn display_name() -> &'static str {
        "Scalars"
    }

    #[inline]
    fn indicator() -> SerializedComponentBatch {
        #[allow(clippy::unwrap_used)]
        ScalarsIndicator::DEFAULT.serialized().unwrap()
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
        let scalars = arrays_by_descr
            .get(&Self::descriptor_scalars())
            .map(|array| SerializedComponentBatch::new(array.clone(), Self::descriptor_scalars()));
        Ok(Self { scalars })
    }
}

impl ::re_types_core::AsComponents for Scalars {
    #[inline]
    fn as_serialized_batches(&self) -> Vec<SerializedComponentBatch> {
        use ::re_types_core::Archetype as _;
        [Some(Self::indicator()), self.scalars.clone()]
            .into_iter()
            .flatten()
            .collect()
    }
}

impl ::re_types_core::ArchetypeReflectionMarker for Scalars {}

impl Scalars {
    /// Create a new `Scalars`.
    #[inline]
    pub fn new(scalars: impl IntoIterator<Item = impl Into<crate::components::Scalar>>) -> Self {
        Self {
            scalars: try_serialize_field(Self::descriptor_scalars(), scalars),
        }
    }

    /// Update only some specific fields of a `Scalars`.
    #[inline]
    pub fn update_fields() -> Self {
        Self::default()
    }

    /// Clear all the fields of a `Scalars`.
    #[inline]
    pub fn clear_fields() -> Self {
        use ::re_types_core::Loggable as _;
        Self {
            scalars: Some(SerializedComponentBatch::new(
                crate::components::Scalar::arrow_empty(),
                Self::descriptor_scalars(),
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
        let columns = [self
            .scalars
            .map(|scalars| scalars.partitioned(_lengths.clone()))
            .transpose()?];
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
        let len_scalars = self.scalars.as_ref().map(|b| b.array.len());
        let len = None.or(len_scalars).unwrap_or(0);
        self.columns(std::iter::repeat(1).take(len))
    }

    /// The scalar values to log.
    #[inline]
    pub fn with_scalars(
        mut self,
        scalars: impl IntoIterator<Item = impl Into<crate::components::Scalar>>,
    ) -> Self {
        self.scalars = try_serialize_field(Self::descriptor_scalars(), scalars);
        self
    }
}

impl ::re_byte_size::SizeBytes for Scalars {
    #[inline]
    fn heap_size_bytes(&self) -> u64 {
        self.scalars.heap_size_bytes()
    }
}
