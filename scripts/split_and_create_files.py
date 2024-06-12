import os
import re
import uuid

def split_transcript(volume, transcript_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(transcript_path, 'r') as file:
        text = file.read()
    
    document_pattern = re.compile(r'(No\. \d+\.|REPORTS, ETC\.)')
    documents = document_pattern.split(text)
    
    doc_index = 0
    for i in range(1, len(documents), 2):
        doc_header = documents[i].strip()
        doc_content = documents[i+1].strip()
        
        doc_uuid = str(uuid.uuid4())
        document_id = f"{volume}_Doc{doc_index}_{doc_uuid}"
        document_path = os.path.join(output_dir, f"{document_id}.txt")
        
        with open(document_path, 'w') as doc_file:
            doc_file.write(f"{doc_header}\n{doc_content}")
        
        create_json_metadata(volume, document_id, doc_header, doc_uuid, output_dir)
        doc_index += 1

def create_json_metadata(volume, document_id, doc_header, doc_uuid, output_dir):
    metadata = {
        "document_uuid": doc_uuid,
        "document_id": document_id,
        "type": "Report" if "Report" in doc_header else "Letter",
        "author": extract_author(doc_header),
        "date_written": extract_date(doc_header),
        "recipient": extract_recipient(doc_header),
        "subject_tags": extract_tags(doc_header),
        "text_file": f"{document_id}.txt"
    }
    
    json_path = os.path.join(output_dir, f"{document_id}.json")
    
    with open(json_path, 'w') as json_file:
        json.dump(metadata, json_file, indent=4)

def extract_author(header):
    return "Unknown Author"

def extract_date(header):
    return "Unknown Date"

def extract_recipient(header):
    return "Unknown Recipient"

def extract_tags(header):
    return []

# Example usage
split_transcript('Volume2', '/path/to/Volume2_transcript.txt', '/output/directory')
