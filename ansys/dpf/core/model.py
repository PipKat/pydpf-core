"""
.. _ref_model:

Model
=====
Module contains the Model class to manage file result models.


"""

from ansys import dpf
from ansys.dpf.core import Operator
from ansys.dpf.core.common import types
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.results import Results
from grpc._channel import _InactiveRpcError


class Model:
    """Connects to a gRPC DPF server and allows access to a result using the DPF framework.

    Parameters
    ----------
    data_sources : str, dpf.core.DataSources
        Accepts either a :class:`dpf.core.DataSources` instance or the name of the
        result file to open. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)

    """

    def __init__(self, data_sources=None, server=None):
        """Initialize connection with DPF server."""

        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._metadata = Metadata(data_sources, self._server)
        self._results = Results(self)

    @property
    def metadata(self):
        """Model metadata.

        Includes:

        - ``data_sources``
        - ``meshed_region``
        - ``time_freq_support``
        - ``result_info``
        - ``mesh_provider``

        Returns
        -------
        metadata : Metadata

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)

        Get the meshed region of the model and extract the element
        numbers.

        >>> meshed_region = model.metadata.meshed_region
        >>> meshed_region.elements.scoping.ids[2]
        759

        Get the data sources of the model.

        >>> ds = model.metadata.data_sources

        Print the number of result sets.

        >>> tf = model.metadata.time_freq_support
        >>> tf.n_sets
        35

        Get the unit system used in the analysis.

        >>> rinfo = model.metadata.result_info
        >>> rinfo.unit_system
        'Metric (m, kg, N, s, V, A)'

        """
        return self._metadata

    @property
    def results(self):
        """Available results of the model.

        Organizes the results from DPF into accessible methods. All the available
        results are dynamically created depending on the model's class:`ansys.dpf.core.result_info`.

        Returns
        -------
        Results
            Available results of the model.

        Attributes
        ----------
        all types of results : Result
            Result provider helper wrapping all types of provider available for a
            given result file.

            Examples
            --------
            Create a stress result from the model and choose its time and mesh scopings.

            >>> from ansys.dpf import core as dpf
            >>> from ansys.dpf.core import examples
            >>> model = dpf.Model(examples.electric_therm)
            >>> v = model.results.electric_potential
            >>> rf = model.results.reaction_force
            >>> dissip = model.results.thermal_dissipation_energy

        Examples
        --------
        Extract the result object from a model.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.simple_bar)
        >>> results = model.results # printable object

        Access the displacement at all times.

        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> displacements = model.results.displacement.on_all_time_freqs.eval()

        """
        return self._results

    def __connect_op__(self, op):
        """Connect the data sources or the streams to the operator."""
        if self.metadata._stream_provider is not None and hasattr(op.inputs, "streams"):
            op.inputs.streams.connect(self.metadata._stream_provider.outputs)
        elif self.metadata._data_sources is not None and hasattr(
            op.inputs, "data_sources"
        ):
            op.inputs.data_sources.connect(self.metadata._data_sources)

    def operator(self, name):
        """Operator associated with the data sources of this model.

        Parameters
        ----------
        name : str
            Operator name, which must be valid.

        Examples
        --------
        Create a displacement operator.

        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> disp = model.operator('U')

        Create a sum operator.

        >>> sum = model.operator('accumulate')

        """
        op = Operator(name=name, server=self._server)
        self.__connect_op__(op)
        return op

    def __str__(self):
        txt = "DPF Model\n"
        txt += "-" * 30 + "\n"
        txt += str(self.results)
        txt += "-" * 30 + "\n"
        txt += str(self.metadata.meshed_region)
        txt += "\n" + "-" * 30 + "\n"
        txt += str(self.metadata.time_freq_support)
        return txt

    def plot(self, color="w", show_edges=True, **kwargs):
        """Plot the mesh of the model.

        Examples
        --------
        Plot the model using the default options.

        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> model.plot()

        """
        self.metadata.meshed_region.grid.plot(
            color=color, show_edges=show_edges, **kwargs
        )


