from setuptools import setup 
setup(
    name= "data1mathieutremblay",
    version="0.2",
    scripts=['home_work_data1.py'],
data_files= [('.',['data-1.csv'])],

install_requires=['matplotlib','pandas'],

author="Mathieu tremblay",
Author_email="mattremblay76@gmail.com",
description="This is an Example Package",
keywords="data1 mathieu tremblay"
)
