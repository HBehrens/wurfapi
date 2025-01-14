import pyquery
import os
import pprint
import mock
import logging

import wurfapi
import wurfapi.doxygen_parser
import wurfapi.doxygen_generator
import wurfapi.doxygen_downloader
import wurfapi.run

import record


def generate_coffee_xml(testdirectory):
    """ Test helper - generate the XML. """

    output_dir = testdirectory.mkdir('xml_output')
    coffee_dir = testdirectory.copy_dir('test/data/cpp_coffee')
    src_dirs = [os.path.join(coffee_dir.path(), 'src'), os.path.join(
        coffee_dir.path(), 'examples', 'header', 'header.h')]

    doxygen_executable = wurfapi.doxygen_downloader.ensure_doxygen()

    generator = wurfapi.doxygen_generator.DoxygenGenerator(
        doxygen_executable=doxygen_executable,
        runner=wurfapi.run,
        recursive=True,
        source_paths=src_dirs,
        output_path=output_dir.path(),
        warnings_as_error=True)

    return coffee_dir.path(), src_dirs, generator.generate()


def test_coffee(testdirectory, caplog):

    caplog.set_level(logging.DEBUG)

    coffee_dir, src_dirs, xml_dir = generate_coffee_xml(testdirectory)
    log = logging.getLogger(name='test_coffee')

    mapper = wurfapi.location_mapper.LocationMapper(
        project_root=coffee_dir, include_paths=[], log=log)

    parser = wurfapi.doxygen_parser.DoxygenParser(
        doxygen_path=xml_dir,
        location_mapper=mapper,
        # Patch fix Doxygen bug reported here:
        # https://bit.ly/2BWPllZ
        patch_api=[
            {'selector': 'project::v1_0_0::coffee::machine::impl',
             'key': 'access', 'value': 'private'}],
        log=log)

    api = parser.parse_index()

    mismatch_path = testdirectory.mkdir('mismatch')

    recorder = record.Record(
        filename='coffee.json',
        recording_path='test/data/parser_recordings',
        mismatch_path=mismatch_path.path())

    recorder.record(data=api)


def generate_xml(testdirectory, source_file):
    """ Test helper - generate the XML. """

    output_dir = testdirectory.mkdir('xml_output')
    source_dir = testdirectory.mkdir('sources')
    source_dir.copy_file(source_file)

    doxygen_executable = wurfapi.doxygen_downloader.ensure_doxygen()

    generator = wurfapi.doxygen_generator.DoxygenGenerator(
        doxygen_executable=doxygen_executable,
        runner=wurfapi.run,
        recursive=True,
        source_paths=[source_dir.path()],
        output_path=output_dir.path(),
        warnings_as_error=True)

    return source_dir.path(), generator.generate()


def test_parser_input_function(testdirectory, caplog):

    caplog.set_level(logging.DEBUG)

    src_dir, xml_dir = generate_xml(
        testdirectory,
        source_file='test/data/parser_input/function.hpp')

    log = logging.getLogger(name='test_parser_input_function')

    mapper = wurfapi.location_mapper.LocationMapper(
        project_root=src_dir, include_paths=[], log=log)

    parser = wurfapi.doxygen_parser.DoxygenParser(
        doxygen_path=xml_dir,
        location_mapper=mapper,
        patch_api=[],
        log=log)

    api = parser.parse_index()

    mismatch_path = testdirectory.mkdir('mismatch')

    recorder = record.Record(
        filename='parser_input_function.json',
        recording_path='test/data/parser_recordings',
        mismatch_path=mismatch_path.path())

    recorder.record(data=api)


def test_parser_input_enum_class(testdirectory, caplog):

    caplog.set_level(logging.DEBUG)

    src_dir, xml_dir = generate_xml(
        testdirectory,
        source_file='test/data/parser_input/enum_class.hpp')

    log = logging.getLogger(name='test_parser_input_enum_class')

    mapper = wurfapi.location_mapper.LocationMapper(
        project_root=src_dir, include_paths=[], log=log)

    parser = wurfapi.doxygen_parser.DoxygenParser(
        doxygen_path=xml_dir,
        location_mapper=mapper,
        patch_api=[],
        log=log)

    api = parser.parse_index()

    mismatch_path = testdirectory.mkdir('mismatch')

    recorder = record.Record(
        filename='parser_input_enum_class.json',
        recording_path='test/data/parser_recordings',
        mismatch_path=mismatch_path.path())

    recorder.record(data=api)


def test_parser_input_variables(testdirectory, caplog):

    caplog.set_level(logging.DEBUG)

    src_dir, xml_dir = generate_xml(
        testdirectory,
        source_file='test/data/parser_input/variables.hpp')

    log = logging.getLogger(name='test_parser_input_variables')

    mapper = wurfapi.location_mapper.LocationMapper(
        project_root=src_dir, include_paths=[], log=log)

    parser = wurfapi.doxygen_parser.DoxygenParser(
        doxygen_path=xml_dir,
        location_mapper=mapper,
        patch_api=[],
        log=log)

    api = parser.parse_index()

    mismatch_path = testdirectory.mkdir('mismatch')

    recorder = record.Record(
        filename='parser_input_variables.json',
        recording_path='test/data/parser_recordings',
        mismatch_path=mismatch_path.path())

    recorder.record(data=api)


