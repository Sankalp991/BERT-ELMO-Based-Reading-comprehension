import csv
import json
import random

bert_file_name = 'training/trained_files/bert_model.csv'
bidaf_file_name = 'training/trained_files/bidaf_model.csv'

with open('training/trained_files/ensembled.csv', 'w', newline='', encoding='utf-8') as csv_fh:
    csv_writer = csv.writer(csv_fh, delimiter=',')
    csv_writer.writerow(['Id', 'Predicted'])

    with open(bert_file_name,encoding='utf-8') as baseline:
        with open(bidaf_file_name,encoding='utf-8') as model:
            # read_baseline = sorted(csv.reader(baseline, delimiter = ','), key = lambda row: row[0])
            # read_model = sorted(csv.reader(model, delimiter = ','), key = lambda row: row[0])

            read_baseline = csv.reader(baseline, delimiter=',')
            read_model = csv.reader(model, delimiter=',')

            baseline_dict = {}
            model_dict = {}

            for row in read_model:
                model_dict[row[0]] = row[1]

            for row in read_baseline:
                baseline_dict[row[0]] = row[1]

            for key in model_dict:
                if key in baseline_dict:
                    if baseline_dict[key] == model_dict[key]:
                        csv_writer.writerow([key, baseline_dict[key]])
                    else:
                        if random.random() <= 0.02:
                            csv_writer.writerow([key, baseline_dict[key]])
                        else:
                            csv_writer.writerow([key, model_dict[key]])