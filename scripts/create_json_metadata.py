import os
import json
import uuid

def create_json_metadata(text_file, doc_uuid, title, date_written, location, author, author_role, recipient, doc_type, subject_tags, summary):
    metadata = {
        "document_uuid": doc_uuid,
        "title": title,
        "date_written": date_written,
        "location": location,
        "author": author,
        "author_role": author_role,
        "recipient": recipient,
        "type": doc_type,
        "subject_tags": subject_tags,
        "summary": summary,
        "text_file": text_file
    }
    
    json_filename = text_file.replace('.txt', '.json')
    json_filepath = os.path.join(output_dir, json_filename)
    
    with open(json_filepath, 'w') as json_file:
        json.dump(metadata, json_file, indent=4)

# Define metadata for each text file
documents_metadata = [
    {
        "text_file": "9.1.1.1 April 18 1861.txt",
        "doc_uuid": "7d3ccb24-5a40-4690-a8ed-a52d3417c308",
        "title": "Report of First Lieut. R. Jones, April 18, 1861",
        "date_written": "April 18, 1861",
        "location": "Harper’s Ferry, Va.",
        "author": "First Lieut. R. Jones",
        "author_role": "Mounted Rifles, U.S. Army",
        "recipient": "Assistant Adjutant-General, Headquarters of the Army, Washington, D.C.",
        "doc_type": "Military Report",
        "subject_tags": [
            "Arsenal and Armament",
            "Harper’s Ferry",
            "Military Readiness",
            "Arsenal Destruction",
            "Troop Movements",
            "Communication with General Scott",
            "Personnel Movements",
            "Intelligence and Reconnaissance",
            "Infrastructure and Logistics",
            "Engagements and Skirmishes"
        ],
        "summary": "Lieutenant R. Jones reports from Harper’s Ferry on the eve of April 18, 1861, detailing preparations and defensive actions in anticipation of an attack aimed at seizing government property. The report highlights the strategic significance of the location, the measures taken to destroy the arsenal if necessary, and the urgent request for reinforcements."
    },
    {
        "text_file": "9.1.1.2 April 19 1861.txt",
        "doc_uuid": "5350521d-cd3f-4cee-8e82-5361af26eb87",
        "title": "Report of First Lieut. R. Jones, April 19, 1861",
        "date_written": "April 19, 1861",
        "location": "Chambersburg, Pa.",
        "author": "First Lieut. R. Jones",
        "author_role": "Mounted Rifles, U.S. Army",
        "recipient": "General Winfield Scott",
        "doc_type": "Military Report",
        "subject_tags": [
            "Harper’s Ferry",
            "Arsenal and Armament",
            "Evacuation",
            "Military Strategy",
            "Retreat"
        ],
        "summary": "Lieutenant R. Jones reports from Chambersburg on April 19, 1861, describing the destruction of the arsenal and the armory buildings at Harper’s Ferry under cover of night and the subsequent retreat of his command."
    },
    # Add other documents here following the same structure
]

volume = "Volume2"
chapter = "Chapter9"
output_dir = '/mnt/data/Volume2_Chapter9_Metadata'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for doc in documents_metadata:
    create_json_metadata(**doc)

print("JSON metadata files created successfully.")
