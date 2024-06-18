# Official Records of the American Civil War Dataset

## Project Overview

This project involves organizing, digitizing, structuring, and annotating the 128 volumes of the Official Records of the American Civil War. The goal is to create a comprehensive and analyzable dataset that supports detailed historical research and analysis.

## Folder Structure

The project directory is organized as follows:

dataset-civil_war_records/
├── .devcontainer/
│   └── devcontainer.json
├── Original Texts/
│   ├── Volume 1/
│   ├── Volume 2/
│   │   └── The War of the Rebellion Volume 2 Chapter 9.txt
│   ├── Volume 3/
├── UUIDs.txt
├── requirements.txt
├── README.md
└── scripts/
    ├── split_and_create_files.py
    ├── create_json_metadata.py
└── script_test_output/

## Setup and Installation

### Prerequisites

- Docker
- Visual Studio Code
- Remote - Containers extension for VS Code

### Steps to Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AdmiralEM/dataset-civil_war_records.git
    cd dataset-civil_war_records
    ```

2. **Open the project in VS Code**:
    ```bash
    code .
    ```

3. **Reopen in Container**:
    Press `Ctrl+Shift+P`, select `Remote-Containers: Reopen in Container`.

4. **Install Python dependencies**:
    Dependencies are automatically installed in the virtual environment defined in the `.devcontainer/devcontainer.json` file.

## Usage

### Splitting and Creating Files

The script `split_and_create_files.py` is used to split the original text files into individual documents and create corresponding JSON metadata files.

#### Example Usage

1. **Run the script**:
    ```bash
    python scripts/split_and_create_files.py
    ```

2. **Input and Output**:
    - **Input**: Original text files located in `Original Texts/Volume 2/`
    - **Output**: Split text files and JSON metadata files are saved in `script_test_output/`

### JSON Metadata

Each split document has a corresponding JSON metadata file that includes:

- **UUID**: Unique identifier
- **Title**: Title of the document
- **Date Written**: Date the document was written
- **Location**: Location from where the document was written
- **Author**: Author of the document
- **Author Role**: Role of the author
- **Recipient**: Recipient of the document
- **Subject Tags**: Tags related to the content
- **Summary**: Brief summary of the document
- **Text File**: Name of the text file

### Example JSON Metadata

```json
{
  "document_uuid": "5350521d-cd3f-4cee-8e82-5361af26eb87",
  "title": "Report of First Lieut. R. Jones, April 19, 1861",
  "date_written": "April 19, 1861",
  "location": "Chambersburg, Pa.",
  "author": "First Lieut. R. Jones",
  "author_role": "Mounted Rifles, U.S. Army",
  "recipient": "General Winfield Scott",
  "type": "Military Report",
  "subject_tags": [
    "Harper’s Ferry",
    "Arsenal and Armament",
    "Evacuation",
    "Military Strategy",
    "Retreat"
  ],
  "summary": "Lieutenant R. Jones reports from Chambersburg on April 19, 1861, describing the destruction of the arsenal and the armory buildings at Harper’s Ferry under cover of night and the subsequent retreat of his command.",
  "text_file": "9.1.1.2 April 19 1861.txt"
}