def test_parser_input_type_definitions(testdirectory, caplog):

    caplog.set_level(logging.DEBUG)

    src_dir, xml_dir = generate_xml(
        testdirectory,
        source_file='test/data/parser_input/type_definitions.hpp')

    log = logging.getLogger(name='test_parser_input_type_definitions')

    mapper = wurfapi.location_mapper.LocationMapper(
        project_root=src_dir, include_paths=[], log=log)

    parser = wurfapi.doxygen_parser.DoxygenParser(
        doxygen_path=xml_dir,
        location_mapper=mapper,
        patch_api=[],
        log=log)

    api = parser.parse_index()

    mismatch_path = testdirectory.mkdir('mismatch')

    recorder = record.Record(
        filename='parser_input_type_definitions.json',
        recording_path='test/data/parser_recordings',
        mismatch_path=mismatch_path.path())

    recorder.record(data=api)


def test_parser_input_templates(testdirectory, caplog):

    caplog.set_level(logging.DEBUG)

    src_dir, xml_dir = generate_xml(
        testdirectory,
        source_file='test/data/parser_input/templates.hpp')

    log = logging.getLogger(name='test_parser_templates')

    mapper = wurfapi.location_mapper.LocationMapper(
        project_root=src_dir, include_paths=[], log=log)

    parser = wurfapi.doxygen_parser.DoxygenParser(
        doxygen_path=xml_dir,
        location_mapper=mapper,
        patch_api=[],
        log=log)

    api = parser.parse_index()

    mismatch_path = testdirectory.mkdir('mismatch')

    recorder = record.Record(
        filename='parser_input_templates.json',
        recording_path='test/data/parser_recordings',
        mismatch_path=mismatch_path.path())

    recorder.record(data=api)


def test_parser_replace_with():

    data_in = {
        'a': {'b': 'replace', 'c': ['replace', {'a': 'replace'}]}
    }

    data_out = wurfapi.doxygen_parser.replace_with(
        {'replace': 'with'}, data_in
    )

    data_expect = {
        'a': {'b': 'with', 'c': ['with', {'a': 'with'}]}
    }

    assert data_out == data_expect


def test_parse_using_type():

    test = "using project::coffee::machine::callback =  std::function<void()>"

    result = wurfapi.doxygen_parser.parse_using_type(definition=test)

    assert result == "std::function<void()>"


def test_parse_variable_type():

    # Test
    variable_type = [{'value': 'constexpr', 'link': None},
                     {'value': 'int', 'link': None}]

    result_type, is_const, is_constexpr = wurfapi.doxygen_parser.parse_variable_type(
        variable_type=variable_type)

    assert result_type == [{'value': 'int', 'link': None}]
    assert is_const == False
    assert is_constexpr == True

    # Test
    variable_type = [{'value': 'static', 'link': None},
                     {'value': ' constexpr ', 'link': None},
                     {'value': 'int', 'link': None}]

    result_type, is_const, is_constexpr = wurfapi.doxygen_parser.parse_variable_type(
        variable_type=variable_type)

    assert result_type == [{'value': 'static', 'link': None},
                           {'value': ' ', 'link': None},
                           {'value': 'int', 'link': None}]
    assert is_const == False
    assert is_constexpr == True

    # Test
    variable_type = [{'value': ' sdfs_constexpr ', 'link': None},
                     {'value': 'int', 'link': None}]

    result_type, is_const, is_constexpr = wurfapi.doxygen_parser.parse_variable_type(
        variable_type=variable_type)

    assert result_type == variable_type
    assert is_const == False
    assert is_constexpr == False

    # Test
    variable_type = [{'value': ' constexpr_dsf ', 'link': None},
                     {'value': 'int', 'link': None}]

    result_type, is_const, is_constexpr = wurfapi.doxygen_parser.parse_variable_type(
        variable_type=variable_type)

    assert result_type == variable_type
    assert is_const == False
    assert is_constexpr == False

    # Test
    variable_type = [{'value': 'static constexpr unsigned ', 'link': None},
                     {'value': 'int', 'link': None}]

    result_type, is_const, is_constexpr = wurfapi.doxygen_parser.parse_variable_type(
        variable_type=variable_type)

    assert result_type == [{'value': 'static unsigned ', 'link': None},
                           {'value': 'int', 'link': None}]
    assert is_const == False
    assert is_constexpr == True


def test_parser_input_inline_namespace(testdirectory, caplog, datarecorder):

    caplog.set_level(logging.DEBUG)

    src_dir, xml_dir = generate_xml(
        testdirectory,
        source_file='test/data/parser_input/inline_namespace.hpp')

    log = logging.getLogger(name='test_parser_inline_namespace')

    mapper = wurfapi.location_mapper.LocationMapper(
        project_root=src_dir, include_paths=[], log=log)

    parser = wurfapi.doxygen_parser.DoxygenParser(
        doxygen_path=xml_dir,
        location_mapper=mapper,
        patch_api=[],
        log=log)

    data = parser.parse_index()

    datarecorder.recording_path = os.path.join(
        "test/data/parser_recordings/parser_input_inline_namespace.json")

    datarecorder.record(data=data)
