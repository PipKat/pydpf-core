import pytest
import numpy as np

from ansys import dpf
from ansys.dpf.core import TimeFreqSupport, Model
from ansys.dpf.core import fields_factory
from ansys.dpf.core.common import locations
from ansys.dpf.core import examples


@pytest.fixture()
def vel_acc_model(velocity_acceleration):
    return dpf.core.Model(velocity_acceleration)


def test_get_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    assert res.n_sets == 5
    assert res.get_frequency(0, 0) == 0.02
    assert res.get_frequency(0, 1) == 0.04
    assert res.get_frequency(cumulative_index=2) == 0.06
    assert res.get_cumulative_index(0, 0) == 0
    assert res.get_cumulative_index(freq=0.06) == 2


def test_model_time_freq_support(vel_acc_model):
    timefreq = vel_acc_model.metadata.time_freq_support
    assert str(timefreq.n_sets) in str(timefreq)
    assert len(timefreq.time_frequencies.data) == timefreq.n_sets
    expected_data = [0.02, 0.04, 0.06, 0.08, 0.1]
    assert np.allclose(expected_data, timefreq.time_frequencies.data)


def test_get_frequencies_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    freq = res.time_frequencies
    assert np.allclose(freq.data, [0.02, 0.04, 0.06, 0.08, 0.1])
    assert freq.scoping.ids == [1]


def test_print_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    assert "Number of sets: 5" in str(res)
    assert "Time (s)" in str(res)
    assert "LoadStep" in str(res)
    assert "Substep" in str(res)


def test_delete_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    res.__del__()
    with pytest.raises(Exception):
        res.get_frequence(0, 0)


def test_delete_auto_timefreqsupport(simple_rst):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(simple_rst)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    res1 = dpf.core.TimeFreqSupport(res._message)
    res.__del__()
    with pytest.raises(Exception):
        res1.n_sets


def test_create_time_freq_support():
    tfq = TimeFreqSupport()
    assert tfq is not None


def test_update_time_freq_support_real_freq():
    tfq = TimeFreqSupport()
    frequencies = fields_factory.create_scalar_field(3)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies
    frequencies_check = tfq.time_frequencies
    assert np.allclose(frequencies.data, frequencies_check.data)
    assert tfq.rpms is None
    assert tfq.complex_frequencies is None


def test_update_time_freq_support_im_freq():
    tfq = TimeFreqSupport()
    frequencies = fields_factory.create_scalar_field(3)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.complex_frequencies = frequencies
    frequencies_check = tfq.complex_frequencies
    assert np.allclose(frequencies.data, frequencies_check.data)
    assert tfq.rpms is None
    assert tfq.time_frequencies is None


def test_update_time_freq_support_rpms():
    tfq = TimeFreqSupport()
    rpm = fields_factory.create_scalar_field(3)
    rpm.data = [0.1, 0.32, 0.4]
    tfq.rpms = rpm
    rpm_check = tfq.rpms
    assert np.allclose(rpm.data, rpm_check.data)
    assert tfq.time_frequencies is None
    assert tfq.complex_frequencies is None


def test_update_time_freq_support_harmonic_indeces():
    tfq = TimeFreqSupport()
    harm = fields_factory.create_scalar_field(3)
    harm.data = [0.1, 0.32, 0.4]
    tfq.set_harmonic_indices(harm)
    harm_check = tfq.get_harmonic_indices()
    assert np.allclose(harm.data, harm_check.data)
    assert tfq.time_frequencies is None
    assert tfq.complex_frequencies is None
    assert tfq.rpms is None


def test_update_time_freq_support_harmonic_indeces_with_num_stage():
    tfq = TimeFreqSupport()
    harm = fields_factory.create_scalar_field(3)
    harm.data = [0.12, 0.32, 0.8]
    tfq.set_harmonic_indices(harm, 2)
    harm_check = tfq.get_harmonic_indices(2)
    assert np.allclose(harm.data, harm_check.data)
    assert tfq.time_frequencies is None
    assert tfq.complex_frequencies is None
    assert tfq.rpms is None
    harm_check_2 = tfq.get_harmonic_indices(3)
    assert harm_check_2 is None
    harm_check_3 = tfq.get_harmonic_indices(0)
    assert harm_check_3 is None
    harm_check_4 = tfq.get_harmonic_indices()
    assert harm_check_4 is None


def test_update_time_freq_support_real_freq_with_ds(velocity_acceleration):
    model = Model(velocity_acceleration)
    disp = model.results.displacement()
    tfq = disp.outputs.fields_container().time_freq_support
    assert tfq.time_frequencies is not None
    frequencies = fields_factory.create_scalar_field(3)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies
    frequencies_check = tfq.time_frequencies
    assert np.allclose(frequencies.data, frequencies_check.data)


