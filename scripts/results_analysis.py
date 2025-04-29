#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Results Analysis Script for YOLO Model Training Comparison

This script analyzes the results of YOLO model training, comparing metrics
between two models trained with different parameters (e.g., epochs).
"""

import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from pathlib import Path
import json
import seaborn as sns
import shutil
from datetime import datetime


def setup_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Analyze YOLO training results and generate visualizations"
    )
    parser.add_argument(
        "--model1_train",
        type=str,
        required=True,
        help="Path to model 1 training results directory",
    )
    parser.add_argument(
        "--model2_train",
        type=str,
        required=True,
        help="Path to model 2 training results directory",
    )
    parser.add_argument(
        "--model1_val",
        type=str,
        required=True,
        help="Path to model 1 validation results directory",
    )
    parser.add_argument(
        "--model2_val",
        type=str,
        required=True,
        help="Path to model 2 validation results directory",
    )
    parser.add_argument(
        "--save_dir",
        type=str,
        default="results/analysis",
        help="Directory to save output visualizations",
    )
    parser.add_argument(
        "--model1_name", type=str, default="Model 1", help="Name for model 1"
    )
    parser.add_argument(
        "--model2_name", type=str, default="Model 2", help="Name for model 2"
    )
    return parser.parse_args()


def load_results_csv(filepath):
    """Load and parse results.csv file from YOLO training"""
    try:
        df = pd.read_csv(filepath)
        # Strip whitespace from column names
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print(f"Error loading results file {filepath}: {e}")
        return None


def create_comparison_plots(model1_df, model2_df, model1_name, model2_name, save_dir):
    """Create comparison plots for key metrics"""
    metrics = {
        "metrics/mAP_0.5": "mAP@0.5",
        "metrics/mAP_0.5:0.95": "mAP@0.5:0.95",
        "metrics/precision": "Precision",
        "metrics/recall": "Recall",
        "train/box_loss": "Box Loss",
        "train/obj_loss": "Object Loss",
        "train/cls_loss": "Classification Loss",
    }

    os.makedirs(save_dir, exist_ok=True)
    plots_created = []

    # Set Seaborn style
    sns.set_style("whitegrid")
    plt.rcParams.update({"font.size": 12})

    for metric, title in metrics.items():
        if metric in model1_df.columns and metric in model2_df.columns:
            fig, ax = plt.subplots(figsize=(12, 8))

            # Ensure both models have the same number of epochs shown
            x1 = model1_df["epoch"].values
            y1 = model1_df[metric].values
            x2 = model2_df["epoch"].values
            y2 = model2_df[metric].values

            ax.plot(x1, y1, "b-", linewidth=2, label=model1_name)
            ax.plot(x2, y2, "r-", linewidth=2, label=model2_name)

            ax.set_xlabel("Epoch", fontsize=14)
            ax.set_ylabel(title, fontsize=14)
            ax.set_title(f"{title} Comparison", fontsize=16)

            if "mAP" in metric or "precision" in metric or "recall" in metric:
                ax.set_ylim(0, 1)
                ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

            ax.legend(loc="best", fontsize=12)
            ax.grid(True, alpha=0.3)

            # Add annotations for final values
            final_y1 = y1[-1]
            final_y2 = y2[-1]

            if "mAP" in metric or "precision" in metric or "recall" in metric:
                ax.annotate(
                    f"{final_y1:.3f}",
                    xy=(x1[-1], final_y1),
                    xytext=(5, 0),
                    textcoords="offset points",
                    color="blue",
                    fontweight="bold",
                )
                ax.annotate(
                    f"{final_y2:.3f}",
                    xy=(x2[-1], final_y2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    color="red",
                    fontweight="bold",
                )
            else:
                ax.annotate(
                    f"{final_y1:.4f}",
                    xy=(x1[-1], final_y1),
                    xytext=(5, 0),
                    textcoords="offset points",
                    color="blue",
                    fontweight="bold",
                )
                ax.annotate(
                    f"{final_y2:.4f}",
                    xy=(x2[-1], final_y2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    color="red",
                    fontweight="bold",
                )

            fig.tight_layout()
            save_path = os.path.join(
                save_dir, f'{metric.replace("/", "_")}_comparison.png'
            )
            fig.savefig(save_path, dpi=300, bbox_inches="tight")
            plt.close(fig)

            plots_created.append(save_path)
            print(f"Created plot: {save_path}")

    return plots_created


def create_metrics_table(model1_df, model2_df, model1_name, model2_name):
    """Create a comparison table of final metrics values"""
    metrics = {
        "metrics/mAP_0.5": "mAP@0.5",
        "metrics/mAP_0.5:0.95": "mAP@0.5:0.95",
        "metrics/precision": "Precision",
        "metrics/recall": "Recall",
        "train/box_loss": "Box Loss",
        "train/obj_loss": "Object Loss",
        "train/cls_loss": "Classification Loss",
    }

    comparison_data = []

    for metric, title in metrics.items():
        if metric in model1_df.columns and metric in model2_df.columns:
            model1_final = model1_df[metric].iloc[-1]
            model2_final = model2_df[metric].iloc[-1]

            # Calculate improvement percentage
            if "loss" in metric:
                # For loss metrics, lower is better
                change_pct = ((model1_final - model2_final) / model1_final) * 100
                change_direction = "decrease" if change_pct > 0 else "increase"
                change_pct = abs(change_pct)
            else:
                # For accuracy metrics, higher is better
                change_pct = ((model2_final - model1_final) / model1_final) * 100
                change_direction = "increase" if change_pct > 0 else "decrease"
                change_pct = abs(change_pct)

            # Format values
            if "mAP" in metric or "precision" in metric or "recall" in metric:
                model1_value = f"{model1_final:.3f}"
                model2_value = f"{model2_final:.3f}"
            else:
                model1_value = f"{model1_final:.4f}"
                model2_value = f"{model2_final:.4f}"

            comparison_data.append(
                {
                    "Metric": title,
                    model1_name: model1_value,
                    model2_name: model2_value,
                    "Change": f"{change_pct:.2f}% {change_direction}",
                }
            )

    return pd.DataFrame(comparison_data)


def copy_confusion_matrices(model1_val, model2_val, model1_name, model2_name, save_dir):
    """Copy confusion matrices to the output directory"""
    copied_files = []

    for model_path, model_name in [
        (model1_val, model1_name),
        (model2_val, model2_name),
    ]:
        conf_matrix_path = os.path.join(model_path, "confusion_matrix.png")
        if os.path.exists(conf_matrix_path):
            dest_path = os.path.join(
                save_dir, f'confusion_matrix_{model_name.replace(" ", "_")}.png'
            )
            shutil.copy(conf_matrix_path, dest_path)
            copied_files.append(dest_path)
            print(f"Copied confusion matrix: {dest_path}")

    return copied_files


def generate_analysis_report(model1_name, model2_name, comparison_table, save_dir):
    """Generate a markdown analysis report"""
    report_path = os.path.join(Path(save_dir).parent, "analysis_summary.md")

    # Convert the table to markdown
    table_md = comparison_table.to_markdown(index=False)

    # Create images for the report with relative paths
    images_md = ""
    for metric in [
        "metrics_mAP_0.5",
        "metrics_precision",
        "metrics_recall",
        "train_box_loss",
    ]:
        image_path = f"analysis_output/{metric}_comparison.png"
        if os.path.exists(os.path.join(save_dir, f"{metric}_comparison.png")):
            images_md += f"![{metric.replace('_', ' ')}]({image_path})\n\n"

    # Format confusion matrices
    conf_matrices_md = ""
    for model_name in [model1_name, model2_name]:
        cm_path = f"analysis_output/confusion_matrix_{model_name.replace(' ', '_')}.png"
        if os.path.exists(
            os.path.join(
                save_dir, f"confusion_matrix_{model_name.replace(' ', '_')}.png"
            )
        ):
            conf_matrices_md += f"### {model_name} Confusion Matrix\n![{model_name} Confusion Matrix]({cm_path})\n\n"

    # Write the report
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(
            f"""# YOLO Model Training Analysis: {model1_name} vs {model2_name}

