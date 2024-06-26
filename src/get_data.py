## read params
## process
## return dataframe
import os
import yaml
import pandas as pd
import argparse

params_path = "D:\wtl_musicreco\params.yaml"

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config
    

def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",",encoding='utf-8')
    feature_path = config["data_source"]["feature_source"]
    feature_df = pd.read_csv(feature_path,sep=",",encoding='utf-8')
    return df,feature_df

# extra comment
    
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default=params_path)
    parsed_args = args.parse_args()
    data = read_params(config_path=parsed_args.config)
    print(data)