def test_append_step_1():
    tfq = TimeFreqSupport()
    frequencies = [0.1, 0.21, 1.0]
    tfq.append_step(1, frequencies, rpm_value=2.0)
    assert len(tfq.rpms.data) == 1
    assert len(tfq.time_frequencies.data) == 3
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose(frequencies, tfq.time_frequencies.data)
    assert np.allclose(2.0, tfq.rpms.data)
    assert tfq.complex_frequencies is None
    assert tfq.get_harmonic_indices() is None
    frequencies2 = [1.1, 2.0]
    tfq.append_step(1, frequencies2, rpm_value=2.0)
    assert len(tfq.rpms.data) == 2
    assert len(tfq.time_frequencies.data) == 5
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose(frequencies + frequencies2, tfq.time_frequencies.data)
    assert np.allclose(2.0, tfq.rpms.data)
    assert tfq.complex_frequencies is None
    assert tfq.get_harmonic_indices() is None


def test_append_step_2():
    tfq = TimeFreqSupport()
    tfq.append_step(
        1, [0.1, 0.21, 1.0], rpm_value=2.0, step_harmonic_indices=[1.0, 2.0, 3.0]
    )
    tfq.append_step(2, [1.1, 2.0], rpm_value=2.3, step_harmonic_indices=[1.0, 2.0])
    tfq.append_step(3, [0.23, 0.25], rpm_value=3.0, step_harmonic_indices=[1.0, 2.0])
    assert len(tfq.rpms.data) == 3
    assert len(tfq.time_frequencies.data) == 7
    assert len(tfq.get_harmonic_indices().data) == 7
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.get_harmonic_indices().location == locations.time_freq
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose(
        [0.1, 0.21, 1.0, 1.1, 2.0, 0.23, 0.25], tfq.time_frequencies.data
    )
    assert np.allclose([2.0, 2.3, 3.0], tfq.rpms.data)
    assert tfq.complex_frequencies is None


def test_append_step_3():
    tfq = TimeFreqSupport()
    tfq.append_step(
        1,
        [0.1, 0.21],
        rpm_value=2.0,
        step_harmonic_indices={1: [1.0, 2.0], 2: [3.0, 3.1]},
    )
    assert len(tfq.rpms.data) == 1
    assert len(tfq.time_frequencies.data) == 2
    assert len(tfq.get_harmonic_indices(1).data) == 2
    assert len(tfq.get_harmonic_indices(2).data) == 2
    assert tfq.get_harmonic_indices() is None
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.get_harmonic_indices(1).location == locations.time_freq
    assert tfq.get_harmonic_indices(2).location == locations.time_freq
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose([1.0, 2.0], tfq.get_harmonic_indices(1).data)
    assert np.allclose([3.0, 3.1], tfq.get_harmonic_indices(2).data)
    assert tfq.complex_frequencies is None


def test_deep_copy_time_freq_support(velocity_acceleration):
    model = Model(velocity_acceleration)
    tf = model.metadata.time_freq_support
    copy = tf.deep_copy()
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert tf.time_frequencies.scoping.ids == copy.time_frequencies.scoping.ids


def test_deep_copy_time_freq_support_harmonic():
    model = Model(examples.download_multi_harmonic_result())
    tf = model.metadata.time_freq_support
    copy = tf.deep_copy()
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert tf.time_frequencies.scoping.ids == copy.time_frequencies.scoping.ids
    assert tf.time_frequencies.unit == copy.time_frequencies.unit
    assert np.allclose(tf.complex_frequencies.data, copy.complex_frequencies.data)
    assert tf.complex_frequencies.scoping.ids == copy.complex_frequencies.scoping.ids
    assert np.allclose(tf.rpms.data, copy.rpms.data)
    assert tf.rpms.scoping.ids == copy.rpms.scoping.ids


def test_deep_copy_time_freq_support_multi_stage():
    model = Model(examples.download_multi_stage_cyclic_result())
    tf = model.metadata.time_freq_support
    copy = tf.deep_copy()
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert tf.time_frequencies.scoping.ids == copy.time_frequencies.scoping.ids
    assert tf.time_frequencies.unit == copy.time_frequencies.unit
    assert np.allclose(
        tf.get_harmonic_indices(0).data, copy.get_harmonic_indices(0).data
    )
    assert (
        tf.get_harmonic_indices(0).scoping.ids
        == copy.get_harmonic_indices(0).scoping.ids
    )
    assert np.allclose(
        tf.get_harmonic_indices(1).data, copy.get_harmonic_indices(1).data
    )
    assert (
        tf.get_harmonic_indices(1).scoping.ids
        == copy.get_harmonic_indices(1).scoping.ids
    )

    assert len(tf.get_harmonic_indices(0).data) == 6
    assert len(tf.get_harmonic_indices(1).data) == 6
