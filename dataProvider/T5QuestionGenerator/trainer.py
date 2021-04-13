import pandas as pd

from simpletransformers.t5 import T5Model
import torch

if __name__ == '__main__':
    train_df = pd.read_csv("data/train_df_3.tsv", sep="\t").astype(str)
    eval_df = pd.read_csv("data/eval_df_3.tsv", sep="\t").astype(str)

    model_args = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "max_seq_length": 128,
        "train_batch_size": 1,
        "num_train_epochs": 1,
        "save_eval_checkpoints": True,
        "save_steps": -1,
        "use_multiprocessing": False,
        # "silent": True,
        "evaluate_during_training": True,
        "evaluate_during_training_steps": 1500,
        "evaluate_during_training_verbose": True,
        "fp16": False,
        "wandb_project": "Question Generation with T5",
    }

    model = T5Model("mt5", "google/mt5-small", use_cuda=False, args=model_args)

    if hasattr(torch.cuda, 'empty_cache'):
        torch.cuda.empty_cache()

    try:
        model.train_model(train_df, eval_data=eval_df)
    except:
        if hasattr(torch.cuda, 'empty_cache'):
            torch.cuda.empty_cache()
