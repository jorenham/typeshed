"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DeploymentMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DeploymentModeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DeploymentMode.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DEPLOYMENT_MODE_UNSPECIFIED: _DeploymentMode.ValueType  # 0
    DEPLOYMENT_MODE_COLOCATED: _DeploymentMode.ValueType  # 1
    """tf.data service workers colocate with TF workers."""
    DEPLOYMENT_MODE_REMOTE: _DeploymentMode.ValueType  # 2
    """tf.data service workers run in dedicated tf.data hosts."""
    DEPLOYMENT_MODE_HYBRID: _DeploymentMode.ValueType  # 3
    """tf.data service workers run in colocated TF hosts and dedicated tf.data
    hosts.
    """

class DeploymentMode(_DeploymentMode, metaclass=_DeploymentModeEnumTypeWrapper):
    """tf.data service deployment mode."""

DEPLOYMENT_MODE_UNSPECIFIED: DeploymentMode.ValueType  # 0
DEPLOYMENT_MODE_COLOCATED: DeploymentMode.ValueType  # 1
"""tf.data service workers colocate with TF workers."""
DEPLOYMENT_MODE_REMOTE: DeploymentMode.ValueType  # 2
"""tf.data service workers run in dedicated tf.data hosts."""
DEPLOYMENT_MODE_HYBRID: DeploymentMode.ValueType  # 3
"""tf.data service workers run in colocated TF hosts and dedicated tf.data
hosts.
"""
global___DeploymentMode = DeploymentMode

@typing.final
class ProcessingModeDef(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ShardingPolicy:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ShardingPolicyEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ProcessingModeDef._ShardingPolicy.ValueType], builtins.type
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        OFF: ProcessingModeDef._ShardingPolicy.ValueType  # 0
        """No sharding will be performed. Each worker produces the entire dataset
        without any sharding. With this mode, the best practice is to shuffle the
        dataset nondeterministically so that workers process the dataset in
        different orders.
        """
        DYNAMIC: ProcessingModeDef._ShardingPolicy.ValueType  # 1
        """The input dataset is dynamically split among workers at runtime. Each
        worker gets the next split when it reads data from the dispatcher. There
        is no fixed sharding with this mode.
        """
        FILE: ProcessingModeDef._ShardingPolicy.ValueType  # 2
        """The following are static sharding policies. The semantics are similar to
        `tf.data.experimental.AutoShardPolicy`. These policies require:
        * The tf.data service cluster has a fixed size, and you need to specify
          the workers in DispatcherConfig.
        * Each client only reads from the local tf.data service worker.

        Shards by input files (each worker will get a set of files to process).
        When this option is selected, make sure that there is at least as many
        files as workers. If there are fewer input files than workers, a runtime
        error will be raised.
        """
        DATA: ProcessingModeDef._ShardingPolicy.ValueType  # 3
        """Shards by elements produced by the dataset. Each worker will process the
        whole dataset and discard the portion that is not for itself. Note that
        for this mode to correctly partitions the dataset elements, the dataset
        needs to produce elements in a deterministic order.
        """
        FILE_OR_DATA: ProcessingModeDef._ShardingPolicy.ValueType  # 4
        """Attempts FILE-based sharding, falling back to DATA-based sharding on
        failures.
        """
        HINT: ProcessingModeDef._ShardingPolicy.ValueType  # 5
        """Looks for the presence of `shard(SHARD_HINT, ...)` which is treated as a
        placeholder to replace with `shard(num_workers, worker_index)`.
        """

    class ShardingPolicy(_ShardingPolicy, metaclass=_ShardingPolicyEnumTypeWrapper):
        """Specifies how data is sharded among tf.data service workers."""

    OFF: ProcessingModeDef.ShardingPolicy.ValueType  # 0
    """No sharding will be performed. Each worker produces the entire dataset
    without any sharding. With this mode, the best practice is to shuffle the
    dataset nondeterministically so that workers process the dataset in
    different orders.
    """
    DYNAMIC: ProcessingModeDef.ShardingPolicy.ValueType  # 1
    """The input dataset is dynamically split among workers at runtime. Each
    worker gets the next split when it reads data from the dispatcher. There
    is no fixed sharding with this mode.
    """
    FILE: ProcessingModeDef.ShardingPolicy.ValueType  # 2
    """The following are static sharding policies. The semantics are similar to
    `tf.data.experimental.AutoShardPolicy`. These policies require:
    * The tf.data service cluster has a fixed size, and you need to specify
      the workers in DispatcherConfig.
    * Each client only reads from the local tf.data service worker.

    Shards by input files (each worker will get a set of files to process).
    When this option is selected, make sure that there is at least as many
    files as workers. If there are fewer input files than workers, a runtime
    error will be raised.
    """
    DATA: ProcessingModeDef.ShardingPolicy.ValueType  # 3
    """Shards by elements produced by the dataset. Each worker will process the
    whole dataset and discard the portion that is not for itself. Note that
    for this mode to correctly partitions the dataset elements, the dataset
    needs to produce elements in a deterministic order.
    """
    FILE_OR_DATA: ProcessingModeDef.ShardingPolicy.ValueType  # 4
    """Attempts FILE-based sharding, falling back to DATA-based sharding on
    failures.
    """
    HINT: ProcessingModeDef.ShardingPolicy.ValueType  # 5
    """Looks for the presence of `shard(SHARD_HINT, ...)` which is treated as a
    placeholder to replace with `shard(num_workers, worker_index)`.
    """

    SHARDING_POLICY_FIELD_NUMBER: builtins.int
    sharding_policy: global___ProcessingModeDef.ShardingPolicy.ValueType
    def __init__(self, *, sharding_policy: global___ProcessingModeDef.ShardingPolicy.ValueType | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["sharding_policy", b"sharding_policy"]) -> None: ...

