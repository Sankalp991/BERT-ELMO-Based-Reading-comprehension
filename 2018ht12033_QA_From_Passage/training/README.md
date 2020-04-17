# BERT-SQuAD 

## Run

`run_squad.py`: Fine-tuning on SQuAD for question-answering

```bash
python -m torch.distributed.launch --nproc_per_node=8 ./training/run_squad.py \
    --model_type bert \
    --model_name_or_path bert-large-uncased-whole-word-masking \
    --do_train \
    --do_eval \
    --do_lower_case \
    --train_file ./training/train-v1.1.json \
    --predict_file ./training/dev-v1.1.json \
    --learning_rate 3e-5 \
    --num_train_epochs 3 \
    --max_seq_length 384 \
    --doc_stride 128 \
    --output_dir ../model/wwm_uncased_finetuned_squad/ \
    --per_gpu_eval_batch_size=8   \
    --per_gpu_train_batch_size=8   \
```
Training with these hyper-parameters gave us the following results:

```bash
{"exact_match": 73.609, "f1": 77.165}
```

