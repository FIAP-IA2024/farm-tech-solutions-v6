import os
import subprocess
from pathlib import Path

# Base paths
ROOT_DIR = Path(__file__).resolve().parent.parent
YOLOV5_DIR = ROOT_DIR / "yolov5"
DATA_YAML = ROOT_DIR / "data.yml"


def install_yolov5():
    """Clone YOLOv5 repo and install its dependencies."""
    if not YOLOV5_DIR.exists():
        print("📦 Cloning YOLOv5 repository...")
        subprocess.run(
            ["git", "clone", "https://github.com/ultralytics/yolov5"], cwd=ROOT_DIR
        )
        subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd=YOLOV5_DIR)
    else:
        print("✅ YOLOv5 already installed.")


def create_data_yaml():
    """Generate data.yml with absolute paths to dataset folders."""
    print("📄 Generating data.yml with absolute paths...")
    data_dir = ROOT_DIR / "data"
    yaml_content = f"""
train: {str((data_dir / "train").resolve())}
val: {str((data_dir / "val").resolve())}
test: {str((data_dir / "test").resolve())}

nc: 2
names: ['A', 'B']
"""
    with open(DATA_YAML, "w") as f:
        f.write(yaml_content.strip())
    print("✅ data.yml created successfully.")


def train_model(epochs: int, name: str):
    """Run YOLOv5 training with given number of epochs and experiment name."""
    print(f"\n🚀 Starting training: {epochs} epochs → {name}")
    subprocess.run(
        [
            "python",
            "train.py",
            "--img",
            "640",
            "--batch",
            "8",
            "--epochs",
            str(epochs),
            "--data",
            str(DATA_YAML),
            "--weights",
            "yolov5s.pt",
            "--name",
            name,
        ],
        cwd=YOLOV5_DIR,
    )


def test_model(model_name: str):
    """Run evaluation on test set using a trained model."""
    print(f"\n🧪 Evaluating model on test set: {model_name}")
    weights = YOLOV5_DIR / "runs" / "train" / model_name / "weights" / "best.pt"
    subprocess.run(
        [
            "python",
            "val.py",
            "--data",
            str(DATA_YAML),
            "--weights",
            str(weights),
            "--task",
            "test",
        ],
        cwd=YOLOV5_DIR,
    )


def main():
    print("🔧 Initializing pipeline...")
    install_yolov5()
    create_data_yaml()

    train_model(30, "experiment_30_epochs")
    train_model(60, "experiment_60_epochs")

    test_model("experiment_30_epochs")
    print("\n✅ Done!")


if __name__ == "__main__":
    main()
