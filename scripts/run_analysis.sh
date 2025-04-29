#!/bin/bash
# Script to run the results analysis and generate reports
# UTF-8 encoded

set -e

# Define directories
RESULTS_DIR="results/comparison"
OUTPUT_DIR="${RESULTS_DIR}/analysis_output"
REPORT_FILE="${RESULTS_DIR}/analysis_summary.md"

# Model paths
MODEL_30_TRAIN="${RESULTS_DIR}/train_e30_bs16_20250429_103607"
MODEL_60_TRAIN="${RESULTS_DIR}/train_e60_bs16_20250429_105247"
MODEL_30_VAL="${RESULTS_DIR}/val_best_20250429_112355"
MODEL_60_VAL="${RESULTS_DIR}/val_best_20250429_112434"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "Starting YOLO model training results analysis..."

# Run the analysis script
python scripts/results_analysis.py \
  --model1_train "$MODEL_30_TRAIN" \
  --model2_train "$MODEL_60_TRAIN" \
  --model1_val "$MODEL_30_VAL" \
  --model2_val "$MODEL_60_VAL" \
  --save_dir "$OUTPUT_DIR" \
  --model1_name "30 Epochs" \
  --model2_name "60 Epochs"

# Check if analysis was successful
if [ $? -eq 0 ]; then
  echo "Analysis completed successfully."
  echo "Results saved to $OUTPUT_DIR"
  echo "Analysis report available at $REPORT_FILE"
  
  # Open the analysis summary if on macOS
  if [[ "$OSTYPE" == "darwin"* ]]; then
    open "$REPORT_FILE"
  # Open with xdg-open on Linux
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "$REPORT_FILE"
  fi
else
  echo "Analysis failed with error code $?"
  exit 1
fi

# Print summary of generated visualizations
echo -e "\nGenerated visualizations:"
find "$OUTPUT_DIR" -name "*.png" | sort | while read -r file; do
  echo " - $(basename "$file")"
done

exit 0 