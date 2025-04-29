# YOLO Model Comparison: 30 Epochs vs 60 Epochs

## Final Metrics Comparison

| Metric | 30 Epochs | 60 Epochs | Difference | Percent Change |
|--------|---------|---------|------------|---------------|
| Mean Average Precision (mAP@0.5) | 0.2105 | 0.1167 | -0.0937 | -44.54% |
| Precision | 0.2841 | 0.1039 | -0.1802 | -63.43% |
| Recall | 0.2500 | 0.2500 | 0.0000 | 0.00% |

## Training Curves

### Mean Average Precision (mAP@0.5)

![Mean Average Precision (mAP@0.5)](metrics_mAP_0.5_comparison.png)

### Precision

![Precision](metrics_precision_comparison.png)

### Recall

![Recall](metrics_recall_comparison.png)

### Box Loss

![Box Loss](train_box_loss_comparison.png)

### Object Loss

![Object Loss](train_obj_loss_comparison.png)

### Class Loss

![Class Loss](train_cls_loss_comparison.png)

### Validation Box Loss

![Validation Box Loss](val_box_loss_comparison.png)

### Validation Object Loss

![Validation Object Loss](val_obj_loss_comparison.png)