class Metadata:
    """Contains the metadata of a data source.

    Parameters
    ----------
    data_sources :

    server : server.DPFServer
        Server with the channel connected to the remote or local instance.

    """

    def __init__(self, data_sources, server):
        self._server = server
        self._set_data_sources(data_sources)
        self._meshed_region = None
        self.result_info = None
        self._stream_provider = None
        self._time_freq_support = None
        self._cache_streams_provider()
        self._cache_result_info()

    def _cache_result_info(self):
        """Store result information."""
        self.result_info = self._load_result_info()

    def _cache_streams_provider(self):
        """Create a stream provider and cache it."""
        from ansys.dpf.core import operators

        if hasattr(operators, "metadata") and hasattr(
            operators.metadata, "stream_provider"
        ):
            self._stream_provider = operators.metadata.streams_provider(
                data_sources=self._data_sources, server=self._server
            )
        else:
            self._stream_provider = Operator("stream_provider", server=self._server)
            self._stream_provider.inputs.connect(self._data_sources)

    @property
    def time_freq_support(self):
        """Time frequency support.

        Returns
        -------
        ansys.dpf.core.time_freq_support.TimeFreqSupport
            Time frequency support.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)

        Get the number of sets from the result file.

        >>> tf = model.metadata.time_freq_support
        >>> tf.n_sets
        35

        Get the time values for the active result.

        >>> tf.time_frequencies.data
        array([0.        , 0.019975  , 0.039975  , 0.059975  , 0.079975  ,
               0.099975  , 0.119975  , 0.139975  , 0.159975  , 0.179975  ,
               0.199975  , 0.218975  , 0.238975  , 0.258975  , 0.278975  ,
               0.298975  , 0.318975  , 0.338975  , 0.358975  , 0.378975  ,
               0.398975  , 0.417975  , 0.437975  , 0.457975  , 0.477975  ,
               0.497975  , 0.517975  , 0.53754972, 0.55725277, 0.57711786,
               0.59702054, 0.61694639, 0.63683347, 0.65673452, 0.67662783])

        """
        if self._time_freq_support is None:
            timeProvider = Operator("TimeFreqSupportProvider", server=self._server)
            timeProvider.inputs.connect(self._stream_provider.outputs)
            self._time_freq_support = timeProvider.get_output(
                0, types.time_freq_support
            )
        return self._time_freq_support

    @property
    def data_sources(self):
        """Data sources instance.

        This data source can be connected to other operators.

        Returns
        -------
        data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)

        Connect the model data sources to the 'U' operator.

        >>> ds = model.metadata.data_sources
        >>> op = dpf.operators.result.displacement()
        >>> op.inputs.data_sources.connect(ds)

        """
        return self._data_sources

    @property
    def streams_provider(self):
        """Streams provider operator connected to the data sources.

        This streams provider can be connected to other operators.

        Returns
        -------
        streams_provider : operators.metadata.streams_provider

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)

        Connect the model data sources to the ``U`` operator.

        >>> streams = model.metadata.streams_provider
        >>> op = dpf.operators.result.displacement()
        >>> op.inputs.streams_container.connect(streams)

        """
        return self._stream_provider

    def _set_data_sources(self, var_inp):
        if isinstance(var_inp, dpf.core.DataSources):
            self._data_sources = var_inp
        elif isinstance(var_inp, str):
            self._data_sources = DataSources(var_inp, server=self._server)
        else:
            self._data_sources = DataSources(server=self._server)
        self._cache_streams_provider()

    def _load_result_info(self):
        """Returns a result info object"""
        op = Operator("ResultInfoProvider", server=self._server)
        op.inputs.connect(self._stream_provider.outputs)
        try:
            result_info = op.get_output(0, types.result_info)
        except _InactiveRpcError as e:
            # give the user a more helpful error
            if "results file is not defined in the Data sources" in e.details():
                raise RuntimeError("Unable to open result file") from None
            else:
                raise e
        return result_info

    @property
    def meshed_region(self):
        """Meshed region instance.

        Returns
        -------
        mesh : :class:`ansys.dpf.core.meshed_region`
            Mesh
        """
        # NOTE: this uses the cached mesh and we might consider
        # changing this
        if self._meshed_region is None:
            self._meshed_region = self.mesh_provider.get_output(0, types.meshed_region)
            self._meshed_region._set_stream_provider(self._stream_provider)

        return self._meshed_region

    @property
    def mesh_provider(self):
        """Mesh provider operator.

        This operator reads a mesh from the result file. The underlying
        operator symbol is the class:`ansys.dpf.core.operators.mesh.mesh_provider`
        operator.

        Returns
        -------
        mesh_provider : class:`ansys.dpf.core.operators.mesh.mesh_provider`
            Mesh provider operator.

        """
        try:
            tmp = Operator("MeshSelectionManagerProvider", server=self._server)
            tmp.inputs.connect(self._stream_provider.outputs)
            tmp.run()
        except:
            pass
        mesh_provider = Operator("MeshProvider", server=self._server)
        mesh_provider.inputs.connect(self._stream_provider.outputs)
        return mesh_provider

    @property
    def available_named_selections(self):
        """List of available named selections.

        Returns
        -------
        named_selections : list str
        """
        return self.meshed_region.available_named_selections

    def named_selection(self, named_selection):
        """Scoping containing the list of nodes or elements in the named selection.

        Parameters
        ----------
        named_selection : str
            name of the named selection

        Returns
        -------
        named_selection : :class:`ansys.dpf.core.scoping`
        """
        return self.meshed_region.named_selection(named_selection)
