from pandas import read_csv
from torch import from_numpy
import sys
sys.path.append('..')  
from src.utils import constants

class RawDataReader():
    def __init__(self) -> None:
        self.lables_file = 'labels_train.csv'
        
        self.raw_data_dir = constants.RAW_DATA_DIR 
        self.rs = list(range(constants.MIN_R, constants.MAX_R+1))

    def __get_labels_path(self):
        return f'{self.raw_data_dir}/{self.lables_file}'
    
    def __get_dataset_path(self, r):
        return f'{self.raw_data_dir}/R{r}_train.csv'
    
    def __load_data(self, file):
        return read_csv(file)
    
    def get_labels(self):
        return from_numpy(self.__load_data(self.__get_labels_path()).to_numpy()).float()
    
    def get_datasets(self):
        return {
            r: from_numpy(self.__load_data(self.__get_dataset_path(r)).to_numpy()).float()
            for r in self.rs
        }

    def get_normalised_dataset(self):
        r_dfs = self.get_datasets()
        means = {
            r: r_dfs[r].mean(dim=0)
            for r in r_dfs
        }
        stds = {
            r: r_dfs[r].std(dim=0)
            for r in r_dfs
        }
        norm_datasets = {
            r: (r_dfs[r] - means[r]) / stds[r]
            for r in r_dfs
        }
        return norm_datasets, means, stds
