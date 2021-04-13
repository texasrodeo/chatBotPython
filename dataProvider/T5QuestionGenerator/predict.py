from simpletransformers.t5 import T5Model
import pandas as pd
from pprint import pprint
import torch
import codecs

if __name__ == '__main__':
    model_args = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "max_seq_length": 128,
        "eval_batch_size": 16,
        "num_train_epochs": 2,
        "save_eval_checkpoints": False,
        "use_multiprocessing": False,
        "num_beams": None,
        "do_sample": True,
        "max_length": 50,
        "top_k": 50,
        "top_p": 0.95,
        "num_return_sequences": 3,
    }

    if hasattr(torch.cuda, 'empty_cache'):
        torch.cuda.empty_cache()

    model = T5Model("t5", "outputs/best_model", args=model_args)

    df = pd.read_csv("data/eval_df_3.tsv", sep="\t").astype(str)

    if hasattr(torch.cuda, 'empty_cache'):
        torch.cuda.empty_cache()
    try:
        preds = model.predict(
            ["ask_question: " + description for description in df["input_text"].tolist()]
        )
        questions = df["target_text"].tolist()

        with codecs.open("outputs/generated_questions_sampling.txt", "w", "utf-8") as f:
            for i, desc in enumerate(df["input_text"].tolist()):
                pprint(desc)
                pprint(preds[i])
                print()

                f.write(str(desc) + "\n\n")

                f.write("Real question:\n")
                f.write(questions[i] + "\n\n")

                f.write("Generated questions:\n")
                for pred in preds[i]:
                    f.write(str(pred) + "\n")
                f.write("________________________________________________________________________________\n")
    except:
        if hasattr(torch.cuda, 'empty_cache'):
            torch.cuda.empty_cache()
