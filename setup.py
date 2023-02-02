from distutils.core import setup

setup(
    name='peakrdl_format_trans',
    version='0.0.1',
    author='jiangqingliu',
    author_email='jiangqingliu822@gmail.com',
    url='https://github.com/jiangqingliu88/peakrdl_format_trans',
    description="Import csv/xlxs transfer to systemrdl file",
    license='LICENSE',
    packages=['peakrdl_format_trans'],
    package_dir={'': 'peakrdl_format_trans'},
    packages=[
        "peakrdl_format_trans",
    ],
    include_package_data=True,
    description='An example of extern peakrdl Python package.',
    entry_points = {
        "peakrdl.exporters": [
            'formattrans = peakrdl_format_trans.__peakrdl__:MyExporterDescriptor'
        ],
        "peakrdl.exporters": [
            'formattrans = peakrdl_format_trans.__peakrdl__:MyExporterDescriptor'
        ],
    },
    install_requires=[
        # 'python>=3.6.0',
        # 'pandas>=0.10.0'
    ],
)
