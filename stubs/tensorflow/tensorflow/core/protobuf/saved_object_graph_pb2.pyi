"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2
import tensorflow.core.framework.variable_pb2
import tensorflow.core.framework.versions_pb2
import tensorflow.core.protobuf.struct_pb2
import tensorflow.core.protobuf.trackable_object_graph_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SavedObjectGraph(google.protobuf.message.Message):
    """SavedObjectGraph shares some structure with TrackableObjectGraph, but
    SavedObjectGraph belongs to the MetaGraph and contains pointers to functions
    and type information, while TrackableObjectGraph lives in the checkpoint
    and contains pointers only to variable values.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class ConcreteFunctionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___SavedConcreteFunction: ...
        def __init__(self, *, key: builtins.str | None = ..., value: global___SavedConcreteFunction | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NODES_FIELD_NUMBER: builtins.int
    CONCRETE_FUNCTIONS_FIELD_NUMBER: builtins.int
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SavedObject]:
        """Flattened list of objects in the object graph.

        The position of the object in this list indicates its id.
        Nodes[0] is considered the root node.
        """

    @property
    def concrete_functions(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___SavedConcreteFunction]:
        """Information about captures and output structures in concrete functions.
        Referenced from SavedBareConcreteFunction and SavedFunction.
        """

    def __init__(
        self,
        *,
        nodes: collections.abc.Iterable[global___SavedObject] | None = ...,
        concrete_functions: collections.abc.Mapping[builtins.str, global___SavedConcreteFunction] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["concrete_functions", b"concrete_functions", "nodes", b"nodes"]) -> None: ...

global___SavedObjectGraph = SavedObjectGraph

@typing.final
class SavedObject(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class SaveableObjectsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___SaveableObject: ...
        def __init__(self, *, key: builtins.str | None = ..., value: global___SaveableObject | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    CHILDREN_FIELD_NUMBER: builtins.int
    DEPENDENCIES_FIELD_NUMBER: builtins.int
    SLOT_VARIABLES_FIELD_NUMBER: builtins.int
    USER_OBJECT_FIELD_NUMBER: builtins.int
    ASSET_FIELD_NUMBER: builtins.int
    FUNCTION_FIELD_NUMBER: builtins.int
    VARIABLE_FIELD_NUMBER: builtins.int
    BARE_CONCRETE_FUNCTION_FIELD_NUMBER: builtins.int
    CONSTANT_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    CAPTURED_TENSOR_FIELD_NUMBER: builtins.int
    SAVEABLE_OBJECTS_FIELD_NUMBER: builtins.int
    REGISTERED_NAME_FIELD_NUMBER: builtins.int
    SERIALIZED_USER_PROTO_FIELD_NUMBER: builtins.int
    REGISTERED_SAVER_FIELD_NUMBER: builtins.int
    registered_name: builtins.str
    """The fields below are filled when the user serializes a registered Trackable
    class or an object with a registered saver function.

    Registered classes may save additional metadata and supersede the
    default loading process where nodes are recreated from the proto.
    If the registered class cannot be found, then the object will load as one
    one of the default trackable objects: Autotrackable (a class similar to
    tf.Module), tf.function, or tf.Variable.

    Unlike SaveableObjects, which store the functions for saving and restoring
    from tensors, registered savers allow Trackables to write checkpoint shards
    directly (e.g. for performance or coordination reasons).
    *All registered savers must be available when loading the SavedModel.*

    The name of the registered class of the form "{package}.{class_name}".
    This field is used to search for the registered class at loading time.
    """
    registered_saver: builtins.str
    """String name of the registered saver. At most one of `saveable_objects` or
    `registered_saver` is defined for each SavedObject.
    """
    @property
    def children(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        tensorflow.core.protobuf.trackable_object_graph_pb2.TrackableObjectGraph.TrackableObject.ObjectReference
    ]:
        """Objects which this object depends on: named edges in the dependency
        graph.

        Note: All kinds of SavedObject may have children, except
        "constant" and "captured_tensor".
        """

    @property
    def dependencies(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        tensorflow.core.protobuf.trackable_object_graph_pb2.TrackableObjectGraph.TrackableObject.ObjectReference
    ]:
        """Ordered list of dependencies that must be loaded before this object.
        SavedModel loads with the bottom-up approach, by first creating all objects
        (in the order defined by the dependencies), then connecting the edges.
        """

    @property
    def slot_variables(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        tensorflow.core.protobuf.trackable_object_graph_pb2.TrackableObjectGraph.TrackableObject.SlotVariableReference
    ]:
        """Slot variables owned by this object. This describes the three-way
        (optimizer, variable, slot variable) relationship; none of the three
        depend on the others directly.

        Note: currently only valid if kind == "user_object".
        """

    @property
    def user_object(self) -> global___SavedUserObject: ...
    @property
    def asset(self) -> global___SavedAsset: ...
    @property
    def function(self) -> global___SavedFunction: ...
    @property
    def variable(self) -> global___SavedVariable: ...
    @property
    def bare_concrete_function(self) -> global___SavedBareConcreteFunction: ...
    @property
    def constant(self) -> global___SavedConstant: ...
    @property
    def resource(self) -> global___SavedResource: ...
    @property
    def captured_tensor(self) -> global___CapturedTensor: ...
    @property
    def saveable_objects(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___SaveableObject]:
        """Stores the functions used to save and restore this object. At most one of
        `saveable_objects` or `registered_saver` is defined for each SavedObject.
        See the comment below for the difference between SaveableObject and
        registered savers.
        """

    @property
    def serialized_user_proto(self) -> google.protobuf.any_pb2.Any:
        """The user-generated proto storing metadata for this object, to be passed to
        the registered classes's _deserialize_from_proto method when this object is
        loaded from the SavedModel.
        """

    def __init__(
        self,
        *,
        children: (
            collections.abc.Iterable[
                tensorflow.core.protobuf.trackable_object_graph_pb2.TrackableObjectGraph.TrackableObject.ObjectReference
            ]
            | None
        ) = ...,
        dependencies: (
            collections.abc.Iterable[
                tensorflow.core.protobuf.trackable_object_graph_pb2.TrackableObjectGraph.TrackableObject.ObjectReference
            ]
            | None
        ) = ...,
        slot_variables: (
            collections.abc.Iterable[
                tensorflow.core.protobuf.trackable_object_graph_pb2.TrackableObjectGraph.TrackableObject.SlotVariableReference
            ]
            | None
        ) = ...,
        user_object: global___SavedUserObject | None = ...,
        asset: global___SavedAsset | None = ...,
        function: global___SavedFunction | None = ...,
        variable: global___SavedVariable | None = ...,
        bare_concrete_function: global___SavedBareConcreteFunction | None = ...,
        constant: global___SavedConstant | None = ...,
        resource: global___SavedResource | None = ...,
        captured_tensor: global___CapturedTensor | None = ...,
        saveable_objects: collections.abc.Mapping[builtins.str, global___SaveableObject] | None = ...,
        registered_name: builtins.str | None = ...,
        serialized_user_proto: google.protobuf.any_pb2.Any | None = ...,
        registered_saver: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "asset",
            b"asset",
            "bare_concrete_function",
            b"bare_concrete_function",
            "captured_tensor",
            b"captured_tensor",
            "constant",
            b"constant",
            "function",
            b"function",
            "kind",
            b"kind",
            "resource",
            b"resource",
            "serialized_user_proto",
            b"serialized_user_proto",
            "user_object",
            b"user_object",
            "variable",
            b"variable",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "asset",
            b"asset",
            "bare_concrete_function",
            b"bare_concrete_function",
            "captured_tensor",
            b"captured_tensor",
            "children",
            b"children",
            "constant",
            b"constant",
            "dependencies",
            b"dependencies",
            "function",
            b"function",
            "kind",
            b"kind",
            "registered_name",
            b"registered_name",
            "registered_saver",
            b"registered_saver",
            "resource",
            b"resource",
            "saveable_objects",
            b"saveable_objects",
            "serialized_user_proto",
            b"serialized_user_proto",
            "slot_variables",
            b"slot_variables",
            "user_object",
            b"user_object",
            "variable",
            b"variable",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["kind", b"kind"]
    ) -> (
        typing.Literal[
            "user_object", "asset", "function", "variable", "bare_concrete_function", "constant", "resource", "captured_tensor"
        ]
        | None
    ): ...

global___SavedObject = SavedObject

@typing.final
class SavedUserObject(google.protobuf.message.Message):
    """A SavedUserObject is an object (in the object-oriented language of the
    TensorFlow program) of some user- or framework-defined class other than
    those handled specifically by the other kinds of SavedObjects.

    This object cannot be evaluated as a tensor, and therefore cannot be bound
    to an input of a function.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDENTIFIER_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    identifier: builtins.str
    """Corresponds to a registration of the type to use in the loading program."""
    metadata: builtins.str
    """Metadata for deserializing this object.

    Deprecated! At the time of deprecation, Keras was the only user of this
    field, and its saving and loading code will be updated shortly.
    Please save your application-specific metadata to a separate file.
    """
    @property
    def version(self) -> tensorflow.core.framework.versions_pb2.VersionDef:
        """Version information from the producer of this SavedUserObject."""

    def __init__(
        self,
        *,
        identifier: builtins.str | None = ...,
        version: tensorflow.core.framework.versions_pb2.VersionDef | None = ...,
        metadata: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["version", b"version"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["identifier", b"identifier", "metadata", b"metadata", "version", b"version"]
    ) -> None: ...

global___SavedUserObject = SavedUserObject

@typing.final
class SavedAsset(google.protobuf.message.Message):
    """A SavedAsset points to an asset in the MetaGraph.

    When bound to a function this object evaluates to a tensor with the absolute
    filename. Users should not depend on a particular part of the filename to
    remain stable (e.g. basename could be changed).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSET_FILE_DEF_INDEX_FIELD_NUMBER: builtins.int
    asset_file_def_index: builtins.int
    """Index into `MetaGraphDef.asset_file_def[]` that describes the Asset.

    Only the field `AssetFileDef.filename` is used. Other fields, such as
    `AssetFileDef.tensor_info`, MUST be ignored.
    """
    def __init__(self, *, asset_file_def_index: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["asset_file_def_index", b"asset_file_def_index"]) -> None: ...

global___SavedAsset = SavedAsset

@typing.final
class SavedFunction(google.protobuf.message.Message):
    """A function with multiple signatures, possibly with non-Tensor arguments."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONCRETE_FUNCTIONS_FIELD_NUMBER: builtins.int
    FUNCTION_SPEC_FIELD_NUMBER: builtins.int
    @property
    def concrete_functions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def function_spec(self) -> global___FunctionSpec: ...
    def __init__(
        self,
        *,
        concrete_functions: collections.abc.Iterable[builtins.str] | None = ...,
        function_spec: global___FunctionSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["function_spec", b"function_spec"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["concrete_functions", b"concrete_functions", "function_spec", b"function_spec"]
    ) -> None: ...

global___SavedFunction = SavedFunction

@typing.final
class CapturedTensor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CONCRETE_FUNCTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of captured tensor"""
    concrete_function: builtins.str
    """Name of concrete function which contains the computed graph tensor."""
    def __init__(self, *, name: builtins.str | None = ..., concrete_function: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["concrete_function", b"concrete_function", "name", b"name"]) -> None: ...

global___CapturedTensor = CapturedTensor

@typing.final
class SavedConcreteFunction(google.protobuf.message.Message):
    """Stores low-level information about a concrete function. Referenced in either
    a SavedFunction or a SavedBareConcreteFunction.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BOUND_INPUTS_FIELD_NUMBER: builtins.int
    CANONICALIZED_INPUT_SIGNATURE_FIELD_NUMBER: builtins.int
    OUTPUT_SIGNATURE_FIELD_NUMBER: builtins.int
    @property
    def bound_inputs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def canonicalized_input_signature(self) -> tensorflow.core.protobuf.struct_pb2.StructuredValue:
        """Input in canonicalized form that was received to create this concrete
        function.
        """

    @property
    def output_signature(self) -> tensorflow.core.protobuf.struct_pb2.StructuredValue:
        """Output that was the return value of this function after replacing all
        Tensors with TensorSpecs. This can be an arbitrary nested function and will
        be used to reconstruct the full structure from pure tensors.
        """

    def __init__(
        self,
        *,
        bound_inputs: collections.abc.Iterable[builtins.int] | None = ...,
        canonicalized_input_signature: tensorflow.core.protobuf.struct_pb2.StructuredValue | None = ...,
        output_signature: tensorflow.core.protobuf.struct_pb2.StructuredValue | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "canonicalized_input_signature", b"canonicalized_input_signature", "output_signature", b"output_signature"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "bound_inputs",
            b"bound_inputs",
            "canonicalized_input_signature",
            b"canonicalized_input_signature",
            "output_signature",
            b"output_signature",
        ],
    ) -> None: ...

global___SavedConcreteFunction = SavedConcreteFunction

@typing.final
class SavedBareConcreteFunction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONCRETE_FUNCTION_NAME_FIELD_NUMBER: builtins.int
    ARGUMENT_KEYWORDS_FIELD_NUMBER: builtins.int
    ALLOWED_POSITIONAL_ARGUMENTS_FIELD_NUMBER: builtins.int
    FUNCTION_SPEC_FIELD_NUMBER: builtins.int
    concrete_function_name: builtins.str
    """Identifies a SavedConcreteFunction."""
    allowed_positional_arguments: builtins.int
    """The prefix of `argument_keywords` which may be identified by position."""
    @property
    def argument_keywords(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """A sequence of unique strings, one per Tensor argument."""

    @property
    def function_spec(self) -> global___FunctionSpec:
        """The spec of the function that this ConcreteFunction is traced from. This
        allows the ConcreteFunction to be called with nest structure inputs. This
        field may not be populated. If this field is absent, the concrete function
        can only be called with flat inputs.
        TODO(b/169361281): support calling saved ConcreteFunction with structured
        inputs in C++ SavedModel API.
        """

    def __init__(
        self,
        *,
        concrete_function_name: builtins.str | None = ...,
        argument_keywords: collections.abc.Iterable[builtins.str] | None = ...,
        allowed_positional_arguments: builtins.int | None = ...,
        function_spec: global___FunctionSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["function_spec", b"function_spec"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "allowed_positional_arguments",
            b"allowed_positional_arguments",
            "argument_keywords",
            b"argument_keywords",
            "concrete_function_name",
            b"concrete_function_name",
            "function_spec",
            b"function_spec",
        ],
    ) -> None: ...

global___SavedBareConcreteFunction = SavedBareConcreteFunction

@typing.final
class SavedConstant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATION_FIELD_NUMBER: builtins.int
    operation: builtins.str
    """An Operation name for a ConstantOp in this SavedObjectGraph's MetaGraph."""
    def __init__(self, *, operation: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["operation", b"operation"]) -> None: ...

global___SavedConstant = SavedConstant

@typing.final
class SavedVariable(google.protobuf.message.Message):
    """Represents a Variable that is initialized by loading the contents from the
    checkpoint.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DTYPE_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    TRAINABLE_FIELD_NUMBER: builtins.int
    SYNCHRONIZATION_FIELD_NUMBER: builtins.int
    AGGREGATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    EXPERIMENTAL_DISTRIBUTED_VARIABLE_COMPONENTS_FIELD_NUMBER: builtins.int
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    trainable: builtins.bool
    synchronization: tensorflow.core.framework.variable_pb2.VariableSynchronization.ValueType
    aggregation: tensorflow.core.framework.variable_pb2.VariableAggregation.ValueType
    name: builtins.str
    device: builtins.str
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    @property
    def experimental_distributed_variable_components(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SavedVariable]:
        """List of component variables for a distributed variable.

        When this field is non-empty, the SavedVariable will be assumed
        to be a distributed variable defined by the components listed here.

        This is only supported by experimental loaders at the moment.
        """

    def __init__(
        self,
        *,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        trainable: builtins.bool | None = ...,
        synchronization: tensorflow.core.framework.variable_pb2.VariableSynchronization.ValueType | None = ...,
        aggregation: tensorflow.core.framework.variable_pb2.VariableAggregation.ValueType | None = ...,
        name: builtins.str | None = ...,
        device: builtins.str | None = ...,
        experimental_distributed_variable_components: collections.abc.Iterable[global___SavedVariable] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["shape", b"shape"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "aggregation",
            b"aggregation",
            "device",
            b"device",
            "dtype",
            b"dtype",
            "experimental_distributed_variable_components",
            b"experimental_distributed_variable_components",
            "name",
            b"name",
            "shape",
            b"shape",
            "synchronization",
            b"synchronization",
            "trainable",
            b"trainable",
        ],
    ) -> None: ...

global___SavedVariable = SavedVariable

@typing.final
class FunctionSpec(google.protobuf.message.Message):
    """Represents `FunctionSpec` used in `Function`. This represents a
    function that has been wrapped as a TensorFlow `Function`.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _JitCompile:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _JitCompileEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FunctionSpec._JitCompile.ValueType], builtins.type
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEFAULT: FunctionSpec._JitCompile.ValueType  # 0
        ON: FunctionSpec._JitCompile.ValueType  # 1
        OFF: FunctionSpec._JitCompile.ValueType  # 2

    class JitCompile(_JitCompile, metaclass=_JitCompileEnumTypeWrapper):
        """Whether the function should be compiled by XLA.

        The public interface to `tf.function` uses an optional boolean to
        represent three distinct states for this field.  Unfortunately, proto3
        removes the ability to explicitly check for the presence or absence of a
        field, so we instead map to an enum.

        See `tf.function` for details.
        """

    DEFAULT: FunctionSpec.JitCompile.ValueType  # 0
    ON: FunctionSpec.JitCompile.ValueType  # 1
    OFF: FunctionSpec.JitCompile.ValueType  # 2

    FULLARGSPEC_FIELD_NUMBER: builtins.int
    IS_METHOD_FIELD_NUMBER: builtins.int
    INPUT_SIGNATURE_FIELD_NUMBER: builtins.int
    JIT_COMPILE_FIELD_NUMBER: builtins.int
    is_method: builtins.bool
    """Whether this represents a class method."""
    jit_compile: global___FunctionSpec.JitCompile.ValueType
    @property
    def fullargspec(self) -> tensorflow.core.protobuf.struct_pb2.StructuredValue:
        """Full arg spec from inspect.getfullargspec()."""

    @property
    def input_signature(self) -> tensorflow.core.protobuf.struct_pb2.StructuredValue:
        """The input signature, if specified."""

    def __init__(
        self,
        *,
        fullargspec: tensorflow.core.protobuf.struct_pb2.StructuredValue | None = ...,
        is_method: builtins.bool | None = ...,
        input_signature: tensorflow.core.protobuf.struct_pb2.StructuredValue | None = ...,
        jit_compile: global___FunctionSpec.JitCompile.ValueType | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["fullargspec", b"fullargspec", "input_signature", b"input_signature"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "fullargspec",
            b"fullargspec",
            "input_signature",
            b"input_signature",
            "is_method",
            b"is_method",
            "jit_compile",
            b"jit_compile",
        ],
    ) -> None: ...

global___FunctionSpec = FunctionSpec

@typing.final
class SavedResource(google.protobuf.message.Message):
    """A SavedResource represents a TF object that holds state during its lifetime.
    An object of this type can have a reference to a:
    create_resource() and an initialize() function.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_FIELD_NUMBER: builtins.int
    device: builtins.str
    """A device specification indicating a required placement for the resource
    creation function, e.g. "CPU". An empty string allows the user to select a
    device.
    """
    def __init__(self, *, device: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["device", b"device"]) -> None: ...

global___SavedResource = SavedResource

@typing.final
class SaveableObject(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SAVE_FUNCTION_FIELD_NUMBER: builtins.int
    RESTORE_FUNCTION_FIELD_NUMBER: builtins.int
    save_function: builtins.int
    """Node ids of concrete functions for saving and loading from a checkpoint.
    These functions save and restore directly from tensors.
    """
    restore_function: builtins.int
    def __init__(self, *, save_function: builtins.int | None = ..., restore_function: builtins.int | None = ...) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["restore_function", b"restore_function", "save_function", b"save_function"]
    ) -> None: ...

global___SaveableObject = SaveableObject
