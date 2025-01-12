from Decal import Decal_exp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--kg", type=str, default='')

args = parser.parse_args()

path_main = "../decal-embeddings/main.py"
folder_name = f"Experiments_{args.kg}"
Experiments_path=f"../decal-embeddings/Experiments_{args.kg}"
path_dataset = f"../decal-embeddings/KGs/{args.kg}"

dat = Decal_exp(emb_dim=16,path_main = path_main,folder_name = folder_name,Experiments_path=Experiments_path,\
               num_epochs=250,batch_size=1024, scoring_technique= "KvsAll",path_dataset=path_dataset)

params_values = range(16)
df = dat.GSDC(params_values)
df.to_csv(f'GSDC_{args.kg}.csv',index=False)