global___ProcessingModeDef = ProcessingModeDef

@typing.final
class DataServiceMetadata(google.protobuf.message.Message):
    """Metadata related to tf.data service datasets.
    Next tag: 4
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Compression:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CompressionEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DataServiceMetadata._Compression.ValueType], builtins.type
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        COMPRESSION_UNSPECIFIED: DataServiceMetadata._Compression.ValueType  # 0
        COMPRESSION_OFF: DataServiceMetadata._Compression.ValueType  # 1
        """No compression."""
        COMPRESSION_SNAPPY: DataServiceMetadata._Compression.ValueType  # 2
        """Snappy compression as defined in tensorflow/core/platform/snappy.h."""

    class Compression(_Compression, metaclass=_CompressionEnumTypeWrapper): ...
    COMPRESSION_UNSPECIFIED: DataServiceMetadata.Compression.ValueType  # 0
    COMPRESSION_OFF: DataServiceMetadata.Compression.ValueType  # 1
    """No compression."""
    COMPRESSION_SNAPPY: DataServiceMetadata.Compression.ValueType  # 2
    """Snappy compression as defined in tensorflow/core/platform/snappy.h."""

    ELEMENT_SPEC_FIELD_NUMBER: builtins.int
    COMPRESSION_FIELD_NUMBER: builtins.int
    CARDINALITY_FIELD_NUMBER: builtins.int
    element_spec: builtins.bytes
    """Serialized element spec."""
    compression: global___DataServiceMetadata.Compression.ValueType
    cardinality: builtins.int
    """Cardinality of the dataset."""
    def __init__(
        self,
        *,
        element_spec: builtins.bytes | None = ...,
        compression: global___DataServiceMetadata.Compression.ValueType | None = ...,
        cardinality: builtins.int | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["element_spec", b"element_spec", "optional_element_spec", b"optional_element_spec"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "cardinality",
            b"cardinality",
            "compression",
            b"compression",
            "element_spec",
            b"element_spec",
            "optional_element_spec",
            b"optional_element_spec",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["optional_element_spec", b"optional_element_spec"]
    ) -> typing.Literal["element_spec"] | None: ...

global___DataServiceMetadata = DataServiceMetadata

@typing.final
class CrossTrainerCacheOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRAINER_ID_FIELD_NUMBER: builtins.int
    trainer_id: builtins.str
    def __init__(self, *, trainer_id: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["trainer_id", b"trainer_id"]) -> None: ...

global___CrossTrainerCacheOptions = CrossTrainerCacheOptions

@typing.final
class DataServiceConfig(google.protobuf.message.Message):
    """Data service config available to the client through GetDataServiceConfig RPC.
    Next tag: 2
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPLOYMENT_MODE_FIELD_NUMBER: builtins.int
    deployment_mode: global___DeploymentMode.ValueType
    def __init__(self, *, deployment_mode: global___DeploymentMode.ValueType | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["deployment_mode", b"deployment_mode"]) -> None: ...

global___DataServiceConfig = DataServiceConfig
