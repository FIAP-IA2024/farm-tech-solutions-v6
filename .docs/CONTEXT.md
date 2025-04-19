# Project Context

## Project Overview

Academic project for FIAP focused on solutions for the agricultural sector using computer vision. The data consists of labeled images with corresponding `.txt` files, stored in `/data`.

## Dataset

### Organization

The dataset has been reorganized in YOLO format with the following structure:

```plaintext
data/  
├── train/  
│   ├── images/  (64 images: 32 of Object A, 32 of Object B)  
│   └── labels/  (64 corresponding label files)  
├── val/  
│   ├── images/  (8 images: 4 of Object A, 4 of Object B)  
│   └── labels/  (8 corresponding label files)  
└── test/  
    ├── images/  (8 images: 4 of Object A, 4 of Object B)  
    └── labels/  (8 corresponding label files)  
```

### Proper Data Distribution

- 80% of the dataset allocated to training (64 images)  
- 10% allocated to validation (8 images)  
- 10% allocated to testing (8 images)  
- Balanced representation of Object A and B maintained in each split  

## Development

### Current Progress

- Dataset organized and labeled locally.
- Task structure created in `/docs/tasks`.
- Task 1 (dataset organization) completed.
- Task 2 (dataset splitting) completed.

### Completed Tasks

- 0001-dataset_organization.md
- 0002-dataset_splitting.md

### Important Notes

- Execution is being done locally before migrating to Google Colab.
- The original `CONTEXT.md` file was renamed to `PROJECT.md`.

### Last Updated

2025-04-19T18:01:55-03:00
