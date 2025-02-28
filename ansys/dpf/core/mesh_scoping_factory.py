"""
mesh_scoping_factory
====================

Contains functions to simplify creating mesh scopings.
"""

from ansys.dpf.core import Scoping
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.common import locations


def nodal_scoping(node_ids, server=None):
    """Create a specific nodal :class:`ansys.dpf.core.Scoping` associated with a mesh.

    Parameters
    ----------
    node_ids : List of int
        List of IDs for the nodes.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : ansys.dpf.core.Scoping
    """
    if not isinstance(node_ids, list):
        raise dpf_errors.InvalidTypeError("list", "node_ids")
    scoping = Scoping(server=server, ids=node_ids, location=locations.nodal)
    return scoping


def elemental_scoping(element_ids, server=None):
    """Create a specific elemental :class:`ansys.dpf.core.Scoping` associated with a mesh.

    Parameters
    ----------
    element_ids : List of int
        List of IDs for the elements.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : ansys.dpf.core.Scoping
    """
    if not isinstance(element_ids, list):
        raise dpf_errors.InvalidTypeError("list", "element_ids")
    scoping = Scoping(server=server, ids=element_ids, location=locations.elemental)
    return scoping


def named_selection_scoping(named_selection_name, model, server=None):
    """Create a specific :class:`ansys.dpf.core.Scoping` associated with a specified model's mesh.

    Parameters
    ----------
    named_selection_name : str
        Name of the named selection.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : ansys.dpf.core.Scoping
    """
    return model.metadata.named_selection(named_selection_name)