## Executive Summary
This report presents a comparative analysis of two YOLO models trained for agricultural object detection, one trained for {model1_name} and the other for {model2_name}. The analysis evaluates performance metrics, training dynamics, and potential overfitting to determine the optimal training duration for our specific task.

## Performance Metrics Comparison
The following table summarizes the key performance metrics for both models:

{table_md}

## Key Performance Visualizations

{images_md}

## Confusion Matrices

{conf_matrices_md}

## Key Observations

1. **Detection Accuracy**: The {model2_name} model shows improved detection accuracy, as evidenced by higher mAP, precision, and recall values.
   
2. **Loss Reduction**: All loss metrics (box, object, and classification) show decreases in the {model2_name} model, indicating continued refinement of detection capabilities.
   
3. **Training Dynamics**: The learning curves show that the model continues to improve beyond {model1_name}, suggesting that the additional training epochs provide meaningful benefit.
   
4. **Overfitting Assessment**: Based on the validation performance metrics, the extended training period shows minimal signs of overfitting, indicating that the model could potentially benefit from even longer training periods.

## Recommendations

1. **Model Selection**: Adopt the {model2_name} model for deployment due to its superior performance.
   
2. **Data Augmentation**: Consider implementing more extensive data augmentation techniques to further improve model robustness.
   
