import kfp

from  kfp.v2.dsl import(
    Artifact,
    Input,
    Output,
    Metrics,
    component
)

import json

from components.data_ingest_component import ingest_data_component

from kfp.v2 import compiler

import sys

from typing import Callable

def pipeline_func(data:dict,enable_caching:bool=False):
    
    @kfp.dsl.pipeline(name='xyz-pipeline',pipeline_root=data['PIPELINE_ROOT'])

    def pipeline(
        data_path:str=data['data_source']
    ):
        data_ingest=(
            ingest_data_component(data_path).set_cpu_request('64').set_memory_request('416G').set_caching_options(False))
    return pipeline
    

def final_pipeline(config:str,callback:Callable[[str,str],None]=None,enable_caching:bool=False):

    with open(config,'r') as file:
        data=json.load(file)

    pipeline=pipeline_func(data,enable_caching)

    if callable(pipeline):
        compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path=data['PIPELINE_JSON']
    )
    else:
        print("Error: pipeline_func did not return a callable pipeline")


    if callback is not None:
        callback(data['REGION'],data['PIPELINE_ROOT'])

if __name__=='__main__':
    final_pipeline(str(sys.argv[1]))
