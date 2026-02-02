"""Tyck - TypeScript-style Pydantic Wrapper

A fluent, TypeScript-inspired API for Pydantic validation that makes it easier 
to define schemas with method chaining while maintaining full compatibility 
with Pydantic's features.

Installation:
    pip install Tyck

Quick Start:
    >>> from Tyck import interface, String, Integer
    >>> 
    >>> User = interface({
    ...     'id': Integer.positive(),
    ...     'name': String.min(1).max(100),
    ...     'email': String.email(),
    ... })
    >>> 
    >>> user = User(id=1, name="John", email="john@example.com")
    >>> print(user.model_dump())
    {'id': 1, 'name': 'John', 'email': 'john@example.com'}

Features:
    - TypeScript-like fluent API with method chaining
    - Full Pydantic compatibility (validation, serialization, JSON Schema)
    - Both functional (interface()) and class-based (@model()/@schema()) APIs
    - Utility functions (pick_fields, omit_fields, make_optional, extend_fields)
    - Immutable builder pattern
    - Complete type safety

Examples:
    See examples/ directory for comprehensive examples.
"""

__version__ = "0.1.0"

# Core exports
from Tyck.core.types import (
    String, Number, Integer, Boolean,
    DateTime, Date, Time, Uuid,
    Bytes, Decimal, Any, NoneType,
)

from Tyck.core.complex_types import (
    Array, Dict, Optional, Literal, Union,
    Set, Tuple, Enum,
)

from Tyck.api.functional import interface, config
from Tyck.api.class_based import model, schema, field
from Tyck.api.utils import pick_fields, omit_fields, make_optional, extend_fields, add_fields, merge_schemas, make_required
from Tyck.runtime_validation import ValidatedField, validate_call, validate_call_with_return

__all__ = [
    # Version
    "__version__",
    # Types
    "String", "Number", "Integer", "Boolean",
    "DateTime", "Date", "Time", "Uuid",
    "Bytes", "Decimal", "Any", "NoneType",
    # Complex types
    "Array", "Dict", "Optional", "Literal", "Union",
    "Set", "Tuple", "Enum",
    # APIs
    "interface", "config", "model", "schema", "field",
    # Utilities
    "pick_fields", "omit_fields", "make_optional", "extend_fields", "add_fields",
    "merge_schemas", "make_required",
    # Runtime validation
    "ValidatedField", "validate_call", "validate_call_with_return",
]