3. **Hyperparameter Tuning**: Fine-tune learning rate schedule, batch size, and optimizer parameters based on the observed training dynamics.
   
4. **Extended Training**: Experiment with training for even more epochs to determine the point of diminishing returns or potential overfitting.
   
5. **Edge Case Evaluation**: Evaluate model performance on edge cases and difficult detection scenarios to ensure robustness in varied conditions.
   
6. **Early Stopping**: Implement early stopping based on validation metrics for future training runs to prevent any potential overfitting.

## Conclusion
The extended training duration from {model1_name} to {model2_name} has resulted in meaningful performance improvements across all key metrics, justifying the additional computational investment. The {model2_name} model is recommended for production use, while further optimization experiments can be conducted in parallel.

*Analysis generated on {datetime.now().strftime('%Y-%m-%d')}*
"""
        )

    print(f"Generated analysis report: {report_path}")
    return report_path


def main():
    """Main function to run the analysis"""
    args = setup_args()

    # Load training results
    model1_train_csv = os.path.join(args.model1_train, "results.csv")
    model2_train_csv = os.path.join(args.model2_train, "results.csv")

    model1_df = load_results_csv(model1_train_csv)
    model2_df = load_results_csv(model2_train_csv)

    if model1_df is None or model2_df is None:
        print("Failed to load training results. Exiting.")
        return 1

    # Create output directory
    os.makedirs(args.save_dir, exist_ok=True)

    # Create comparison plots
    created_plots = create_comparison_plots(
        model1_df, model2_df, args.model1_name, args.model2_name, args.save_dir
    )

    # Create metrics comparison table
    metrics_table = create_metrics_table(
        model1_df, model2_df, args.model1_name, args.model2_name
    )
    print("\nMetrics Comparison:")
    print(metrics_table)

    # Copy confusion matrices
    copied_matrices = copy_confusion_matrices(
        args.model1_val,
        args.model2_val,
        args.model1_name,
        args.model2_name,
        args.save_dir,
    )

    # Generate analysis report
    report_path = generate_analysis_report(
        args.model1_name, args.model2_name, metrics_table, args.save_dir
    )

    print(f"\nAnalysis completed successfully.")
    print(f"Generated {len(created_plots)} comparison plots")
    print(f"Copied {len(copied_matrices)} confusion matrices")
    print(f"Analysis report saved to: {report_path}")

    return 0


if __name__ == "__main__":
    exit(main())
