from _typeshed import Incomplete
from abc import ABCMeta
from typing_extensions import TypeAlias

from tensorflow import Tensor, TensorShape
from tensorflow._aliases import TensorCompatible
from tensorflow.dtypes import DType

_SparseTensorCompatible: TypeAlias = TensorCompatible | SparseTensor

class SparseTensor(metaclass=ABCMeta):
    @property
    def indices(self) -> Tensor: ...
    @property
    def values(self) -> Tensor: ...
    @property
    def dense_shape(self) -> Tensor: ...
    @property
    def shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    name: str
    def __init__(self, indices: TensorCompatible, values: TensorCompatible, dense_shape: TensorCompatible) -> None: ...
    def get_shape(self) -> TensorShape: ...
    # Many arithmetic operations are not directly supported. Some have alternatives like tf.sparse.add instead of +.
    def __div__(self, y: _SparseTensorCompatible) -> SparseTensor: ...
    def __truediv__(self, y: _SparseTensorCompatible) -> SparseTensor: ...
    def __mul__(self, y: _SparseTensorCompatible) -> SparseTensor: ...
    def __getattr__(self, name: str) -> Incomplete: ...

def __getattr__(name: str): ...  # incomplete module
