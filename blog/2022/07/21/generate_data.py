import csv
import json

with open("data/output.csv", "w") as output_file:
    writer = csv.writer(output_file, delimiter=",", lineterminator="\n")
    writer.writerow(["timestamp_field","json_field"])
    writer.writerow([
        760530903363,
        json.dumps(json.dumps({"id": 7886, "details": {"collaborator": "Brett Gill", "score": 6056, "address": "2882 Sheila Lakes Apt. 264\nRhondaville, KS 09803"}}))
    ])